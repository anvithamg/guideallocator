from cgitb import text
from lib2to3.pgen2.token import NUMBER
import random
from select import select
from pywebio.input import *
from pywebio.output import *

def create_student_record():
    global student 
    student = input("Enter Student File",type = "text")
    student_file = open(student,"w+")
    number_of_students = int(input("Enter the number of students"))
    toast("Enter student names along with their project names")
    for i in range(number_of_students):
        x = input("student name",type="text")
        y = input("project name",type="text")
        student_file.write(x+"-------->"+y+"\n")
    student_file.close()


def create_guide_record():
    global guide 
    guide = input("Enter Guide File",type="text")
    guide_file = open(guide,"w")
    number_of_guides = int(input("Enter the number of guides"))
    toast("Enter guide names")
    for i in range(number_of_guides):
        guide_file.write(input()+"\n")
    guide_file.close()

def delete_student_record():
    x = input("Enter the record to be deleted")
    y = input("Enter project name to be deleted")
    val = x+"-------->"+y
    student_file = open(student)
    student_content = student_file.readlines()
    student_file.close()
    if val in student_content:
        student_content.remove(val)
    student_file = open(student,"w")
    student_content = "\n".join(student_content)
    student_file.write(student_content)
    student_file.close()
    toast("student record has been deleted")

def delete_guide_record():
    val = input("Enter the record to be deleted")
    val = val
    guide_file = open(guide)
    guide_content = guide_file.readlines()
    guide_file.close()
    guide_file = open(guide,"w")
    if val in guide_content:
        guide_content.remove(val)
    guide_content = '\n'.join(guide_content)
    guide_file.write(guide_content)
    guide_file.close()
    toast("Guide record has been deleted")


def allocate_guide():        
    student_file = open(student)
    guide_file = open(guide)
    student_content = student_file.readlines()
    guide_content = guide_file.readlines()
    output_file = open("Output.txt",'w')
    length_student = len(student_content)
    length_guide = len(guide_content)
    val = length_student/length_guide
    random.shuffle(student_content)
    random.shuffle(guide_content)
    for i in guide_content:
        student_count = 1
        for j in student_content:
            if(student_count>=val):
                break
            if(j=="\n"):
                continue
            student_count += 1
            output_file.write(i.rstrip()+":"+j.rstrip()+"\n")
            student_content.remove(j)
    while(len(student_content)>0):
        i=0
        output_file.write(guide_content[i].rstrip()+":"+student_content[i].rstrip()+"\n")
        guide_content.remove(guide_content[i])
        student_content.remove(student_content[i])
        i+1
    popup("The guide and their allocated studenets are written in the file named output.txt")

while(True):
    choice = select("Enter your choice",["1.Adding Student Record and Project","2.Adding Guide Record","3.Deleting Student Record","4.Deleting Guide Record","5.Allocating guide","6.Exit"])
    if choice == "1.Adding Student Record and Project":
        create_student_record()
    elif choice == "2.Adding Guide Record":
        create_guide_record()
    elif choice == "3.Deleting Student Record":
        delete_student_record()
    elif choice == "4.Deleting Guide Record":
        delete_guide_record()
    elif choice == "5.Allocating guide":
        allocate_guide()
    elif choice == "6.Exit":
        exit(0)
    else:
        popup("Enter correct option")
