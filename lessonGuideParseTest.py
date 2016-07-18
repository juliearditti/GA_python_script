'''
Created on Jul 6, 2016

@author: juliearditti
'''
'''
Created on Jul 5, 2016

@author: juliearditti
'''
import re

import os
from CodeWarrior.Standard_Suite import files

#loop through each file in directory and find readme.md of lessons
def findFiles(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file == "readme.md" and "lesson" in subdir:

                filetolist(os.path.join(subdir, file))


#takes in a file and makes a list of strings where each string is a line in the file
def filetolist(file):
    listinfo = []
    f = open(file)
    for line in f:
        line = line.strip()
        listinfo.append(line)
    f.close()
    listLines = parse(listinfo)
    replace(listLines, file)

#put new markdown textbox in original file
def replace(list, file):

    fileO = open(file, "r+")
    index = 0
    for i, line in enumerate(fileO):                #find location where table of contents should be
        if "Opening" in line:
            index = i-1
    fileO.close()

    f =open(file)
    contents = f.readlines()
    for l in list:                                  #insert table of contents in file
        contents.insert(index, l)
        index+=1

    f.close()
    f = open(file, "w")
    f.writelines(contents)
    f.close()

#turns list of strings of file lines into a list of strings with the markdown version of the table
def parse(lines):
    listNew = []
    listNew.append("\n")                                 #create first few line template
    listNew.append("### LESSON GUIDE"+"\n")
    listNew.append("\n")
    listNew.append("| TIMING  | TYPE  | TOPIC  |"+"\n")
    listNew.append("|:-:|---|---|"+"\n")

    #create variables
    for line in lines:
        if "(" in line and line[0:3] == "## ":                       #if its a header of a section that should be in the chart
            parStart =line.index("(")
            firstColon = line.find(":")
            minStart=line.rfind("m")
            time = line[parStart+1:minStart-1]

            if firstColon != -1:                                  #create title variable
                title = line[3:firstColon]
            else:
                title = line[3:parStart-1]

            if title == "Opening":                                  #create description variable
                description = "Discuss lesson objectives"
            elif title == "Conclusion":
                description = "Review / Recap"
            else:
                lastColon = line.rfind(":")
                if lastColon == -1:
                    description = " "
                else:
                    description = line[lastColon+2: parStart-1]
            link = line[3:].lower()
            regex = '[^\w,\s]'
            link = re.sub(regex,'', link)
            link = link.split()
            link = '-'.join(link)

            #put it all together

            listNew.append("| " +time+" min  | ["+title+"](#"+link+")  | "+description+" |"+ "\n")

    return listNew

if __name__ == '__main__':

    # hardcode what your rootdir is
    rootdir = '/Users/juliearditti/ADI-course-materials'
    findFiles(rootdir)

    
