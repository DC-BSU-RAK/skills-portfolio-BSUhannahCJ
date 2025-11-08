import tkinter
# importing everything from tkinter
from tkinter import * 
# imports random (its a python module)
import random
# imports messagebox from tkinter
from tkinter import messagebox



# creating main window
tkwindow = Tk()
# title of window
tkwindow.title("Math Quiz!")
# icon of window changed, false means it wont show in other widgets
tkwindow.iconphoto(False, PhotoImage(file="Assessment 1 - Skills Portfolio/Exercises/EX1ICON.png"))
# size of screen
tkwindow.geometry("500x500")





# variables 
# user's score
userscore = 0

# attempts allowed after getting it wrong once
userattempt = 1


# variables used for numbers and operations
num_1 = 0       
num_2 = 0       
opr = '+'

# the question the user is currently on
q_num = 0

# The difficulty the user chose
userlevel = ""





# defined function for switching frames
def frameswitch(frames):
# used because multiple frames are used and i want just one to display at first
    frames.tkraise()    



# random number generator function
def random_num(lvl):
    # if the user is on level easy then it'll generate a random number from 1-9
    if lvl == "Easy":
        min = 1
        max = 9
    # else if the user is on level medium then it'll generate a random number from 10-99
    elif lvl == "Medium":
        min = 10
        max = 99
    # else, the user is on level hard then it'll generate a random number from 1000-9999
    else:
        min = 1000
        max = 9999

    # generates random number from min and max and returns it to the called function
    '''asked chatgpt to help me understand random and randit. 
    randint is a function of random and generates a random integer'''
    return random.randint(min, max)



# random ooperation generator function
def random_operation():
    # it picks a random number, either 1 or 2
    ro = random.randint(1, 2)
    # if it picked one then it'll use addition and return it 
    if ro == 1:
        return '+'
    # else it'll use subtraction and return it
    else:
        return '-'


# new generated questions function
def questions(lvl):
    global userlevel, userattempt, q_num, opr, num_1, num_2 
    
    # q_num is the amount of questions and if its higher than 10
    if q_num >= 10:
        userresults()
        # takes player back to the intro frame
        frameswitch(intro_frame)  
        userscore=0
        q_num=0
        # ends function
        return


    # checks level
    userlevel = lvl
    # resets amount of attempts
    userattempt = 1
    
    # pulls two random numbers based on level by using the random_num function
    num_1 = random_num(lvl)
    num_2 = random_num(lvl)
    # plays the function that chooses a random operation-
    opr = random_operation()

    q_num += 1

    # creates the question 
    the_question = f"[Question {q_num}] {num_1} {opr} {num_2}"

    # displays the question depending on which level the user is on
    # if its easy then it will configure(change) the text to whatever the_question will generate 
    if lvl == "Easy":
        easy_questions.configure(text=the_question)
    # if its medium then it will configure(change) the text to whatever the_question will generate 
    elif lvl == "Medium":
        medium_questions.configure(text=the_question)
    # if its hard then it will configure(change) the text to whatever the_question will generate 
    elif lvl == "Hard":
        hard_questions.configure(text=the_question)
        



# checking system function that checks if user answer is correct or wrong and displays a messagebox
def checking(lvl):
    global userscore, userattempt

    # because python keeps showing me a warning
    userinput = 0

    # gets the user's input/answer using a local variable userinput
    # if user is on the easy level
    if lvl == "Easy":
    # gets user's input from the entry box in the lvl1 frame. 
        userinput = int(entry_easy.get())
    # else if they are on the medium level
    elif lvl == "Medium":
    #it gets user's input from the entry box in the lvl2 frame.
        userinput = int(entry_medium.get())
    #else if gets user's input from the entry box in the lvl3 frame if theyre in the hard level 
    elif lvl == "Hard":
        userinput = int(entry_hard.get())

    # calculates using a local variable correct
    # if the operator is a plus
    if opr == '+':
        # it'll add first number and second number together
        correct = num_1 + num_2
    # else it'll subtract 
    else:
        correct = num_1 - num_2


    # here I do understand what to do and what I should use, but I did ask chatgpt to help me fix the order
    # here it checks the answer
    # this checks if the user's answer matches the computer's
    if userinput == correct:
        # nested if else for giving points. if attempt is 1 then it'll be 10 points and if it's over 1 then it's 5 points
        if userattempt == 1:
            points = 10
        else:
            points = 5
        
        # outside the nested if else
        # the score variable will be equal to or increase by the value of the points variable
        userscore += points
        # messagebox 
        messagebox.showinfo("Correct answer",f"That's correct! You earned {points} points!")

        # then this resets the attempt score
        userattempt = 1

        # brings a new question
        questions(lvl)

    # if the answer of the user is not the same (wrong) as the computer then it will play the else of the outer if-else
    else:
        #nested if-else again. This will check if the attempt for the usre is 1 (this is different because this is in the else section)
        if userattempt == 1:
            # gives one more chance
            userattempt += 1
            # message box 
            messagebox.showinfo("Wrong answer","That's wrong. Please try again!")
            return  # returns and wait's for user to try once more
        # else if they get the attempt wrong again
        else:
            # message box
            messagebox.showinfo("Wrong answer","Sorry, you got it wrong again. Next question!")
            # resets the attempt again and generates a new question
            userattempt = 1
            questions(lvl)


def userresults():
    global userscore, q_num


