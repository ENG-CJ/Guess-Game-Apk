import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Image
import ImageTk
import pyttsx3
attempts=10
ans=random.randint(1,10)
def start():
    s = ttk.Style()
    s.configure("TProgressbar", foreground="red", background="red", thickness=40)
    progr = ttk.Progressbar(root, style="TProgressbar",  length=400, mode="determinate")
    progr.place(x=650, y=725)
    for i in range(1, 101, 1):
        progr['value'] = i
        root.update_idletasks()
        time.sleep(0.05)

    progr['value'] = 100
    root.destroy()
    window=Tk()
    window.state('zoomed')
    window.config(bg="blue")
    window.title("GUESS GAME")
    window.resizable(False,False)
    #_____________________________________
    frame=Frame(window,bg="white",bd=20,relief="groove",width=1270,height=700).place(x=150,y=80)
    Label(frame,text="GUESS GAME",bg="white",fg="red",font=("Verdana",60,"bold","underline")
          ).place(x=500,y=120)

    Label(frame, text="ENJOY UR LIFE", bg="white", fg="#003e53", font=("Verdana", 14, "bold")
          ).place(x=700, y=230)
    img2=Image.open("Images/welcome.png")
    res=img2.resize((300,200),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(res)
    Label(frame,image=new,bg="white").place(x=200,y=90)

    def check():

        global attempts
        attempts -= 1
        guess = int(entry.get())
        if ans == guess:
            text.set("You Win! Congrats")
            entry.delete(0,END)
            engine=pyttsx3.init()
            engine.say("HI USER CONGRATULATION YOU WIN!")
            engine.runAndWait()
            btn1.pack_forget()
            # attempts=0

        elif attempts == 0:
            engine = pyttsx3.init()
            engine.setProperty('rate',160)
            engine.say("HI USERRE OUT OF ATTEMPTS\n"
                       "THE WINDOW WILL DESTROYING GOOD BY!")
            engine.runAndWait()
            text.set("You Are Out Of Attempts")
            entry.delete(0,END)

            window.destroy()
            return root
        elif guess < ans:
            text.set("Incorrect! You Have  " + str(attempts) + "  Attempts Remaining!")
            entry.delete(0, END)

        elif guess > ans:
            text.set("Incorrect! You Have  " + str(attempts) + "  Attempts Remaining!")
            entry.delete(0, END)

        # return


    entry=Entry(window,bd=20,relief="groove",font=("Verdana",16,"bold"))
    entry.place(x=480,y=330,
                                                                               width=600,height=100)
    Label(frame,text="Guess The Number Between 1-50",bg="blue",fg="white",
          bd=5,relief="groove",font=("Verdana",15,"bold")).place(x=580,y=280)
    btn1=Button(frame,text="CHECK",bg="red",fg="white",
                bd=5,relief="groove",
                command=check,font=("Verdana",14,"bold")).place(x=600,y=500)

    def quit():
        ans = messagebox.askyesno("Confirm", "Are You Sure To Exit?")
        if ans == 1:
            window.destroy()
    btn2 = Button(frame, text="QUIT", command=quit,bg="#003e53", fg="white",
                  bd=5, relief="groove", font=("Verdana", 14, "bold")).place(x=720, y=500)
    btn3 = Button(frame, text="HOME", bg="black", fg="white",
                  bd=5, relief="groove", font=("Verdana", 14, "bold")).place(x=820, y=500)
    Label(frame,text="",bg="gray",width=175).place(x=170,y=600)
    Label(frame,text="GENERATOR GAME",bg="white",fg="red",font=("Verdana",16,"bold")
          ).place(x=670,y=630)

    Label(frame, text="POWERED BY- ENG-CJ", bg="white", fg="black", font=("Verdana", 14, "bold")
          ).place(x=670, y=659)
    Label(frame, text="", bg="blue", width=175).place(x=170, y=700)
    # img3=Image.open("Images/")
    # Manipulating Information From Tk Entry Box Agent Navigation GET the Way
    # Green Board For Gate way for half time
    text=StringVar()
    text.set("You Have 10 Attempts Remaining!")
    guess_attempt=Label(frame,textvariable=text,bg="white",fg="red",
                        font=("Verdana",16,"bold"))
    guess_attempt.place(x=540,y=440)
    mainloop()


# Window SetUp
root = Tk()
root.config(bg="#2c3539")

root.state('zoomed')
root.resizable(False, False)
root.title("Guess Game | Developed By ENG-CJ")
# _------------------------------------------------------------

# Frame
f1 = Frame(root, bd=10, bg="white", width=1290, height=700)
f1.place(x=130, y=90)
txt = Label(f1, text="GUESS-GAME", bg="white", fg="black", font=("Verdana", 50, "bold"))
txt.place(x=390, y=30)

Label(f1, text="DEVELOPED BY: ENG-CJ", bg="white", fg="red", font=("sans serif", 16, "bold")).place(x=490, y=100)
img = Image.open("Images/GUES.png")
res = img.resize((400, 800), Image.ANTIALIAS)
new = ImageTk.PhotoImage(res)
img1 = Label(f1, image=new, bg="white").place(x=1, y=100)

Label(f1, text="TIPS", bg="white", fg="blue", font=("Ms Comic Sans", 60, "underline")).place(x=540, y=170)
Label(f1, text="WAA GAME YAR OO GUESS AH"
               "WAXAA KUJIRO RANDOM NUMBERS"
               "\nWAXAAD QABSANYSAA HAL NUMBER "
               "NUMBER-KAAS AAD QABSATAY IYO\nGENERATOR-KA"
               "HADDAY ISKU MID NOQDAAN WAAD GUULAYSATAY\n"
               "HADDI KALANE WAAD KU GUULDARAYSATY GAME-KA\n\n"
               "WAXAA KU XERAN TIME HALKII DOORASHO WAA 1POINT"
               " \nHADDII AAD DOONAYSID INAAD CIYAARTO"
               "\nTAABO BUTTON-KA START SI AAD U BILLOWDO", bg="white", fg="red", font=("Verdana", 16, "bold")
      ).place(x=300, y=270)

Button(f1
       , text="Start", bg="blue", command=start,fg="white", bd=6, relief="sunken", font=("Verdana", 14, "bold")).place(
    x=600, y=500
)
l1=ttk.Label(root,background="white",foreground="black",font=("Verdana",16,"bold")).place(x=820,y=755)

Button(f1
       , text="EXIT", bg="red", fg="white", bd=6, relief="sunken", font=("Verdana", 14, "bold"),
       command=root.destroy).place(
    x=690, y=500
)


def helpy():
    messagebox.showinfo("Terminal | ENG-CJ", "FAQ MINIMISE THE WINDOW\nSEE THE TERMINAL")
    print('--------FAQ----------')
    print("HELLO USER WELCOME")
    print("SEND A MESSAGE : http://www.facebook.com/Abdulrahman_Haaji")
    print()
    print()

Button(f1
       , text="HELP", bg="black", fg="white", bd=6, relief="sunken", font=("Verdana", 14, "bold"),
       command=helpy).place(
    x=690, y=570
)



def inspact():
    messagebox.showinfo("Inspect |ENG-CJ", "CODE-KA WAXAA LAGUU SO QORAYAA\nTERMINAL HALKAS KA EEG")
    insp = open("inspect.txt", "r")
    op = insp.read()
    print(op)


Button(f1
       , text="Inspect", bg="magenta", fg="black", bd=6, relief="sunken", font=("Verdana", 14, "bold"),
       command=inspact).place(
    x=790, y=500
)

# Label(root,text="MENU BAR",bg="white",fg="black",font=("verdana",20,"bold"))
mainloop()
