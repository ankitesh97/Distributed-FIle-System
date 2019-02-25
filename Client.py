import os
import socket
import sys
import time
import hashlib

addr=[]
port=[]
imp=[]

def put(feed):
    print("In PUT function in client")
    filename=feed.split(' ')[1]
    imp.append(filename)
    print("imp i.e., list of filenames ---->", imp)
    filename1=filename.encode("utf8")  #subfolderName=userInput.split(' ')[2]  #subfolderNameInBytes=subfolderName.encode('utf-8')
    if os.path.isfile(filename):
        print("Yes, the given file exists!")
        f=open(filename, 'rb')
        data=f.read() 
        f.close()
        print("Sending the file to the Server. Please Wait......") #try:
        try:
            s1.send(b'Client demands PUT')
        except:
            pass #time.sleep(3) #except:  #pass #try: 
            
        try:
            s2.send(b'Client demands PUT') #time.sleep(3)  #except:  #pass #try:
        except:
            pass
            
        try:    
            s3.send(b'Client demands PUT') #time.sleep(3)  #except: #pass  #try:
        except:
            pass
            
        try:
            s4.send(b'Client demands PUT') #time.sleep(3)
        except:
            pass
        
        def Hash(data):
            h=hashlib.md5()                                             
            h.update(data)
            h1=h.hexdigest()
            number=int(h1, 16)
            xvalue=number%4
            return xvalue
        xvalue=Hash(data)
        print("Value of x: "+str(xvalue))
        
        chunks=[]
        bytes=len(data)
        indsize=int(bytes/4)
        indsizebytes=str(indsize).encode("utf8")
        
        f=open(filename, 'rb')           #~~~~~From PA-1
        while True:
            datax=f.read(indsize)
            if not datax:
                break
            chunks.append(datax)
           
        """count2=1                        #~~~~~~New Logic
        for i in range(0, bytes, indsize):
            if(count2<4):
                chunks.append(data[i:i+indsize])
            else:
                chunks.append(data[i:])
                break
            count2=count2+1"""
        
        if(xvalue==0):
            try:    
                s1.send(filename1+b',1,2,'+indsizebytes)    #+b','+subfolderNameInBytes)  # time.sleep(2)
                time.sleep(1)
                s1.send(chunks[0]) #time.sleep(2
                print("Patience my friend, sending Chunk1 to server1 :-)")
                time.sleep(2)
                s1.send(chunks[1])  #time.sleep(2)  #except:  #pass
                print("Patience my friend, sending Chunk2 to server1 :-)")
                time.sleep(2)  #try:   
            except:
                pass
            
            try:
                s2.send(filename1+b',2,3,'+indsizebytes)   #+b','+subfolderNameInBytes) #time.sleep(2)
                time.sleep(1)
                s2.send(chunks[1])  #time.sleep(2)
                print("Patience my friend, sending Chunk1 to server2 :-)")
                time.sleep(2)
                s2.send(chunks[2]) #time.sleep(2)  #except: #pass
                print("Patience my friend, sending Chunk2 to server2 :-)")
                time.sleep(2) #try:
            except:
                pass
            
            try:
                s3.send(filename1+b',3,4,'+indsizebytes)    # +b','+subfolderNameInBytes)  #time.sleep(2)
                time.sleep(1)
                s3.send(chunks[2]) #time.sleep(2)
                print("Patience my friend, sending Chunk1 to server3 :-)")
                time.sleep(2)
                s3.send(chunks[3]) #time.sleep(2)  #except:  #pass
                print("Patience my friend, sending Chunk2 to server3 :-)")
                time.sleep(2) #try:
            except:
                pass
            
            try:
                s4.send(filename1+b',4,1,'+indsizebytes)    #+b','+subfolderNameInBytes)  #time.sleep(2)
                time.sleep(1)
                s4.send(chunks[3])
                print("Patience my friend, sending Chunk1 to server4 :-)")
                time.sleep(2)
                s4.send(chunks[0])
                print("Patience my friend, sending Chunk2 to server4 :-)")
                time.sleep(2) #except: #pass
            except:
                pass
            
        elif(xvalue==1):
            try:
                s1.send(filename1+b',4,1,'+indsizebytes)    #+b','+subfolderNameInBytes)  #time.sleep(3)
                time.sleep(1)
                s1.send(chunks[3])
                print("Patience my friend, sending Chunk1 to server1 :-)")
                time.sleep(2) 
                s1.send(chunks[0])
                print("Patience my friend, sending Chunk2 to server1 :-)")
                time.sleep(2)  #except:  #pass  #try:
            except:
                pass
            
            try:
                s2.send(filename1+b',1,2,'+indsizebytes)    #+b','+subfolderNameInBytes)  #time.sleep(3)
                time.sleep(1)
                s2.send(chunks[0]) 
                print("Patience my friend, sending Chunk1 to server2 :-)")
                time.sleep(2)
                s2.send(chunks[1])
                print("Patience my friend, sending Chunk2 to server2 :-)")
                time.sleep(2) #except: #pass  #try:    
            except:
                pass
            
            try:
                s3.send(filename1+b',2,3,'+indsizebytes)      #+b','+subfolderNameInBytes)  #time.sleep(3)
                time.sleep(1)
                s3.send(chunks[1])
                print("Patience my friend, sending Chunk1 to server3 :-)")
                time.sleep(2)
                s3.send(chunks[2])
                print("Patience my friend, sending Chunk2 to server3 :-)")
                time.sleep(2)  #except: #pass #try:
            except:
                pass
            
            try:
                s4.send(filename1+b',3,4,'+indsizebytes)     #+b','+subfolderNameInBytes) #time.sleep(3)
                time.sleep(1)
                s4.send(chunks[2])
                print("Patience my friend, sending Chunk1 to server4 :-)")
                time.sleep(2)
                s4.send(chunks[3])
                print("Patience my friend, sending Chunk2 to server4 :-)")
                time.sleep(2)
            except:
                pass
            
        elif(xvalue==2):
            try:
                s1.send(filename1+b',3,4,'+indsizebytes)    #+b','+subfolderNameInBytes)  #time.sleep(2)
                time.sleep(1)
                s1.send(chunks[2])
                print("Patience my friend, sending Chunk1 to server1 :-)")
                time.sleep(2)
                s1.send(chunks[3])
                print("Patience my friend, sending Chunk2 to server1 :-)")  #except: #pass
                time.sleep(2)  #try:
            except:
                pass
            
            try:
                s2.send(filename1+b',4,1,'+indsizebytes)   #+b','+subfolderNameInBytes)  #time.sleep(2)
                time.sleep(1)
                s2.send(chunks[3])
                print("Patience my friend, sending Chunk1 to server2 :-)")
                time.sleep(2)
                s2.send(chunks[0])
                print("Patience my friend, sending Chunk2 to server2 :-)") #except: #pass
                time.sleep(2) #try:
            except:
                pass
            
            try:
                s3.send(filename1+b',1,2,'+indsizebytes)  #+b','+subfolderNameInBytes)
                time.sleep(1)
                s3.send(chunks[0])
                print("Patience my friend, sending Chunk1 to server3 :-)")
                time.sleep(2)
                s3.send(chunks[1])
                print("Patience my friend, sending Chunk2 to server3 :-)")  #except: #pass
                time.sleep(2) #try:
            except:
                pass
            
            
            try:
                s4.send(filename1+b',2,3,'+indsizebytes)   #+b','+subfolderNameInBytes)
                time.sleep(1)
                s4.send(chunks[1])
                print("Patience my friend, sending Chunk1 to server4 :-)")
                time.sleep(2)
                s4.send(chunks[2])
                print("Patience my friend, sending Chunk2 to server4 :-)") #except:  #pass
                time.sleep(2)
            except:
                pass
            
        elif(xvalue==3):
            try:
                s1.send(filename1+b',2,3,'+indsizebytes)   #+b','+subfolderNameInBytes)
                time.sleep(1)
                s1.send(chunks[1]) 
                print("Patience my friend, sending Chunk1 to server1 :-)")
                time.sleep(2)
                s1.send(chunks[2])
                print("Patience my friend, sending Chunk2 to server1 :-)")
                time.sleep(2)  #except: #pass  #try:
            except:
                pass
            
            try:
                s2.send(filename1+b',3,4,'+indsizebytes)   #+b','+subfolderNameInBytes)
                time.sleep(1)
                s2.send(chunks[2])
                print("Patience my friend, sending Chunk1 to server2 :-)")
                time.sleep(2)
                s2.send(chunks[3])
                print("Patience my friend, sending Chunk2 to server2 :-)")
                time.sleep(2) #except: #pass #try:
            except:
                pass 
            
            try:    
                s3.send(filename1+b',4,1,'+indsizebytes)   #+b','+subfolderNameInBytes)
                time.sleep(1)
                s3.send(chunks[3])
                print("Patience my friend, sending Chunk1 to server3 :-)")
                time.sleep(2)
                s3.send(chunks[0])
                print("Patience my friend, sending Chunk2 to server3 :-)")
                time.sleep(2) #except: #pass  #try:
            except:
                pass
                
            try:
                s4.send(filename1+b',1,2,'+indsizebytes)   #+b','+subfolderNameInBytes) #time.sleep(2)
                time.sleep(1)
                s4.send(chunks[0])
                print("Patience my friend, sending Chunk1 to server4 :-)")
                time.sleep(2)
                s4.send(chunks[1])
                print("Patience my friend, sending Chunk2 to server4 :-)")
                time.sleep(2)  #except:  #pass      #time.sleep(9)  s1.close()    s2.close()   s3.close()    s4.close()
            except:
                pass
            
        print("Success: File successfully sent to servers. Closing all sockets!")
        s1.close()
        s2.close()
        s3.close()
        s4.close()
    else:
        print("Error: The given file does not exist!")
        sys.exit()
        
