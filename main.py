#Importing needed library
from tkinter import *
from math import *
from tkinter import messagebox

#Commonly used button parameters
commonbuttons = {'font': ("Times New Roman",11),'bg': '#B6B6B6','fg': 'white','width': 9, 'height': 4,
                 'activeforeground': 'white', 'activebackground' : '#B6B6B6'}
darkgraybuttons = {'font': ("Times New Roman",11),'bg': '#4F4F4F','fg': 'white','width': 9, 'height': 4,
                  'activeforeground': 'white', 'activebackground' : '#4F4F4F'}
orgbuttons = {'font': ("Times New Roman",11),'bg': '#EF993E','fg': 'white','width': 9, 'height': 4,
                  'activeforeground': 'white', 'activebackground': '#EF993E'}

#Variables used for normal/inverse calculations
ncon = 1
icon = 1

#Normal cos function
def ncos(num):
    return cos(num*ncon)

#Normal tan function
def ntan(num):
    return tan(num*ncon)

#Normal sin function
def nsin(num):
    return sin(num * ncon)

#Inverse cos function
def invcos(num):
    return acos(num) * icon

#Inverse tan function
def invtan(num):
    return atan(num) * icon

#Inverse sin function
def invsin(num):
    return asin(num) * icon

#Normal csc function
def ncsc(num):
    return(1/((sin(num*ncon))))

#Normal cot function
def ncot(num):
    return ((cos(num*ncon))/(sin(num * ncon)))

#Normal sec function
def nsec(num):
    return (1 / ((cos(num * ncon))))

#Inverse csc function
def icsc(num):
    return asin((1 / num)) * icon

#Inverse cot function
def icot(num):
    return atan((1 / num)) * icon

#Inverse sec function
def isec(num):
    return acos((1 / num)) * icon

#Initiate Calculator class
class Calc:
    def __init__(self,wind):

        #The text used for storing input
        self.eq_text = ""

        #Text Variable used for label
        self.eq_label = StringVar()

        #Label that displays information
        self.label = Label(wind, textvariable=self.eq_label, font=("Times New Roman", 35), bg='black', fg='white', pady=25)
        self.label.pack()

        #Applies func. to key pressed
        wind.bind("<Key>", self.numberkey)

        #Frame to keep buttons within
        frame = Frame()
        frame.pack()


####### ROW1 #######

        #Square root button
        self.btnsqrt = Button(frame,text='√\n( a )',**commonbuttons,command=lambda: self.press('sqrt('))
        self.btnsqrt.grid(row=0,column=1)

        #x^n button
        self.btnxupn = Button(frame,text='x^n\n( b )',**commonbuttons,command=lambda: self.press('**'))
        self.btnxupn.grid(row=0,column=2)

        #x^3 button
        self.btnxup3 = Button(frame,text='x^3\n( c )',**commonbuttons,command=lambda: self.press('**3'))
        self.btnxup3.grid(row=0,column=3)

        #Change to degree button
        self.btndeg = Button(frame,text='Deg\n( d )',**commonbuttons,command= self.con_deg)
        self.btndeg.grid(row=0,column=4)

        #Change to plus/minus button
        self.btnpm = Button(frame,text='+/-\n( e )',**commonbuttons, command=self.pm)
        self.btnpm.grid(row=0,column=5)

        #Left side bracket button
        self.btnbracleft = Button(frame,text='(',**commonbuttons,command=lambda: self.press('('))
        self.btnbracleft.grid(row=0,column=6)

        #Right side bracket button
        self.btnbracright = Button(frame,text=')',**commonbuttons,command=lambda: self.press(')'))
        self.btnbracright.grid(row=0,column=7)

        #Delete most recent character button
        self.btndelete = Button(frame,text='Delete\n(Backspace)',**commonbuttons,command=self.delete)
        self.btndelete.grid(row=0,column=8)

        #Clear label button
        self.btnclear = Button(frame,text='Clear\n(CTRL)',**commonbuttons,command= self.clear)
        self.btnclear.grid(row=0,column=9)

####### ROW2 #######

        #Cube root button
        self.btn3sqrt = Button(frame,text='3√x\n( f )',**commonbuttons,command=lambda: self.press('**(1/3)'))
        self.btn3sqrt.grid(row=1,column=1)

        #x^-1 button
        self.btnxupneg = Button(frame,text='x^-n\n( g )',**commonbuttons,command=lambda: self.press('**-'))
        self.btnxupneg.grid(row=1,column=2)

        #x^2 button
        self.btnxup2 = Button(frame,text='x^2\n( h )',**commonbuttons,command=lambda: self.press('**2'))
        self.btnxup2.grid(row=1,column=3)

        #Change to radians Button
        self.btnrad = Button(frame,text='Rad\n( i )',**commonbuttons,command= self.con_rad)
        self.btnrad.grid(row=1,column=4)

        #Pi button
        self.btnpi = Button(frame,text='π\n( j )',**commonbuttons,command=lambda: self.press('pi'))
        self.btnpi.grid(row=1,column=5)

        #Number 1 button
        self.btn1 = Button(frame,text=1,**darkgraybuttons,command=lambda: self.press(1))
        self.btn1.grid(row=1,column=6)

        #Number 2 button
        self.btn2 = Button(frame,text=2,**darkgraybuttons,command=lambda: self.press(2))
        self.btn2.grid(row=1,column=7)

        #Number 3 button
        self.btn3 = Button(frame,text=3,**darkgraybuttons,command=lambda: self.press(3))
        self.btn3.grid(row=1,column=8)

        #Multiplcation button
        self.btnmul = Button(frame,text='*',**orgbuttons,command=lambda: self.press('*'))
        self.btnmul.grid(row=1,column=9)

