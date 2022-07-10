from tkinter import *
import functools,random,secrets

window=Tk()

window.configure(background='black')
window.title('Password Generator')

try:
    window.iconbitmap('logo.ico')
except:
    pass

window_width=1000
window_height=500

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=(screen_width/2)-(window_width/2)
y=(screen_height/2)-(window_height/2)

window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')


instructions='''Instructions:
- Give size of password through your keyboard
- Password size must be greater than or equal to 8
- Please enter only positive integers
'''


char_str='abcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()_+|{}<>?:/.,;[]\-=ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_list=['abcdefghijklmnopqrstuvwxyz','1234567890','ABCDEFGHIJKLMNOPQRSTUVWXYZ','`~!@#$%^&*()_+|{}<>?:/.,;[]\-=']

def click():
    size=str(entry_input.get())
    if size.isdigit()==True:
        new_size=int(size)
        if new_size>=8:
            password_list=[]
            for i in char_list:
                for j in range(2):
                    password_list.append(secrets.choice(i))
            for i in range(new_size-8):
                password_list.append(secrets.choice(char_str))
            random.shuffle(password_list)
            password=functools.reduce(lambda x,y:x+y,password_list)
            exit_input.delete(0,END)
            exit_input.insert(0,"Password: "+password)
        else:
            exit_input.delete(0,END)
            exit_input.insert(0,"Oops! Password can't be less than 8 characters")
    else:
        exit_input.delete(0,END)
        exit_input.insert(0,"Please enter an positive integer")


credit=Label(window,text='Designed by Naga Sriram',fg='white',bg='black')
instruct=Label(window,text=instructions,fg='white',bg='black')
enter=Label(window,text='Please enter the size of password in the given below box',fg='white',bg='black')

entry_input=Entry(window,width=60,borderwidth=10,fg='white',bg='black')
exit_input=Entry(window,width=60,borderwidth=10,fg='white',bg='black')

exit_input.insert(0,'Password: ')

button_generate=Button(window,text="Generate Password",fg='white',bg='green',padx=245,pady=10,command=click)


l=[credit,instruct,enter,entry_input,exit_input,button_generate]


for i in range(1,7):
    Grid.rowconfigure(window, index=i, weight=1)

Grid.columnconfigure(window, index=0, weight=1)


enter.grid(row=1,column=0,sticky='nsew')
credit.grid(row=6,column=0,sticky='nsew')
instruct.grid(row=5,column=0,sticky='nsew')

entry_input.grid(row=2,column=0,sticky='nsew')
exit_input.grid(row=4,column=0,sticky='nsew')

button_generate.grid(row=3,column=0,sticky='nsew')

def resize(e):
    wid=e.width
    button_newsize=int((16*wid)/(900))
    for i in l:
        i.config(font=('Arial',button_newsize))


window.bind('<Configure>',resize)
window.mainloop()