def get(feed, serv1up, serv2up, serv3up, serv4up):
    dict={}
    print("In GET function in client")
    filename=feed.split(" ")[1]
    filename1=filename.encode("utf8")
    
    if(serv1up=="No" and serv2up=="No"):
        print("Terminating program as 1 chunk of the file would be missing, so cannot get the complete "+filename)
        sys.exit()
    elif(serv2up=="No" and serv3up=="No"):
        print("Terminating program as 1 chunk of the file would be missing, so cannot get the complete "+filename)
        sys.exit()
    elif(serv3up=="No" and serv4up=="No"):
        print("Terminating program as 1 chunk of the file would be missing, so cannot get the complete "+filename)
        sys.exit()
    elif(serv1up=="No" and serv4up=="No"):
        print("Terminating program as 1 chunk of the file would be missing, so cannot get the complete "+filename)
        sys.exit()
        
    if(serv1up=="Yes" and serv3up=="Yes"):        #try:
        s2.close()
        s4.close()
        print("Proceeding to send GET request to Server 1.")
        s1.send(b'Client demands GET')
        time.sleep(2)
        s1.send(filename1)   #+b','+subFolderNameInBytes)    #try:
        time.sleep(2)
        print("Proceeding to send GET request to Server 3.")
        s3.send(b'Client demands GET')
        time.sleep(2)
        s3.send(filename1)        #+b','+subFolderNameInBytes)  #except:   #pass
        time.sleep(2)
        
    elif(serv2up=="Yes" and serv4up=="Yes"):  #try:
        s1.close()
        s3.close()    
        print("Proceeding to send GET request to Server 2.")
        s2.send(b'Client demands GET')
        time.sleep(2)
        s2.send(filename1)       #InBytes+b','+subFolderNameInBytes)  #except:   #pass  #try:
        print("Proceeding to send GET request to Server 4.")
        s4.send(b'Client demands GET')
        time.sleep(2)
        s4.send(filename1)       #InBytes+b','+subFolderNameInBytes)  #except:  #pass
    
    try:    
        serv1msg1=s1.recv(65535)                    #server 1 msg, first chunk
        fname11=serv1msg1.split(b'||')[0]
        data11=serv1msg1.split(b'||')[1]     
        dict[fname11]=data11
        time.sleep(2)
        serv1msg2=s1.recv(65535)                    #server 1 msg, second chunk
        fname12=serv1msg2.split(b'||')[0]
        data12=serv1msg2.split(b'||')[1]     
        dict[fname12]=data12
        time.sleep(2)
    except:
        pass
        
    try:    
        serv2msg1=s2.recv(65535)                    #server 2 msg, first chunk
        fname21=serv2msg1.split(b'||')[0]
        data21=serv2msg1.split(b'||')[1]     
        dict[fname21]=data21
        time.sleep(2)
        serv2msg2=s2.recv(65535)                    #server 2 msg, second chunk
        fname22=serv2msg2.split(b'||')[0]
        data22=serv2msg2.split(b'||')[1]     
        dict[fname22]=data22
        time.sleep(2)
    except:
        pass
    
    try:
        serv3msg1=s3.recv(65535)                    #server 3 msg, first chunk
        fname31=serv3msg1.split(b'||')[0]
        data31=serv3msg1.split(b'||')[1]     
        dict[fname31]=data31
        time.sleep(2)
        serv3msg2=s3.recv(65535)                    #server 3 msg, second chunk
        fname32=serv3msg2.split(b'||')[0]
        data32=serv3msg2.split(b'||')[1]     
        dict[fname32]=data32
        time.sleep(2)
    except:
        pass
        
    try:    
        serv4msg1=s4.recv(65535)                    #server 4 msg, first chunk
        fname41=serv4msg1.split(b'||')[0]
        data41=serv4msg1.split(b'||')[1]     
        dict[fname41]=data41
        time.sleep(2)
        serv4msg2=s4.recv(65535)                    #server 4 msg, second chunk
        fname42=serv4msg2.split(b'||')[0]
        data42=serv4msg2.split(b'||')[1]     
        dict[fname42]=data42
        time.sleep(2)
    except:
        pass
    
    if (len(dict)==4):
        print(filename+": This given file is reconstructible. Reconstructing file, please wait!")
        for keys in sorted(dict.keys()):
            print("Chunk name in serial order for proper file reconstruction", keys)
            b=open('Received_'+filename,'ab')
            b.write(dict[keys])
            b.close()
        print("-------------------Success! Finished reconstructing the file.-------------------")
    else:
        print("-------------------"+filename+": This given file is not reconstructible. Failure!-------------------")  #time.sleep(1)

