import tkinter
# importing everything from tkinter
from tkinter import * 
# for sound, I imported pygame
import pygame 
# imports random
import random



# create main window
tkwindow = Tk()
# title of window
tkwindow.title("Alexa the Comedian")
# icon of window changed, false means it wont show in other widgets
tkwindow.iconphoto(False, PhotoImage(file="Assessment 1 - Skills Portfolio/Exercise 2/icons8-laughing-32.png"))
# the size of screen
tkwindow.geometry("700x500")
# starts the sound mixer system
pygame.mixer.init()




# variable with the random jokes txt file
joketxt= "Assessment 1 - Skills Portfolio/Exercise 2/randomJokes.txt"

# function for pulling text(jokes) from txt file
def jokes():
    # calls the global variable into the function
    global joketxt
    # reads each line in the txt file and then stores then in a list and then returns the list of jokes
    with open(joketxt, "r") as filehandling:
        jokelines = [line for line in filehandling]
    return jokelines


# defined fucntion to display joke
def display():
    # varaible uses random by python to choose (choice) a random joke line from the text file which then this variable is used in the jokelbl.configure
    inputjoke = random.choice(jokes())
    # configures the text in the jokelbl when the function is called (when the 'yes' button and or 'next joke' button is pressed)
    jokelbl.configure(text=inputjoke)


# switching frames function
def nextframe(frames):
    # brings a specific frame to the front 
    frames.tkraise()    

# funtion to play an audio to laugh
def laugh():
    # loads the mp 3 audio file
    pygame.mixer.music.load("Assessment 1 - Skills Portfolio/Exercise 2/laugh.mp3")
    # plays it (when the button is pressed)
    pygame.mixer.music.play()

# funtion to play an audio to boo
def boo():
     # loads the mp 3 audio file
    pygame.mixer.music.load("Assessment 1 - Skills Portfolio/Exercise 2/boo.mp3")
     # plays it (when the button is pressed)
    pygame.mixer.music.play()





# my frames
# menu frame
themenu = Frame(tkwindow)
# frame for jokes 
jokepage = Frame(tkwindow)

# placing the frames so they show
themenu.place(x=0, y=0, relwidth=1, relheight=1)
jokepage.place(x=0, y=0, relwidth=1, relheight=1)




# menu frame background
# the tkinter photoimage feature is stored in variable 'menubg'
menubg = PhotoImage(file="Assessment 1 - Skills Portfolio/Exercise 2/1-abcdbd12.png")
# use a label to display image and chose the intro frame
bg_label1 = Label(themenu, image=menubg)
# this is the placing of image (it take's up the whole window)
bg_label1.place(x=0, y=0, relwidth=1, relheight=1)

# jokes page frame background
# use a label to display image and chose the intro frame
bg_label2 = Label(jokepage, image=menubg)
# this is the placing of image (it take's up the whole window)
bg_label2.place(x=0, y=0, relwidth=1, relheight=1)





# my texts/labels/headings & for menu frame 
# menu frame heading, ornage background, comic sans MS font, size 20, placed on the left of screen
# asked ai with the pady because the button didn't want to sit right underneath the label
Label(themenu, text="Do you want to hear a joke?", bg="orange", font=("Comic Sans MS", 20)).pack(pady=(250, 10), padx=10, anchor=W)

# my buttons for menu frame
# yes button
# display joke function, next frame function
Button(themenu, text="Yes :D", width=25, height=2, bg="orange", font=("Comic Sans MS", 10), command=lambda: [display(), nextframe(jokepage)]).pack(padx=10, anchor=W)
# no button
# quits window fucntion
Button(themenu, text="NO >:(", width=25, height=2, bg="orange", font=("Comic Sans MS", 10), command=tkwindow.quit).pack(padx=10, anchor=W)






# my texts/labels/headings & for joke page frame
#label for jokes
# comic sans ms font, size 20, wraplength so it doesn't go off screen
jokelbl = Label(jokepage, text="", font=("Comic Sans MS", 20), wraplength=500, bg="orange")
# places the joke label 
jokelbl.pack(pady=1)


#my  buttons for joke page
# plays laughing sound effect
Button(jokepage, text="HAHA!",width=25, height=2,font=("Comic Sans MS", 10),bg="orange",  command=laugh).pack(pady=5)
# plays booing sound effect
Button(jokepage, text="BOO!",width=25, height=2,font=("Comic Sans MS", 10),bg="orange",  command=boo).pack(pady=5)
# calls display function and tells you another joke
Button(jokepage, text="Alexa, tell me another joke",width=25, height=2, font=("Comic Sans MS", 10),bg="orange",  command=display).pack(pady=10)
# takes you back to menu with next frame function
Button(jokepage, text="Menu", width=25, height=2, font=("Comic Sans MS", 10), bg="orange", command=lambda: nextframe(themenu)).pack(pady=10)
# quits the program
Button(jokepage, text="leave", width=25, height=2, font=("Comic Sans MS", 10), bg="orange", command=tkwindow.quit).pack(pady=10)






# displays the first frame (the menu)
nextframe(themenu)
tkwindow.mainloop()