####### ROW3 #######

        #Cosecant button
        self.btncsc = Button(frame,text='Csc\n( k )',**commonbuttons,command=lambda: self.press('ncsc('))
        self.btncsc.grid(row=2,column=1)

        #Inverse cosecant button
        self.btnincsc = Button(frame,text='Csc^-1\n( l )',**commonbuttons,command=lambda: self.press('icsc('))
        self.btnincsc.grid(row=2,column=2)

        #Cosine button
        self.btncos = Button(frame,text='Cos\n( m )',**commonbuttons,command=lambda: self.press('ncos('))
        self.btncos.grid(row=2,column=3)

        #Inverse cosine button
        self.btnincos = Button(frame,text='Cos^-1\n( n )',**commonbuttons,command=lambda: self.press('invcos('))
        self.btnincos.grid(row=2,column=4)

        #Log button
        self.btnlog = Button(frame,text='log\n( o )',**commonbuttons,command=lambda: self.press('log('))
        self.btnlog.grid(row=2,column=5)

        #Number 4 button
        self.btn4 = Button(frame,text=4,**darkgraybuttons,command=lambda: self.press(4))
        self.btn4.grid(row=2,column=6)

        #Number 5 button
        self.btn5 = Button(frame,text=5,**darkgraybuttons,command=lambda: self.press(5))
        self.btn5.grid(row=2,column=7)

        #Number 6 button
        self.btn6 = Button(frame,text=6,**darkgraybuttons,command=lambda: self.press(6))
        self.btn6.grid(row=2,column=8)

        #Divison button
        self.btndiv = Button(frame,text='/',**orgbuttons,command=lambda: self.press('/'))
        self.btndiv.grid(row=2,column=9)

####### ROW4 #######

        #Cotangent button
        self.btncot = Button(frame,text='Cot\n( p )',**commonbuttons,command=lambda: self.press('ncot('))
        self.btncot.grid(row=3,column=1)

        #Inverse cotangent button
        self.btnincot = Button(frame,text='Cot^-1\n( q )',**commonbuttons,command=lambda: self.press('icot('))
        self.btnincot.grid(row=3,column=2)

        #Tangent button
        self.btntan = Button(frame,text='Tan\n( r )',**commonbuttons,command=lambda: self.press('ntan('))
        self.btntan.grid(row=3,column=3)

        #Inverse tangent button
        self.btnintan = Button(frame,text='Tan^-1\n( s )',**commonbuttons,command=lambda: self.press('invtan('))
        self.btnintan.grid(row=3,column=4)

        #Log10() button
        self.btnlog10 = Button(frame,text='log10\n( t )',**commonbuttons,command=lambda: self.press('log10('))
        self.btnlog10.grid(row=3,column=5)

        #Number 7 button
        self.btn7 = Button(frame,text=7,**darkgraybuttons,command=lambda: self.press(7))
        self.btn7.grid(row=3,column=6)

        #Number 8 button
        self.btn8 = Button(frame,text=8,**darkgraybuttons,command=lambda: self.press(8))
        self.btn8.grid(row=3,column=7)

        #Number 9 button
        self.btn9 = Button(frame,text=9,**darkgraybuttons,command=lambda: self.press(9))
        self.btn9.grid(row=3,column=8)

        #Addition button
        self.btnplus = Button(frame,text='+',**orgbuttons,command=lambda: self.press('+'))
        self.btnplus.grid(row=3,column=9)

