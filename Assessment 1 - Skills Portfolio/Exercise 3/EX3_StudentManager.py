# importing tkinter
import tkinter
# importing everything from tkinter
from tkinter import * 
# imported message box from tkinter
from tkinter import messagebox





# create main window
tkwindow = Tk()
# title of window
tkwindow.title("BSU STUDENT MANAGER")
# icon of window changed, false means it wont show in other widgets
tkwindow.iconphoto(False, PhotoImage(file="Assessment 1 - Skills Portfolio/Exercise 3/files_file_explorer_manager_survey_icon_153069 (1).png"))
# the size of screen
tkwindow.geometry("900x700")



#frames for student manager 
# menu frame
options = Frame(tkwindow)
# group student records frame (has a background color)
studsrecs = Frame(tkwindow, bg= "#22263D")
# individual student records frame (has a background color)
individualstudrec = Frame(tkwindow, bg= "#22263D")
# high score student record
highstud = Frame(tkwindow,bg= "#22263D" )
# low score student record
lowstud = Frame(tkwindow,bg= "#22263D" )
# sort student records frame
sortstud = Frame(tkwindow,bg= "#22263D" )







# variable storing the txt file
studentmarks="Assessment 1 - Skills Portfolio/Exercise 3/studentMarks.txt"
# variable storing text box and placing it in studrecs
textbox = Text(studsrecs, width=80, height=25)
textbox.pack(pady=(100,0))
# text box for individual student results
resulttextbox = Text(individualstudrec, width=70, height=5)
# text box for individual student results
entrybox = Entry(individualstudrec, width=50, font= (90))
# text box for the highest student
highresult = Text(highstud, width=70, height=5)
# text box for the lowest student
lowresult = Text(lowstud, width=70, height=5)
# sorting student records text box
sorttextbox = Text(sortstud, width=80, height=25)







# a function to load all the stuff from the txt file
def markstxt():
    # calls the global variable into the function
    global studentmarks
    # reads each line in the txt file and then stores then in a list and then returns the data
    with open(studentmarks, "r") as filehandling:
        # then reads each line and split by comma
        info = [line.strip().split(",") for line in filehandling]
    return info



# t=a function that returns or takes the second part of the list/string [1] which is the name of the student
def pullstdntname(stdnt):
    return stdnt[1]   




# function to sort students by name alphabetically
# currently reverse is on false so it's in ascending 
def sorting(descending=False):
    
    # clears text box
    sorttextbox.delete("1.0", END)
    stdnts = [h for h in markstxt() if len(h) == 6]
    # sorts the txt file alphabetically by calling the pullstdntname function which checks the name of students
    # parameters has reverse function
    stdnts.sort(key=pullstdntname, reverse=descending)

    sorttextbox.insert(END, "ID     Name               Exam  Course      %       Grade\n")
    sorttextbox.insert(END, "------------------------------------------------------------\n")

    # display each student in formatted table style
    for h in stdnts:
        id, name, course1, course2, course3, finalexam = h
        totalscore = int(course1) + int(course2) + int(course3)
        studentpercentage = percentage(course1, course2, course3, finalexam)
        studentgrade = grade(studentpercentage)

        line = f"{id:<5} {name:<20} {finalexam:<5} {totalscore:<10} {studentpercentage:<10.2f} {studentgrade:<5}\n"
        sorttextbox.insert(END, line)



# a function to calculate percentage
def percentage(course1, course2, course3, finalexam):
    # final score of everything (all marks added together)
    totalscore = int(course1) + int(course2) + int(course3) + int(finalexam)
    # the maximum you can get from your grades is 160 so the sum of the students total score divided by 160 and then multiplied by a 100 turns it into a percentage
    studentpercentage = (totalscore / 160) * 100   
    return studentpercentage



# a function tp calculate grades
def grade(studentpercentage):
    # the student percentage variable passes as an argument here and then it checks the total. if it meets the if elif else criteria then the computer returns the proper grade
    if studentpercentage >= 70:
        return "A"
    elif studentpercentage >= 60:
        return "B"
    elif studentpercentage >= 50:
        return "C"
    elif studentpercentage >= 40:
        return "D"
    else:
        return "F"



def search():
    #clears text box
    resulttextbox.delete("1.0", END)
    # gets input from user in the entry box
    userinput = entrybox.get()
    # pulls/loads the data in the txt file
    stdnt = markstxt()

    # sections heading at top
    resulttextbox.insert(END, "ID     Name               Exam  Course      %       Grade\n")
    resulttextbox.insert(END, "------------------------------------------------------------\n")

    # basically the same in the display() function but with an if statement
    for h in stdnt:
        # without this, there'd be an erorr. this skips lines that are less than 6 values
        if len(h) != 6:  
            # then it continues the code after checking
            continue
        id, name, course1, course2, course3, finalexam = h
        # if the input from the entry box is the same as an ID number in the txt file
        if userinput == id:
            # then it will proceed with the display  
            totalscore = int(course1) + int(course2) + int(course3)
            studentpercentage = percentage(course1, course2, course3, finalexam)
            studentgrade = grade(studentpercentage)
            line = f"{id:<5} {name:<20} {finalexam:<5} {totalscore:<10} {studentpercentage:<10.2f} {studentgrade:<5}\n"
            resulttextbox.insert(END, line)
            return

    # if loop finishes without finding, show message
    messagebox.showinfo("ERROR", "Student not found!")
    


