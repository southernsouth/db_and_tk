import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def button1():
    if e1.get() != '' and e2.get() != '' and e3.get() != '':
        cursor.execute('INSERT INTO tk_text (text1, text2, text3) VALUES ("{}", "{}", "{}")'.format(e1.get(), e2.get(), e3.get()))
        con.commit()
    else:
        messagebox.showwarning('Information', 'The line is empty.')

def button2():
    cursor.execute('SELECT * FROM tk_text')
    data = cursor.fetchall()

    if e4.get() != '' and e4.get().isdigit() != False and int(e4.get()) > 0 and int(e4.get()) <= len(data):
        l3['text'] = '{} {} {}'.format((data[int(e4.get()) - 1])[1], (data[int(e4.get()) - 1])[2], (data[int(e4.get()) - 1])[3])
    else:
        messagebox.showwarning('Information', 'The line is empty\nor invalid input.')

def button3():
    cursor.execute('SELECT * FROM tk_text')
    data = cursor.fetchall()
    x = ''

    for i in range(len(data)):
        x += '{}. {} {} {}\n'.format((data[i])[0], (data[i])[1], (data[i])[2], (data[i])[3])
    x.rstrip()
    
    t1.config(state=NORMAL)
    t1.delete(1.0, tk.END)
    t1.insert(tk.END, x)

con = mysql.connector.connect(host='localhost',
                                database='tk',
                                user='south',
                                password='21199')

cursor = con.cursor()

w = tk.Tk()
w.title('Database')
w.minsize(width=200, height=500)
w.maxsize(width=200, height=500)

f1 = tk.Frame(w)
f1.pack()

l_ = tk.Label(w, text='')
l_.pack()

f2 = tk.Frame(w)
f2.pack()

l_2 = tk.Label(w, text='')
l_2.pack()

f3 = tk.Frame(w)
f3.pack()


l1 = tk.Label(f1, text='Add to database:')
l1.pack()

e1 = tk.Entry(f1, bg='grey', fg='white')
e1.pack()

e2 = tk.Entry(f1, bg='grey', fg='white')
e2.pack()

e3 = tk.Entry(f1, bg='grey', fg='white')
e3.pack()

b1 = tk.Button(f1, text='Add', width=10, height=1, command=button1)
b1.pack()


l2 = tk.Label(f2, text='Show by id:')
l2.pack()

e4 = tk.Entry(f2, bg='grey', fg='white')
e4.pack()

b2 = tk.Button(f2, text='Show', width=10, height=1, command=button2)
b2.pack()

l3 = tk.Label(f2, text='')
l3.pack()


l4 = tk.Label(f3, text='Show all:')
l4.pack()

t1 = tk.Text(f3, width=21, height=10, wrap='word')
scrollbar = Scrollbar(f3, orient=VERTICAL, command=t1.yview)
scrollbar.pack(side='right', fill='y')
t1.configure(yscrollcommand=scrollbar.set)
t1.pack()

b3 = tk.Button(f3, text='Show', width=10, height=1, command=button3)
b3.pack()

w.mainloop()

cursor.close()
