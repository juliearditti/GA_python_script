'''
Created on Jul 5, 2016

@author: juliearditti
'''


import os
#from CodeWarrior.Standard_Suite import files

#loop through each file in directory and find readme of lessons
def findFiles(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file == "readme.md" and "lesson" in subdir:
                
                #print os.path.join(subdir, file)
                filetolist(os.path.join(subdir, file))
                
                
#takes in a file and returns a list of strings where each string is a line in the file            
def filetolist(file):
    listinfo = []
    f = open(file)
    for line in f:
        
        line = line.strip()
        
        listinfo.append(line)
    
      
    f.close()
    newFile = parse(listinfo)
    return newFile

#turns list of strings of file lines into a new file with the markdown version of the table
def parse(lines):
    
    #create first few line template
    returnFile = open("output.txt", "wb")
    returnFile.write("### LESSON GUIDE"+ "\n"+"| TIMING  | TYPE  | TOPIC  |"+ "\n"+"|:-:|---|---|"+ "\n")
    
    #create variables
    
    for line in lines:
        if "(" in line and line[0:3] == "## ":                       #if its a header of a section that should be in the chart                           
            parStart =line.index("(")
            firstColon = line.find(":")
            minStart=line.rfind("m")
            time = line[parStart+1:minStart-1]
            
            if firstColon != -1:
                title = line[3:firstColon]
            else:
                title = line[3:parStart-1]
            if title == "Opening":
                description = "Discuss lesson objectives"
            elif title == "Conclusion":
                description = "Review / Recap" 
            else:   
                lastColon = line.rfind(":")
                if lastColon == -1:
                    description = " "
                else:
                    description = line[lastColon+2: parStart-1]
            if " " in title:
                
                title2 = title.lower().split()[0]+"-"+title.lower().split()[1]
            else: 
                title2 = title.lower()
            #put it all together
            
            returnFile.write("| " +time+" min  | ["+title+"](#"+title2+")  | "+description+" |"+ "\n")
    
    returnFile.close()
   
    return returnFile        
    
if __name__ == '__main__':
    # hardcode what your rootdir is
    rootdir = '/Users/juliearditti/ADI-course-materials'
    findFiles(rootdir)
    
    