#a function to display the overall student records
def display():
    # got this from gemini because my list would duplicate
    textbox.delete("1.0", END)

    # variable storing the function that loads the txt file
    info = markstxt()  

    # if the first line and the first character of the first line is a digit
    if info[0][0].isdigit():
        # then it will skip to the first liine
        stdnt = info[1:]
        # else include all the info/lines 
    else:
        stdnt = info
   
    # sections heading at top
    textbox.insert(END, "ID     Name               Exam  Course       %       Grade\n")
    textbox.insert(END, "------------------------------------------------------------\n")

    # for loop
    for h in stdnt:
        # every line of student info read, it'll separate them into these variables
        id, name, course1, course2, course3, finalexam = h
        # total sum of marks for each course added in a variable
        totalscore = int(course1) + int(course2) + int(course3)
        # this variable calls the percentage function
        studentpercentage = percentage(course1, course2, course3, finalexam)
        # and then this one calls the grade function
        studentgrade = grade(studentpercentage)
        # then this variable stores each of those variables that i just created with given spaces alignments
        sections = f"{id:<5} {name:<20} {finalexam:<5} {totalscore:<10} {studentpercentage:<10} {studentgrade:<5}\n"
        # then it inserts/prints it into the textbox
        textbox.insert(END, sections)



# highest student marks function
def highmarks ():

    highresult.delete("1.0", END)

    stdnt = markstxt()

    # variable to store the highest total so far
    # its set at zero because that's the lowest you can go
    criteria = 0

    # similar to the other ones except theres a condition
     # without this, there'd be an erorr. this skips lines that are less than 6 values
    for h in stdnt:
        if len(h) != 6: 
            continue
        # calculates
        id, name, course1, course2, course3, finalexam = h
        total = int(course1) + int(course2) + int(course3) + int(finalexam)
        # and if the sum is greater than 
        if total > criteria:
            # this will save the total/highest marks
            criteria = total
            # this will save the student with the highest marks
            highest = h  

        if criteria == 0:
            messagebox.showinfo("ERROR", "")
            return

    # sections heading at top
    highresult.insert(END, "ID     Name               Exam  Course       %       Grade\n")
    highresult.insert(END, "------------------------------------------------------------\n")

    # then the rest of the code displayed
    id, name, course1, course2, course3, finalexam = highest
    totalscore = int(course1) + int(course2) + int(course3)
    studentpercentage = percentage(course1, course2, course3, finalexam)
    studentgrade = grade(studentpercentage)
    line = f"{id:<5} {name:<20} {finalexam:<5} {totalscore:<10} {studentpercentage:<10.2f} {studentgrade:<5}\n"
    highresult.insert(END, line)



# lowest student marks function
# basically the same as highmarks() but different math
def lowmarks ():

    lowresult.delete("1.0", END)

    stdnt = markstxt()

    # variable to store the lowest total so far
    # its set at 170 because that's higher than the max score you can get
    criteria = 170

    # similar to the other ones except theres a condition
     # without this, there'd be an erorr. this skips lines that are less than 6 values
    for h in stdnt:
        if len(h) != 6: 
            continue
        # calculates
        id, name, course1, course2, course3, finalexam = h
        total = int(course1) + int(course2) + int(course3) + int(finalexam)
        # and if the sum is lesser than 
        if total < criteria:
            # this will save the total/lowest marks
            criteria = total
            # this will save the student with the lowesr marks
            lowest = h  

        if criteria == 0:
            messagebox.showinfo("ERROR", "")
            return

    # sections heading at top
    lowresult.insert(END, "ID     Name               Exam  Course       %       Grade\n")
    lowresult.insert(END, "------------------------------------------------------------\n")

    # then the rest of the code displayed
    id, name, course1, course2, course3, finalexam = lowest
    totalscore = int(course1) + int(course2) + int(course3)
    studentpercentage = percentage(course1, course2, course3, finalexam)
    studentgrade = grade(studentpercentage)
    line = f"{id:<5} {name:<20} {finalexam:<5} {totalscore:<10} {studentpercentage:<10.2f} {studentgrade:<5}\n"
    lowresult.insert(END, line)



#  a switching frames function
def changeframe(frames):
    # brings a chosen frame to the front 
    frames.tkraise()   