####### ROW5 #######

        #Secant button
        self.btnsec = Button(frame,text='Sec\n( u )',**commonbuttons,command=lambda: self.press('nsec('))
        self.btnsec.grid(row=4,column=1)

        #Inverse secant button
        self.btninsec = Button(frame,text='Sec^-1\n( v )',**commonbuttons,command=lambda: self.press('isec('))
        self.btninsec.grid(row=4,column=2)

        #Sine button
        self.btnsin = Button(frame,text='Sin\n( w )',**commonbuttons,command=lambda: self.press('nsin('))
        self.btnsin.grid(row=4,column=3)

        #Inverse sin button
        self.btninsin = Button(frame,text='Sin^-1\n( x )',**commonbuttons,command=lambda: self.press('invsin('))
        self.btninsin.grid(row=4,column=4)

        #Inverse button
        self.btninv = Button(frame,text='inv\n( y )',**commonbuttons, command=lambda: self.press('log1p('))
        self.btninv.grid(row=4,column=5)

        #Number 0 button
        self.btn0 = Button(frame,text=0,**darkgraybuttons,command=lambda: self.press(0))
        self.btn0.grid(row=4,column=6)

        #Decimal button
        self.btndecimal = Button(frame,text='.',**darkgraybuttons,command=lambda: self.press('.'))
        self.btndecimal.grid(row=4,column=7)

        #Equals button
        self.btnequals = Button(frame,text='=',**orgbuttons,command=self.equals)
        self.btnequals.grid(row=4,column=8)

        #Subtraction button
        self.btnminus = Button(frame,text='-',**orgbuttons,command=lambda: self.press('-'))
        self.btnminus.grid(row=4,column=9)

    #Keyboard input
    def numberkey(self,event):
        txt = event.keysym
        if event.keysym.isdigit():
            self.eq_text = self.eq_text + event.keysym
            self.eq_label.set(self.eq_text)
        elif txt == "Return" or txt == "equal":
            self.equals()
        elif txt == "BackSpace":
            self.delete()
        elif txt == "plus":
            self.press('+')
        elif txt == "minus":
            self.press('-')
        elif txt == "slash":
            self.press('/')
        elif txt == "asterisk":
            self.press('*')
        elif txt == "parenleft":
            self.press('(')
        elif txt == "parenright":
            self.press(')')
        elif txt == "period":
            self.press('.')
        elif txt == "Control_R" or txt == "Control_L":
            self.clear()
        elif txt == "a":
            self.press('sqrt(')
        elif txt == "b":
            self.press('**')
        elif txt == "c":
            self.press('**3')
        elif txt == "d":
            self.con_deg()
        elif txt == "e":
            self.pm()
        elif txt == "f":
            self.press('**(1/3)')
        elif txt == "g":
            self.press('**-')
        elif txt == "h":
            self.press('**2')
        elif txt == "i":
            self.con_rad()
        elif txt == "j":
            self.press('pi')
        elif txt == "k":
            self.press('ncsc(')
        elif txt == "l":
            self.press('icsc(')
        elif txt == "m":
            self.press('ncos(')
        elif txt == "n":
            self.press('invcos(')
        elif txt == "o":
            self.press('log(')
        elif txt == "p":
            self.press('ncot(')
        elif txt == "q":
            self.press('icot(')
        elif txt == "r":
            self.press('ntan(')
        elif txt == "s":
            self.press('invtan(')
        elif txt == "t":
            self.press('log10(')
        elif txt == "u":
            self.press('nsec(')
        elif txt == "v":
            self.press('isec(')
        elif txt == "w":
            self.press('nsin(')
        elif txt == "x":
            self.press('invsin(')
        elif txt == "y":
            self.press('log1p(')



    #Function for equals button
    def equals(self):
        try:
            #Makes the current text variable into total variable and sets it to the label
            total = str(eval(self.eq_text))
            self.eq_label.set(total)
            self.eq_text = total
        #For different errors, sets the label as the error
        except SyntaxError:
            self.eq_text = "SyntaxError"
            self.eq_label.set(self.eq_text)
            self.eq_text = ""
        except ZeroDivisionError:
            self.eq_text = "ZeroDivisionError"
            self.eq_label.set(self.eq_text)
            self.eq_text = ""
        except ValueError:
            self.eq_text = "ValueError"
            self.eq_label.set(self.eq_text)
            self.eq_text = ""
        except NameError:
            self.eq_text = "NameError"
            self.eq_label.set(self.eq_text)
            self.eq_text = ""

    #Function for clear button
    def clear(self):
        self.eq_text = ""
        self.eq_label.set(self.eq_text)

    #Function for when button is pressed
    def press(self,num):
        self.eq_text = self.eq_text + str(num)
        self.eq_label.set(self.eq_text)

    #Function for delete button
    def delete(self):
        self.eq_text = self.eq_text[:-1]
        self.eq_label.set(self.eq_text)

    #Function for plus/minus button
    def pm(self):
        self.eq_text = self.eq_text + '-'
        self.eq_label.set(self.eq_text)

    #Function for converting to rad
    def con_rad(self):
        global ncon
        global icon
        ncon = 1
        icon = 1
        self.btnrad.config(foreground='#EF993E')
        self.btndeg.config(foreground='white')

    #Function for converting to deg
    def con_deg(self):
        global ncon
        global icon
        ncon = pi / 180
        icon = 180 / pi
        self.btnrad.config(foreground='white')
        self.btndeg.config(foreground='#EF993E')

#Initates the window and runs it
window = Tk()
run = Calc(window)
window.resizable(False, False)
window.config(background="black")
window.title("Calculator")
window.geometry("750x515")
messagebox.showinfo(title='Just a tip!',message='Dont forget to close brackets to avoid potential Syntax Error \nFeel Free to use the keybinds to use program with keyboard')

window.mainloop()