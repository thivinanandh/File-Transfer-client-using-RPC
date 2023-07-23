import xmlrpc.server
import threading
import socketserver
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
import threading
import time
import pathlib
from pathlib import Path
import hashlib


G_FILE_NAME = []
G_HASH = []


def add(a, b):
    print("[Server] A+b :" , a+b)
    return a + b

def list_files(dir_name):
    return os.listdir(dir_name)

def upload_file(file_name, file_content):
    with open(file_name, 'wb') as f:
        f.write(file_content.data)
    return True

def download_file(file_name):
    file_path = Path(f"{file_name}")
    
    if not file_path.exists():
        print(f"[Server] : File {file_name} does not exist..!")
        

    with open(file_name, 'rb') as f:
        return xmlrpc.client.Binary(f.read())

def delete_file(file_name):
    file_path = Path(f"{file_name}")
    
    if not file_path.exists():
        print(f"[Server] : File {file_name} does not exist..!")
    
    os.remove(file_name)

def rename_file(old_file_name, new_file_name):
    os.rename(old_file_name, new_file_name)
    return True
def sort_array(arr):
    arr.sort()
    return arr


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.localServer = xmlrpc.server.SimpleXMLRPCServer(("localhost",8000),requestHandler=RequestHandler,
                            allow_none=True)
        self.localServer.register_multicall_functions()
        self.localServer.register_function(add,'add') #just return a string
        self.localServer.register_function(sort_array,'sort_array') #just return a string
        self.localServer.register_function(upload_file,'upload_file') #just return a string
        self.localServer.register_function(download_file,'download_file') #just return a string
        self.localServer.register_function(delete_file,'delete_file') #just return a string
        self.localServer.register_function(rename_file,'rename_file') #just return a string

        # print("Created a thread")

    def run(self):
         self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print("Server Running")