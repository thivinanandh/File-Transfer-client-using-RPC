import xmlrpc.client
import time
import argparse
import pathlib
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client side')

    parser.add_argument('--upload', action="store", dest="upfile",default='none')
    parser.add_argument('--download', action="store", dest="downfile",default='none')
    parser.add_argument('--rename', action="store", dest="renameFile",default='none')
    parser.add_argument('--delete', action="store", dest="deleteFile",default='none')
    parser.add_argument('--renameTo', action="store", dest="renameFileTo",default='none')
    parser.add_argument('--add', '--list', help='delimited list input', 
    type=lambda s: [float(item) for item in s.split(',')],default=[],action="store")
    parser.add_argument('--sort', help='delimited list input', 
    type=lambda s: [float(item) for item in s.split(',')],default=[],action="store")
    
    # parse arguments
    parsedArgs = parser.parse_args()

    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

    if(parsedArgs.upfile != "none" ):
        my_file = Path(f"{parsedArgs.upfile}")
        if not my_file.is_file():
            print(f"[Client] File {parsedArgs.upfile} does not exist..!")

        with open(parsedArgs.upfile, "rb") as f:
            file_content = xmlrpc.client.Binary(f.read())
            proxy.upload_file(parsedArgs.upfile, file_content)

    elif(parsedArgs.downfile != "none" ):
        with open(parsedArgs.downfile, "wb") as f:
            
            file_content = proxy.download_file(parsedArgs.downfile )
            f.write(file_content.data)

    elif(parsedArgs.renameFile != "none" ):
        proxy.rename_file(parsedArgs.renameFile, parsedArgs.renameFileTo)
    
    elif(parsedArgs.deleteFile != "none" ):
        proxy.delete_file(parsedArgs.deleteFile)

    elif(len(parsedArgs.add) > 0):
       
        sumVal = proxy.add(parsedArgs.add[0],parsedArgs.add[1])
        print("[Client] Sum from server is : ", sumVal)
    
    elif(len(parsedArgs.sort) > 0):
        arr = proxy.sort_array(parsedArgs.sort)
        print("[Client] Sorted Array from server is : ", arr)
    else:
        print("Enter any Arguments")