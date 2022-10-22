#! /usr/bin/env python3

import os
import requests

#add source directory containing text files
src_dir="/data/feedback/"

#list all files in th directory
files=os.listdir(src_dir)

#read each lines from the files.
def readlines(file):
        with open(src_dir + file) as f:
                lines=f.read().splitlines()
        return lines

feedback=[]
#define keys
keys=["title","name","date","feedback"]
for file in files:
        lines=readlines(file)
        feedback.append(dict(zip(keys,lines)))

#add the url of the website
url= "http://localhost/feedback/"

#post data using requests module.
for entry in feedback:
        response=requests.post(url,data=entry)
        if response.ok:
                print("loaded entry")
        else:
                print(f"load entry error:{response.status_code}")