def List(): #list1=[]  list2=[]   list3=[]  list4=[]  #subFolderNameForList=userInput.split(' ')[1]  #subFolderNameForListInBytes=subFolderNameForList.encode('utf-8')  #try:
    print("In List function in client.")
    try:
        s1.send(b'Client demands LIST')
        time.sleep(1)
    except:
        pass
    
    try: 
        s2.send(b'Client demands LIST')
        time.sleep(1)
    except:
        pass
    
    try:
        s3.send(b'Client demands LIST')
        time.sleep(1)
    except:
        pass
    
    try:
        s4.send(b'Client demands LIST')
        time.sleep(1)
    except:
        pass
    
    print("Request for List sent to all servers.")
    biglist=[]
    biglist1=[]
    biglist2=[]
    biglist3=[]
    biglist4=[]
    
    try:
        while True:
            m1=s1.recv(65535)
            if m1:
                print("Receiving chunk....")
                m2=m1.decode("utf8")
                m66=m2.split("||")[0]
                print("Chunk name present at server 1: ",m66)
                biglist1.append(m66)
            else:
                print("Received all Chunk names from server 1.")
                break   #print("biglist1", biglist1)
    except:
        pass
   
    try:    
        while True:
            m3=s2.recv(65535)
            if m3:
                print("Receiving chunk....")
                m4=m3.decode("utf8")
                m77=m4.split("||")[0]
                print("Chunk name present at server 2: ",m77)
                biglist2.append(m77)
            else:
                print("Received all Chunk names from server 2.")
                break   #print("biglist2", biglist2)
    except:
        pass
        
    try:
        while True:
            m5=s3.recv(65535)
            if m5:
                print("Receiving chunk....")
                m6=m5.decode("utf8")
                m88=m6.split("||")[0]
                print("Chunk name present at server 3: ",m88)
                biglist3.append(m88)
            else:
                print("Received all Chunk names from server 3.")
                break   #print("biglist3", biglist3)
    except:
        pass
        
    try:
        while True:
            m7=s4.recv(65535)
            if m7:
                print("Receiving chunk....")
                m8=m7.decode("utf8")
                m99=m8.split("||")[0]
                print("Chunk name present at server 4: ",m99)
                biglist4.append(m99)
            else:
                print("Received all Chunk names from server 4.")
                break     #print("biglist4", biglist4)
    except:
        pass
        
    biglist=biglist1 + biglist2 + biglist3 + biglist4
    print("biglist i.e., unique chunk names from all servers -------> " , list(set(biglist)))
    time.sleep(2)
    for i in imp:   #print(i)
        p=1
        q=1
        r=0
        while(q<5):
            j=i+"."+str(p)
            if j in biglist:
                q=q+1
                p=p+1
                r=r+1
            else:
                p=p+1
                q+=1
        if(r==4):
            print("-------------------File "+i+" is complete-------------------")
        else:
            print("-------------------File "+i+" is incomplete-------------------")
            
