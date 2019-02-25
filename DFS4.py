import os
import socket
import threading
import time
import sys

def put(userrecv, conn):
    print("In put function in server 4.")
    while True:   #try:  
        pdata=conn.recv(65535)     #~~~ receives b'filename,1,2,individualfilesize' -------------- (3)
        dataDFS1=pdata 
        if (len(dataDFS1)>0):
            #print("Data Received For Server 1", dataDFS1)
            dataDFS2=dataDFS1.decode("utf8")
            pdata2=dataDFS2.split(',')
            filename=pdata2[0]  #filenameToWrite=filenameToWrite1.split(',')[0]
            fnumber1=pdata2[1]
            fnumber2=pdata2[2]
            indfilesize=pdata2[3]  #subfolderNameToWrite=pdata2[4]        #~~~~Pending
            print("Detailed description of data for Server 4:", filename," ",fnumber1," ",fnumber2," ",indfilesize)
            path=".\\"+directory1+"\\"+userrecv
            if not os.path.exists(path):
                os.makedirs(path)            
        else:      #clientConn.close()
            break      #except: #clientConn.close() #break #time.sleep(2)
        
        chunk1=conn.recv(65535)            #~~~ receives Chunk1 for this server -------------- (4)
        if(len(chunk1)>0):
            o=open(path+"\\"+filename+"."+fnumber1, "wb")
            o.write(chunk1)
            o.close()
        else:
            break
        
        chunk2=conn.recv(65535)            #~~~ receives Chunk2 for this sever --------------- (5)
        if (len(chunk2)>0):
            o=open(path+"\\"+filename+"."+fnumber2, "wb")
            o.write(chunk2)
            o.close()
        else:
            break
    print("Server 4 done with PUT function!")
    
def get(userrecv, conn):
    print("In get function in server 4.")
    gdata=conn.recv(65535)  #if len(gdata)>0:
    gdata1=gdata.decode("utf8")                       # NOTE: Here gdata1 is the filename!!!!! Didn't deal with filesize in GET
    path=".\\"+directory1+"\\"+userrecv
    listoffiles=os.listdir(path+"\\")
    nameofchunk=[]
    dataoffile=[]
    for i in listoffiles:
        if (gdata1 in i):
            nameofchunk.append(i.encode("utf8"))
            oo=open(path+"\\"+i,'rb')
            datag=oo.read()
            oo.close()
            dataoffile.append(datag)
            time.sleep(10)
            
    print("Sending: 1)chunk1 name  2)chunk1 data")
    conn.send(nameofchunk[0]+b'||'+dataoffile[0])
    time.sleep(2)
    print("Sending: 1)chunk2 name  2)chunk2 data")
    conn.send(nameofchunk[1]+b'||'+dataoffile[1])
    time.sleep(2)
    print("Server 4 done with GET function!")
    conn.close()
    
def list(userrecv, conn):
    print("In list function in server 4.")
    path=".\\"+directory1
    files1=os.listdir(path)  #print("files1", files1)
    files3=[]
    for i in files1:
        files2=os.listdir(path+"\\"+i)
        files3=files3+files2
    print("files3", files3)
    time.sleep(28)
    for i in files3:
        conn.send(i.encode("utf8")+b"||")
        print("Sending chunk in encoded format. Please wait!")
        time.sleep(1)
    conn.close()
    print("Server 4 done with LIST function!")

def check(data):
    if data in userpwd:
        print("In check function in server 4.")
        return "True"
    else:
        return "False"

def thread(conn, clientaddr):
    try:
        while True:
            print("In thread function in server 4.")  #try:
            data=conn.recv(65535)    #~~~ receives b'Pranit:Pranit777' -------------- (1)
            print("Data for user authentication from Client", data)
            data1=data.decode("utf8")
            userrecv=data1.split(":")[0]
            condition=check(data)
            if(condition=="True"):
                print("Value returned TRUE from check function")
                conn.send(b'Success: Username and Password Correct')   #time.sleep(2)
                data2=conn.recv(65535)      #~~~ receives b'Client demands PUT' -------------- (2)
                data3=data2.decode("utf8")  #print("d1",d1)
                print("----data3", data3)
                clientdata=data3.split(' ')[2]
                clientdata1=clientdata   #print(performFunction,"Till Here1")
                if ("PUT"==clientdata1):
                    print("**PUT found in clientdata1. Proceeding to PUT function**")
                    put(userrecv, conn)
                elif("GET"==clientdata1):
                    print("**GET found in clientdata1. Proceeding to GET function**")
                    get(userrecv,conn)
                elif("LIST"==clientdata1):
                    print("**LIST found in clientdata1. Proceeding to LIST function**")
                    list(userrecv,conn)
                        
            elif(condition=="False"):
                    conn.send(b'Invalid Username or Password')  #except:  #pass
    except:
        pass
    
def mthread2():  #Handles Keyboard Interrupt
    while 1:
        try:
            input()
        except Exception:
            os._exit(1)

def main():    #try :
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ("Success: Socket created")  #except:  #print ('Failed to create socket.')   #try:
    s.bind((Host, int(Port1)))
    print ("Socket bind successful")  #except:  #print ('Bind failed.')
    backlog=10
    s.listen(backlog)
    while True:
        s1=threading.Thread(target=mthread2)
        s1.start()
        conn, clientaddr=s.accept()
        thread(conn, clientaddr)
        #t= threading.Thread(target=ClientThread, args=(clientConn,clientAddr))
        #t.start()  #except:   #print("Internal Error")

if(len(sys.argv)==3):
    directory=sys.argv[1]
    directory1=directory.split('/')[1]  #print(directory1)
    Port1=int(sys.argv[2])
    Host='127.0.0.1'  #print(Host, Port1) 
    
    user=[]
    passwd=[]
    userpwd=[]
    if os.path.isfile("dfs.conf"):
        print("Yes, the given file exists!")
        fh=open('dfs.conf')
        data=fh.readlines()
        for line in data: #print(line)
            a=line.split(" ")
            user.append(a[0].encode("utf8"))
            passwd.append(a[1].encode("utf8"))  #print(user)  #print(passwd)
    else:
        print("Error: The given file does not exist!")
    i=0
    while i<len(user):
        userpwd.append(user[i]+b':'+passwd[i].strip())
        i=i+1
    print(userpwd)     ##prints [b'Pranit:Pranit777',  b'Jaya:Jaya777']
    
    main()
else:
    print("Error: Please provide sys.argv[0]=.py file name, sys.argv[1]=/DFS4 and sys.argv[2]=10004!")
    sys.exit()