# places the frames
options.place(x=0, y=0, relwidth=1, relheight=1)
studsrecs.place(x=0, y=0, relwidth=1, relheight=1)
individualstudrec.place(x=0, y=0, relwidth=1, relheight=1)
highstud.place(x=0, y=0, relwidth=1, relheight=1)
lowstud.place(x=0, y=0, relwidth=1, relheight=1)
sortstud.place(x=0, y=0, relwidth=1, relheight=1)





# lowest student record frame customization
# heading/label
Label(lowstud, text="THE BOTTOM STUDENT!", font=("Verdana", 20)).pack(pady=30)
# text box
lowresult.pack(pady=(10,0))

#highest student record frame customization
# heading/label
Label(highstud, text="THE TOP STUDENT!", font=("Verdana", 20)).pack(pady=30)
# text box
highresult.pack(pady=(10,0))





# options frame customization
# background image 
#photoimage feature by tkinter is stored in a variable 'optbg'
optbg = PhotoImage(file="Assessment 1 - Skills Portfolio/Exercise 3/Student Manager.png")
# then i use  a label to display image
bglabel = Label(options, image=optbg)
#places image(it take's up the whole window)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)
# the label/heading
Label(options, text="STUDENT MANAGER", font=("Verdana", 20)).pack(pady=37, padx=150, anchor=W)
# buttons
# student record button
Button(options, text="Student Records",width=25, height=2, font=("Verdana", 15), bg="white", command=lambda: [changeframe(studsrecs), display()]).pack(pady=(20,0), padx=120, anchor=W)
# individual student record button
Button(options, text="Individual Student Records",width=25, height=2, font=("Verdana", 15), bg="white", command=lambda: changeframe(individualstudrec)).pack(pady=(20,0), padx=120, anchor=W)
# highest marks student button
Button(options, text="View the Highest Marks",width=25, height=2, font=("Verdana", 15), bg="white", command=lambda: [changeframe(highstud), highmarks()]).pack(pady=(20,0), padx=120, anchor=W)
# lowest marks student button
Button(options, text="View the Lowest Marks",width=25, height=2, font=("Verdana", 15), bg="white", command=lambda: [changeframe(lowstud), lowmarks()]).pack(pady=(20,0), padx=120, anchor=W)
# sort student records button
Button(options, text="Sort Student Records ",width=25, height=2, font=("Verdana", 15), bg="white", command=lambda: [changeframe(sortstud), sorting()]).pack(pady=(20,0), padx=120, anchor=W)




# individual student record frame customization
# heading/label
# choose student ID because its usually the primary key in data bases
Label(individualstudrec, text="FIND A STUDENT ID NUMBER", font=("Verdana", 20)).pack(pady=30)
# entry box placed underneath the first label
entrybox.pack(pady=(10,0))
Button(individualstudrec, text="SEARCH",width=25, height=2, font=("Verdana", 15), bg="white", command=lambda:search()).pack(pady=50)
# placed the text box underneath the second label
Label(individualstudrec, text="RESULTS", font=("Verdana", 20)).pack(pady=30)
resulttextbox.pack(pady=(10,0))







# sort student records frame customization
# choose student ID because its usually the primary key in data bases
Label(sortstud, text="SORTED ALPHABETICALLY (ASCENDING)", font=("Verdana", 20)).pack(pady=30)
sorttextbox.pack(pady=(10,0))
Button(sortstud, text="ASCENDING", width=25, height=2, font=("Verdana", 10), command=lambda: [changeframe(sortstud), sorting(False)]).pack(pady=(10,0))
Button(sortstud, text="DESCENDING", width=25, height=2, font=("Verdana", 10), command=lambda: [changeframe(sortstud), sorting(True)]).pack(pady=(10,0))





# go back to menu buttons
Button(studsrecs, text="Go Back",width=25, height=2, font=("Verdana", 15), bg="black", fg="white", command=lambda: changeframe(options)).pack(side=BOTTOM, pady=50)
Button(individualstudrec, text="Go Back",width=25, height=2, font=("Verdana", 15),  bg="black", fg="white", command=lambda: [changeframe(options), resulttextbox.delete("1.0", END)]).pack(pady=50)
Button(highstud, text="Go Back",width=25, height=2, font=("Verdana", 15),  bg="black", fg="white", command=lambda: [changeframe(options), highresult.delete("1.0", END)]).pack(pady=50)
Button(lowstud, text="Go Back",width=25, height=2, font=("Verdana", 15),  bg="black", fg="white", command=lambda: [changeframe(options), lowresult.delete("1.0", END)]).pack(pady=50)
Button(sortstud, text="Go Back",width=25, height=2, font=("Verdana", 15),  bg="black", fg="white", command=lambda: changeframe(options)).pack(pady=10)





# raises the options frame to be the first frame you see
changeframe(options)
tkwindow.mainloop()