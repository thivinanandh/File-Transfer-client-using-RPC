# RPC Based server for file operations

## Description 

Remote Procedure Call is referred to as RPC in Python. It is a protocol for sending a request via a network to another computer in order to have that computer carry out a certain function or process. The server receives a request message from the caller (client), asking it to carry out a specific function or operation, and responds with a response message containing the function's outcome. The XML-RPC protocol, which is a compact and straightforward mechanism for making RPC calls over HTTP, is implemented in Python by the xmlrpc package.


## Server setup 

run the follwoing on server folder to start the server setup . Enter into server directory and run

```
python3 server.py
```

it will listen to the port of `8000` by default.


## Client setup 

Run the following to run client based problems from client side. Enter into client directory and run

```
python3 client.py
```

## Sync setup

To sync the client folder with server, run the following 

```
python3 syncFolder.py
```


# FILE OPERATIONS
---

## Upload
---

to upload a file use 

```
python3 client.py --upload <filename>
```
eg:

```
python3 client.py --upload client_1.txt
```


## Delete
---

to delete a file use 

```
python3 client.py --delete <filename>
```
Eg
```
python3 client.py --delete server_22.txt
```

## Download
---

to download a file from server side, we can use

```
python3 client.py --download <filename>
```
Eg
```
python3 client.py --download server_2s.txt
```

## Rename
---

to Rename a file on server side, we can use

```
python3 client.py --rename <actualFileName> --renameTo <changeToFileName>
```
Eg
```
python3 client.py --rename server_3.txt --renameTo server_4.txt
```

## Add

To add two numbers

```
python3 client.py --add 5,3
```

## Sort Array 

To sort the array , pass the aray as argument 

```
python3 client.py --sort 50,3,8,1,76,34
```


# Sync Code
----

## New file addition

When new file is added

```
[Client] : Server Check running at :  2023-02-05 02:10:58.256692
File Newly added :  client_1 (copy).txt
File uploaded :  client_1 (copy).txt
[Client] : Server Check running at :  2023-02-05 02:11:03.272496
[Client] : Server Check running at :  2023-02-05 02:11:08.276592
```

## File Deletion 

When file is deleted 

```
[Client] : Server Check running at :  2023-02-05 02:11:43.314352
[Client] File  client_1 (copy).txt  is deleted
```

## File modification

When file is modified

```
[Client] : Server Check running at :  2023-02-05 02:12:08.340497
File Modified :  client_2.txt
File Uploaded :  client_2.txt
```