# simple else elif if checking id the userscore fits the criteria and then prints results
    if userscore>99:
        messagebox.showinfo("Your score","You scored A, great job!")
    elif userscore>80:
        messagebox.showinfo("Your score","You scored B, good job!")
    elif userscore>50:
        messagebox.showinfo("Your score","You scored C, not bad!")
    else:
        messagebox.showwarning("Your score","You scored D, try again!")








# creating frames 
intro_frame = Frame(tkwindow)
lvl1_frame = Frame(tkwindow, bg="pink")
lvl2_frame = Frame(tkwindow, bg="pink")
lvl3_frame = Frame(tkwindow, bg="pink")




# makes the frame visible at 100% width and height
# used help from ChatGPT with the relwidth & relheight because my labels weren't staying in the middle
intro_frame.place(x=0, y=0, relwidth=1, relheight=1)
lvl1_frame.place(x=0, y=0, relwidth=1, relheight=1)
lvl2_frame.place(x=0, y=0, relwidth=1, relheight=1)
lvl3_frame.place(x=0, y=0, relwidth=1, relheight=1)





# tkinter photoimage feature stored in variable 'background'
background = PhotoImage(file="Assessment 1 - Skills Portfolio/Exercises/EX1BACKGROUND.png")
# use a label to display image and chose the intro frame
bg_label = Label(intro_frame, image=background)
# placing of image (it take's up the whole window)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



''' main heading for intro page using label. pink background, 
space size 10 px above, and font/text customization'''
Label(intro_frame, text="Math Quiz!", bg="black", fg="hotpink", font=("Times", 50, "italic", "bold")).pack(pady=(10))

# sub heading for intro page using label. pink background, space size 10 px above, and font/text customization
Label(intro_frame, text="choose your difficulty",fg="hotpink", bg="black", font=("Times", 20, "bold")).pack(pady=(10))



# buttons for difficulty options
# button to switch to easy questions frame
Button(intro_frame, text="Level 1 - Easy!", width=30, height=3, bg="hotpink", font=(1), 
       command=lambda: (frameswitch(lvl1_frame), questions("Easy"))).pack(pady=10)

# button to switch to medium questions frame
Button(intro_frame, text="Level 2 - Medium!", width=30, height=3, bg="hotpink", font=(1), 
       command=lambda: (frameswitch(lvl2_frame), questions("Medium"))).pack(pady=10)

# button to switch to hard questions frame 
Button(intro_frame, text="Level 3 - Hard!", width=30, height=3, bg="hotpink", font=(1), 
       command=lambda: (frameswitch(lvl3_frame), questions("Hard"))).pack(pady=10)







#level 1 easy frame 
#heading
Label(lvl1_frame, text="DIFFICULTY - EASY", bg="pink", font=("Times", 20, "bold")).pack(pady=(10))

#questions
easy_questions = Label(lvl1_frame, text="", font=("Arial", 15), bg="pink")
easy_questions.pack(pady=5)
 
# allows users to enter input
entry_easy = Entry(lvl1_frame, font=("Arial", 20))
entry_easy.place(x=100,y=130)

# button for users to submit answer
Submitbtn=tkinter.Button(lvl1_frame, text="Submit", width=25, height=2, bg="hotpink", command=lambda: checking("Easy"))
# submit button placing
Submitbtn.place(x=50, y=200)
# button for users to go back to intro/menu
Menubtn=tkinter.Button(lvl1_frame, text="Menu",  width=25, height=2, bg="black", fg="pink", command=lambda: (frameswitch(intro_frame), questions("Easy")))
# menu button placing
Menubtn.place(x=270, y=200)







#level 2 medium frame
# heading 
Label(lvl2_frame, text="DIFFICULTY - MEDIUM", bg="pink", font=("Times", 20, "bold")).pack(pady=(10))

#questions
medium_questions = Label(lvl2_frame, text="", font=("Arial", 15), bg="pink")
medium_questions.pack(pady=5)

# allows users to enter input
entry_medium = Entry(lvl2_frame, font=("Arial", 20))
entry_medium.pack(pady=5)

# button for users to submit answer
Submitbtn=tkinter.Button(lvl2_frame, text="Submit", width=25, height=2, bg="hotpink", command=lambda: checking("Medium"))
# submit button placing
Submitbtn.place(x=50, y=200)
# button for users to go back to intro/menu
Menubtn=tkinter.Button(lvl2_frame, text="Menu",  width=25, height=2, bg="black", fg="pink", command=lambda: (frameswitch(intro_frame), questions("Medium")))
# menu button placing
Menubtn.place(x=270, y=200)







#level 3 hard frame 
#heading
Label(lvl3_frame, text="DIFFICULTY - HARD", bg="pink", font=("Times", 20, "bold")).pack(pady=(10))

#questions
hard_questions = Label(lvl3_frame, text="", font=("Arial", 15), bg="pink")
hard_questions.pack(pady=5)

# allows users to enter input
entry_hard = Entry(lvl3_frame, font=("Arial", 20))
entry_hard.pack(pady=5)

# button for users to submit answer
Submitbtn=tkinter.Button(lvl3_frame, text="Submit", width=25, height=2, bg="hotpink", command=lambda: checking("Hard"))
# submit button placing
Submitbtn.place(x=50, y=200)
# button for users to go back to intro/menu
Menubtn=tkinter.Button(lvl3_frame, text="Menu",  width=25, height=2, bg="black", fg="pink", command=lambda: (frameswitch(intro_frame), questions("Hard")))
# menu button placing
Menubtn.place(x=270, y=200)




# showing intro_frame first
frameswitch(intro_frame)
# so it runs and displays 
tkwindow.mainloop()