def accept(feed,serv1up,serv2up,serv3up,serv4up):
    if("PUT" in feed):
        put(feed)  
    elif("GET" in feed):                            
        get(feed, serv1up, serv2up, serv3up, serv4up)
    elif("LIST" in feed):                                   #~~~~~Pending
        List()

if (len(sys.argv)==2):
    file77=sys.argv[1]
    print("The configuration file at client is: "+str(file77)) 
    
    while True:    
        feed=input('Options available:(1) PUT <filename> <subfolder>  (2)GET <filename> <subfolder>  (3)LIST <subfolder>\nEnter here:')  #~~~Subfolder ??
        if os.path.isfile(file77):
            fh1=open(file77)
            fh=fh1.readlines()  #print(fh)
            for line in fh:
                strip=line.strip()  #print(strip)
                if line.startswith("Server"):
                    z=(line.split(" ")[2]).split(":")
                    addr.append(z[0])
                    port.append(z[1].strip())
                elif line.startswith("Username"):
                    z1=line.split(":")
                    user=z1[1].strip()
                    user1=user.encode("utf8")
                    print("User:", user1)        #gives result b'Pranit'
                elif line.startswith("Password"):
                    z1=line.split(":")
                    passwd=z1[1].strip()
                    passwd1=passwd.encode("utf8")
                    print("Password:", passwd1)   #gives result b'Pranit777'  print("Address", addr)   print("Port", port)   print(user, user1)  print(passwd, passwd1)
          
        s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s3=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s4=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("##### All sockets created #####")
    
        count=0
        try:    
            s1.connect((addr[0], int(port[0])))
            serv1up="Yes"
            print("Success: Server 1 Up")
        except:
            count=count+1
            serv1up="No"
            print("Error: Server 1 Down")      #pass   #~~~~~~Pending
        
        try:
            s2.connect((addr[1], int(port[1])))
            serv2up="Yes"
            print("Success: Server 2 Up")
        except:
            count=count+1
            serv2up="No"
            print("Error: Server 2 Down")     #pass
        
        try:
            s3.connect((addr[2], int(port[2])))
            serv3up="Yes" 
            print("Success: Server 3 Up")
        except:
            count=count+1
            serv3up="No"
            print("Error: Server 3 Down")      #pass
        
        try:
            s4.connect((addr[3], int(port[3])))
            serv4up="Yes"
            print("Success: Server 4 Up")
        except:
            count=count+1
            serv4up="No"
            print("Error: Server 4 Down")     #pass
        
        if(count==4):                           #~~~~ Pending
            print("Error: All Servers Down. Terminating Client Program!")
            sys.exit()
            
        print("Authenticating User...........")  
        count1=0                      
        try:
            s1.send(user1+b':'+passwd1)   #time.sleep(2)   #sock1.settimeout()
            servermsg1=s1.recv(65535)  #sock1.settimeout(1)  #except:  #pass  #try:
            if b'Invalid' in servermsg1:
                count1=count1+1
            else:
                print("Server 1: Authentication Successful.")
        except:
            print("Data for authentication cannot be sent to server 1 as it is down.")
        
        try:
            s2.send(user1+b':'+passwd1) #time.sleep(2) #sock2.settimeout(1)
            servermsg2=s2.recv(65535) #except: #pass #try:
            if b'Invalid' in servermsg2:
                count1=count1+1
            else:
                print("Server 2: Authentication Successful.")
        except:
            print("Data for authentication cannot be sent to server 2 as it is down.")
        
        try:
            s3.send(user1+b':'+passwd1) #time.sleep(2) #sock3.settimeout(1)
            servermsg3=s3.recv(65535) #except: #pass #try:
            if b'Invalid' in servermsg3:
                count1=count1+1
            else:
                print("Server 3: Authentication Successful.")
        except:
            print("Data for authentication cannot be sent to server 3 as it is down.")
        
        try:
            s4.send(user1+b':'+passwd1)  #time.sleep(2) #sock4.settimeout(1)
            servermsg4=s4.recv(65535) #except: #pass #try:
            if b'Invalid' in servermsg4:
                count1=count1+1
            else:
                print("Server 4: Authentication Successful.")
        except:
            print("Data for authentication cannot be sent to server 4 as it is down.")
        
        if(count1==0):
            print("Hurray, successful username/password authentication from respective servers!")
            accept(feed ,serv1up,serv2up,serv3up,serv4up)
        else:
            print("Error: Invalid Username or Password.")
            #sys.exit()

else:
    print("Error: Please enter sys.argv[0]=.py file name and sys.argv[1]=dfc.conf!")
    sys.exit()