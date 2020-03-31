from tkinter import *
import tkinter.messagebox
import time
from random import randint

root=Tk();
root.title("HIT")

def help():
    tkinter.messagebox.showinfo("Help","Set Timer and Level from the Menu\nand Press Start to play.\n\nThen click on Hit Button\nas many times as you can to score.")

def me():
    tkinter.messagebox.showinfo("Credits","Made by : Harsh Chaudhary") 

#default values
speed=800
speed1="Easy"
times=10
t=times

#update functions
def update(a,n):
    global speed
    global speed1
    global times
    speed=a
    speed1=n
    level_head()

def update_1(a):
    global times
    times=a
    t=times
    time_head(times,450)

#menu bar
menubar=Menu(root)
root.config(menu=menubar)
lmenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="Levels",menu=lmenu)
lmenu.add_command(label="Easy",command=lambda:update(800,"Easy     "))
lmenu.add_command(label="Medium",command=lambda:update(600,"Medium"))
lmenu.add_command(label="Hard",command=lambda:update(400,"Hard     "))


tmenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="Timer",menu=tmenu)
tmenu.add_command(label="10",command=lambda:update_1(10))
tmenu.add_command(label="15",command=lambda:update_1(15))
tmenu.add_command(label="20",command=lambda:update_1(20))

menubar.add_command(label="Credits",command=me)
menubar.add_command(label="Help",command=help)


#window frames
frame = Frame(root,height="420",width="630",bg="#393640")
frame.pack(side="bottom")

frame1=Frame(root,height="50",width="630",bg="#0E484F")
frame1.pack(side="top")

frame2=Frame(frame,height="420",width="15",bg="#0E484F")
frame2.place(x=0,y=0)

frame3=Frame(frame,height="420",width="15",bg="#0E484F")
frame3.place(x=615,y=0)

frame3=Frame(frame,height="20",width="630",bg="#0E484F")
frame3.place(x=0,y=400)

#head frame display functions
def time_head(tp,xpos):
    if(tp<10):
         st="0"+str(tp)
    else:
        st=str(tp)

    if(xpos==450):
        label1=Label(frame1,text="Time: "+st+" sec",bg="#0E484F",font = "Verdana 10 bold",fg="white")
    else:
        label1=Label(frame1,text="Time: "+st+" sec",bg="#0E484F",font = "Verdana 12",fg="white")
        
    label1.place(x=xpos,y=10)

def level_head():
    global speed1
    label=Label(frame1,text="Level: "+speed1,bg="#0E484F",font = "Verdana 10 bold",fg="white")
    label.place(x=100,y=10)


#called when the user hits the ball
def hit():
    global count
    
    if(c==0):
        invisible(100,10,15,10)
        invisible(280,10,15,10)
        invisible(450,10,15,10)

    hits=str(count)
    label=Label(frame1,text="Hits: "+hits,bg="#0E484F",font="Verdana 13",fg="white")
    label.place(x=150,y=8)

#initialization of variables  
c=0
count=0
x=0
y=0
level_head()
time_head(t,450)

#called when start button in clicked
def start():
    global c
    global count
    global times
    global t

    hit()
    menubar.entryconfig("Levels",state="disabled")
    menubar.entryconfig("Timer",state="disabled")
    
    c=1
    count=0
    t=times
    ball()
    timer()

#start button function   
def start_button():
    s_button=Button(frame1,text="Start",bg="#0E484F",font = "Verdana 12 bold",fg="white",bd=0,relief=RAISED,command=start)
    s_button.place(x=280,y=10)

   
start_button()
bcanvas= Canvas(frame,width=80,height=80,bg="#393640",highlightthickness=0)
path=PhotoImage(file="blue.png")
path1=PhotoImage(file="blue1.png")

#function to count number of hits
def counter(event):
    global count
    global path1
    global x
    global y
    if(c==1):
        count=count+1
        img1=bcanvas.create_image(40,40,image=path1)
        bcanvas.place(x=x,y=y)
        #bcanvas.unbind("<Button-1>")
        hit()
        
#function to check when the play time is over and reversing variables to original values
def check():
    global t
    global c
    global count
    global times
    if(c==1 and t==0):
            c=0
	    #updation of high score
            high=open("hs.txt","a")
            high=open("hs.txt","r")
            h=high.read()
            if(h==""):
                high=open("hs.txt","w")
                high.write("0")
                h="0"

            hs=int(h)
            if(count>hs):
                high=open("hs.txt","w")
                high.write(str(count))
                h=str(count)
            st=str(count)
            tkinter.messagebox.showinfo("Score","High Score: "+h+"\n\nYour score is "+st)
            count=0
            invisible(150,8,15,10)
            invisible(400,10,20,10)
            level_head()
            time_head(times,450)
            menubar.entryconfig("Levels",state="active")
            menubar.entryconfig("Timer",state="active")

            
#places the ball at any random position            
def place():
    global path
    global x
    global y
    x=randint(80,500)
    y=randint(80,300)
    img=bcanvas.create_image(40,40,image=path)
    bcanvas.place(x=x,y=y)
    bcanvas.bind("<Button-1>",counter)

#driver function to place ball after some delay    
def ball():
    global speed
    global c
    if(c==1):
        place()
        root.after(speed,ball)

#driver function to check function
def timer():
    global t
    global c
    if(c==1):
        time_head(t,400)
        check()
        if(t==0):
            start_button()
        else:
            t=t-1
            root.after(1000,timer)

#hides the unwanted labels 
def invisible(x,y,w,h):
    l=Label(frame1,bg="#0E484F",width=w,height=h)
    l.place(x=x,y=y)
    

root.resizable(width=False, height =False)
root.mainloop()
