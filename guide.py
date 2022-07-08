import random
import pywebio.input as pywebio_input
import pywebio.output as pywebio_output
import os 


def create_student_record():
    global student
    student = pywebio_input.input("Enter Student File", type="text")
    try:
        student_file = open(student,"r")
        student_lines = student_file.readlines()
        if(len(student_lines)>0):
            return
    except:
        with open(student, "w") as student_file:
            number_of_students = pywebio_input.input(
            "Enter the number of students")
            if  not number_of_students.isdigit():
                pywebio_output.toast("Enter a number")
                return
            number_of_students = int(number_of_students)
            pywebio_output.toast(
                "Enter student usn, names and their project names")
            for i in range(number_of_students):
                usn = pywebio_input.input("Student usn")
                student_file.write(usn+"|")
                name = pywebio_input.input("student name", type="text")
                student_file.write(name+"|")
                proj = pywebio_input.input("project name", type="text")
                student_file.write(proj+"\n")


def create_guide_record():
    global guide
    guide = pywebio_input.input("Enter Guide File", type="text")
    try:
        guide_file = open(guide,"r")
        guide_lines = guide_file.readlines()
        if(len(guide_lines)>0):
            return
    except:
        with open(guide, "w") as guide_file:
            number_of_guides = pywebio_input.input(
                "Enter the number of guides")
            if  not number_of_guides.isdigit():
                pywebio_output.toast("Enter a number")
                return
            number_of_guides = int(number_of_guides)
            for i in range(number_of_guides):
                guide_file.write(pywebio_input.input(f"Enter Guide {i+1}")+"\n")


def delete_student_record():
    if "student" not in globals() or not os.path.exists(student):
        pywebio_output.toast("Student File Not found")
        return
    usn = pywebio_input.input("Enter USN of the record to be deleted")
    items = {}
    with open(student) as student_file:
        lines = student_file.readlines()
        for line in lines:
            temp = line.strip()
            row_items = temp.split("|")
            items[row_items[0]] = row_items
    if usn not in items.keys():
        pywebio_output.toast("No record is present with the given USN :"+usn)
        return
    items.pop(usn)
    with open(student, "w") as student_file:
        for item in items.values():
            student_file.write("|".join(item)+"\n")
    pywebio_output.toast("Student record has been deleted")



def delete_guide_record():
    if "guide" not in globals() or not os.path.exists(guide):
        pywebio_output.toast("Guide File Not found")
        return
    val = pywebio_input.input("Enter the record to be deleted")
    val = val + "\n"
    with open(guide) as guide_file:
        guide_content = guide_file.readlines()
    if val not in guide_content:
        pywebio_output.toast("Record not found")
        return
    with open(guide, "w") as guide_file:
        guide_content.remove(val)
        guide_content = '\n'.join(guide_content)
        guide_file.write(guide_content)
    pywebio_output.toast("Guide record has been deleted")

def modify_student_record():
    if "student" not in globals() or not os.path.exists(student):
        pywebio_output.toast("Student File Not found")
        return
    usn = pywebio_input.input("Enter usn of the student record to be modified")
    items = dict()
    with open(student) as student_file:
        lines = student_file.readlines()
        for line in lines:
            temp = line.strip()
            row_items = temp.split("|")
            items[row_items[0]] = row_items
    if usn not in items.keys():
        pywebio_output.toast("No record is present with the given USN :"+usn)
        return
    old_name = items[usn][1]
    old_proj = items[usn][2]
    new_name = pywebio_input.input(f"Enter new name (current value: {old_name}) Leave blank to not modify")
    if new_name == "":
        new_name = old_name
    new_proj = pywebio_input.input(f"Enter new name (current value: {old_proj}) Leave blank to not modify")
    if new_proj == "":
        new_proj = old_proj
    items[usn] = [usn, new_name, new_proj]
    with open(student, "w") as student_file:
        for item in items.values():
            student_file.write("|".join(item)+"\n")
    pywebio_output.toast("Your Record has been successfully modified")

def allocate_guide():
    if "student" not in globals() or not os.path.exists(student):
        pywebio_output.toast("Student File Not found")
        return
    if "guide" not in globals() or not os.path.exists(guide):
        pywebio_output.toast("Guide File Not fount")
        return
    student_file = open(student,"r")
    guide_file = open(guide,"r")
    student_content = student_file.readlines()
    guide_content = guide_file.readlines()
    output_file = open("Output.txt", 'w')
    length_student = len(student_content)
    length_guide = len(guide_content)
    if length_guide == 0:
        pywebio_output.toast("No guides to Allocate")
        return
    if length_student == 0:
        pywebio_output.toast("No Students to Allocate")
        return
    val = length_student/length_guide
    random.shuffle(student_content)
    random.shuffle(guide_content)
    for i in guide_content:
        student_count = 1
        for j in student_content:
            if(student_count >= val):
                break
            if(j == "\n"):
                continue
            student_count += 1
            output_file.write(i.rstrip()+":"+j.rstrip()+"\n")
            student_content.remove(j)
    while(len(student_content) > 0):
        i = 0
        output_file.write(guide_content[i].rstrip(
        )+":"+student_content[i].rstrip()+"\n")
        guide_content.remove(guide_content[i])
        student_content.remove(student_content[i])
        i+1
    pywebio_output.popup(
        "The guide and their allocated studenets are written in the file named output.txt")


if __name__ == '__main__':
    while(True):
        choice = pywebio_input.select("Enter your choice", ["1.Adding Student Record and Project", "2.Adding Guide Record",
                                      "3.Deleting Student Record", "4.Deleting Guide Record","5.Modify Student Record","6.Allocating guide", "7.Exit"])
        if choice == "1.Adding Student Record and Project":
            create_student_record()
        elif choice == "2.Adding Guide Record":
            create_guide_record()
        elif choice == "3.Deleting Student Record":
            delete_student_record()
        elif choice == "4.Deleting Guide Record":
            delete_guide_record()
        elif choice == "5.Modify Student Record":
            modify_student_record()
        elif choice == "6.Allocating guide":
            allocate_guide()
        elif choice == "7.Exit":
            exit(0)
        else:
            pywebio_output.popup("Enter correct option")