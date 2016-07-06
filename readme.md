lessonGuideParseTest.py is the correct file to use. This program will take in a directory and update the markdown of the each lesson's readme to contain a table of contents at the top of the page. The lesson readmes should contain all the information needed for the table of contents before running the program. The heading of each section that should be in the table should be in the format "## title: description (time)". To run the program go to the file and find "if __name__ == '__main__':" at the bottom. Below this line, hard code the variable "rootdir" to be set to the path of the directory you want to use. Only run the program once because every time it's run the table will be inserted.





git add readme.md
git commit -m "heres the new readme"
git push origin master
