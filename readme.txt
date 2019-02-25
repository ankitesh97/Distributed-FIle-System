Author: Pranit Yadav
Python version: 3.5.2
Fourth Scoekt Programming Assignment

Functionality:
1)Python 3.0-3.5 has been used for this code.
2)A total of 5 codes have been written which comprises of 4 server codes(which are all similar) and 1 client code.

=========Client=========
--(To run the client code, enter the following on command prompt-> python Client.py dfc.conf)--
3)In the beginning, 4 sockets are created to connect to 4 different servers. If a particular socket fails to connect, it means that particular server is down. If all sockets failed to get connected, the program is exited. Later, the dfc.conf file consists of the username and its password which are sent to the 4 servers for authentication. If authentication fails from any server, the further operations are not performed on that server. If authentication fails from all servers, the user has to enter valid username and password that is present in the dfs.conf file.
3)Then the user is asked for the operation he wishes to perform like 1)PUT <filename>, 2)GET <filename> or 3)LIST.
4)PUT==>In the PUT function, the file is divided into 4 chunks, its hash value is calcualted, x=hash's value%4 and depending on the value of x that we get, we send (PUT) the chunks to the respective servers. The files are stored in the folder which is dynamically created by the program. The folder is named after the user which is authenticated to perform operations In short, the file is divided into 4 chunks and distributed across the 4 servers user's folder as mentioned below-
x	DFS1	DFS2	DFS3	DFS4
0	(1,2)	(2,3)	(3,4)	(4,1)
1	(4,1)	(1,2)	(2,3)	(3,4)
2	(3,4)	(4,1)	(1,2)	(2,3)
3	(2,3)	(3,4)	(4,1)	(1,2)	
4)For example as seen above, if we get x=0, we send(PUT) the 1st and 2nd chunk in /server1/user folder, the 2nd and 3rd chunk in /server2/user folder, the 3rd and 4th chunk in /server3/user folder, the 4th and 1st chunk in /server4/user folder. If seen closely, 1 chunk is sent to 2 servers.
5)On closely observing again, it can be seen that server1 and server3 have the chunks which complete the file. Same is the case with server2 and server4.
6)GET==>If the user demands(GET) a particular file and if suppose server1 and server2 are down, 1 chunk of the file would be missing and therefore the complete file cannot be reconstructed. Same is the case with server2-server3, server3-server4 and server4-server1. Later, the client code checks if server1 and server3 are up as they contain the complete file. If not, the file is obtained from server2 and server4. In this way only 4 chunks and not 8 chunks of the file are obtained by means of which the file is reconstructed, i.e., Optimized GET is implemented.
7)LIST==>The list function retrieves the names of the chunks present at every server's user folder. If all the chunks of the file are present, the file is termed as complete, else incomplete.

=========Server=========
--(To run the server code, enter the following on command prompt-> python DFS1.py /DFS1 10001)--
1)The server first checks for the user authentication from the client.
2)On authenticating, depending on the operation that the user wants to perform, respective functions are called-1)PUT, 2)GET or 3)LIST
3)PUT==>Stores the chunks received from the client in the user's folder.
4)GET==>If this server is up, the chunks present in the user's folder are sent for reconstructing purposes.
5)LIST==>Sends the name of the chunks present in the user's folder.

*Keyboard interrupt has been handled.(Ctrl+C).
*Error handling has been done at every possible step. For eg, if dfc.conf and dfs.conf files are not present, an error is displayed.
*Submission consists of 1 client code, 4 server codes, a readme file, dfc.conf, dfs.conf, 2 files for transfer purposes namely-Foo1.jpg and Foo2.txt.
