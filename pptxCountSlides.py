
from pptx import Presentation

directory  = "D:/SEM 03 CSE19/CS 2042 Operating Systems/"
def get_slide_count(path="D:/SEM 03 CSE19/CS 2042 Operating Systems/ch1 Introduction.pptx"):
    p = Presentation(path)
    num = len(p.slides)
    print(num)
    return num


import os

sum_of_slides = 0
missed_files = 0
directory  = "D:/SEM 03 CSE19/CS 2042 Operating Systems/"
content = os.listdir(directory)
for file in content:
    if os.path.isdir(directory+file):
        print(file+" is a directory\n")
    else:
        base,ext = os.path.splitext(file)
        if ext==".pptx":
            print(file+" is a pptx presentation\n")
            sum_of_slides += get_slide_count(directory+file)
            print()
        else:
            print(file+" is not pptx presentation\n")
            missed_files+=1

print(sum_of_slides)
print(missed_files)