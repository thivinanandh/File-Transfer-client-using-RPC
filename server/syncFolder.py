import xmlrpc.client
import time
import argparse
import pathlib
from pathlib import Path
import hashlib
import os
from datetime import datetime

if __name__ == '__main__':
    ## get a list of files and store them for initial reference
    path = Path('.')    
    k = list(path.iterdir())
    fileList = [f"./{kk.name}" for kk in k]
    print(fileList)
    dateList = []

    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") 
    
    ## print summary of files 
    for file in fileList:
        print("---------------------------------------------------")
        print("| S.No   |  FileName        |        Date         |")
        print("---------------------------------------------------")
        
        for i,file in enumerate(fileList):
            date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
            date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            dateList.append(date_time_obj)
            print(f"| {i+1:<7}| {file[2:]:17}| {date:<20}|")
            with open(file, "rb") as f:
                file_content = xmlrpc.client.Binary(f.read())
                proxy.upload_file(file, file_content)

                print("File Uploaded : " , file[2:])

        print("---------------------------------------------------")

    

    lastCheckTime = datetime.now()


    while(True):
        now = datetime.now()
        print("[Client] : Server Check running at : ",now)
        path = Path('.')    
        k = list(path.iterdir())
        newfileList = [f"./{kk.name}" for kk in k]
        ## Detect deleted files
        for i,file in enumerate(fileList):
            if(file not in newfileList):
                print("[Client] File " , file[2:] , " is deleted")
                proxy.delete_file(file)
                fileList.remove(file)
                del dateList[i]

                

        ##check if existing files are modified
        for i,file in enumerate(fileList):
            date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
            date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            
            if(date_time_obj >= lastCheckTime):
                print("File Modified : " , file[2:])

                ## Upload the file to Server
                my_file = Path(f"{file}")

                with open(file, "rb") as f:
                    file_content = xmlrpc.client.Binary(f.read())
                    proxy.upload_file(file, file_content)

                print("File Uploaded : " , file[2:])

        ## check if any file is added 

        newDate_L = []

        for i,file in enumerate(newfileList):
            date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
            date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            newDate_L.append(date_time_obj)
            if(file not in fileList):
                print("File Newly added : " , file[2:])

                ## Upload the file to Server
                my_file = Path(f"{file}")

                with open(file, "rb") as f:
                    file_content = xmlrpc.client.Binary(f.read())
                    proxy.upload_file(file, file_content)

                print("File uploaded : " , file[2:])
        

        dateList = newDate_L
        fileList = newfileList.copy()
        lastCheckTime = datetime.now()
        # print(f"END ------- {fileList=}")
        time.sleep(5)

