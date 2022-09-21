import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def button1():
    if entry_1.get() != '' and entry_2.get() != '' and entry_3.get() != '':
        cursor.execute('INSERT INTO tk_text (text1, text2, text3) VALUES ("{}", "{}", "{}")'.format(entry_1.get(), entry_2.get(), entry_3.get()))
        con.commit()
    else:
        messagebox.showwarning('Information', 'The line is empty.')

def button2():
    cursor.execute('SELECT * FROM tk_text')
    data = cursor.fetchall()

    if entry_4.get() != '' and entry_4.get().isdigit() != False and int(entry_4.get()) > 0 and int(entry_4.get()) <= len(data):
        label_3['text'] = '{} {} {}'.format((data[int(entry_4.get()) - 1])[1], (data[int(entry_4.get()) - 1])[2], (data[int(entry_4.get()) - 1])[3])
    else:
        messagebox.showwarning('Information', 'The line is empty\nor invalid input.')

def button3():
    cursor.execute('SELECT * FROM tk_text')
    data = cursor.fetchall()
    result = ''

    for i in range(len(data)):
        result += '{}. {} {} {}\n'.format((data[i])[0], (data[i])[1], (data[i])[2], (data[i])[3])
    result.rstrip()
    
    text_1.config(state=NORMAL)
    text_1.delete(1.0, tk.END)
    text_1.insert(tk.END, result)

con = mysql.connector.connect(host='localhost',
                                database='tk',
                                user='south',
                                password='21199')

cursor = con.cursor()

window = tk.Tk()
window.title('Database')
window.minsize(width=200, height=500)
window.maxsize(width=200, height=500)

frame_1 = tk.Frame(window)
frame_1.pack()

label_space = tk.Label(window, text='')
label_space.pack()

frame_2 = tk.Frame(window)
frame_2.pack()

label_space.pack()

frame_3 = tk.Frame(window)
frame_3.pack()


label_1 = tk.Label(frame_1, text='Add to database:')
label_1.pack()

entry_1 = tk.Entry(frame_1, bg='grey', fg='white')
entry_1.pack()

entry_2 = tk.Entry(frame_1, bg='grey', fg='white')
entry_2.pack()

entry_3 = tk.Entry(frame_1, bg='grey', fg='white')
entry_3.pack()

button_1 = tk.Button(frame_1, text='Add', width=10, height=1, command=button1)
button_1.pack()


label_2 = tk.Label(frame_2, text='Show by id:')
label_2.pack()

entry_4 = tk.Entry(frame_2, bg='grey', fg='white')
entry_4.pack()

button_2 = tk.Button(frame_2, text='Show', width=10, height=1, command=button2)
button_2.pack()

label_3 = tk.Label(frame_2, text='')
label_3.pack()


label_4 = tk.Label(frame_3, text='Show all:')
label_4.pack()

text_1 = tk.Text(frame_3, width=21, height=10, wrap='word')
scrollbar = Scrollbar(frame_3, orient=VERTICAL, command=text_1.yview)
scrollbar.pack(side='right', fill='y')
text_1.configure(yscrollcommand=scrollbar.set)
text_1.pack()

button_3 = tk.Button(frame_3, text='Show', width=10, height=1, command=button3)
button_3.pack()

window.mainloop()

cursor.close()
