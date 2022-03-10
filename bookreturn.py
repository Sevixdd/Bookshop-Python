from tkinter import *
import tkinter.font as font
import database

# this function is taking a frame as parameter and it's used for returning books
def bookreturn_func(frame):
    my_font = font.Font(family='Helvetica', size=24, weight='bold')
    main = Frame(frame)
    #yellow bg
    heading_frame1 = Frame(main, bg="#FFBB00", bd=5)
    heading_frame1.place(relwidth=1, relheight=1)
    #black bg
    labelFrame = Frame(main, bg='#23303d')
    labelFrame.place(relx=0.045, rely=0.02, relwidth=0.9, relheight=0.9)
    #Title
    headingLabel = Label(labelFrame, text="Return Book", bg='#23303d', fg='white', font=my_font)
    headingLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    # Book ID to Return Book
    lb1 = Label(labelFrame, text="Book ID : ", bg='#23303d', fg='white', font=('Courier', 15))
    lb1.place(relx=0.33, rely=0.287)

    #Book is returned/Error label
    label2 = Label(labelFrame, text='', bg='#23303d', fg='white', font=('Courier', 15))
    label2.place(relx=0.33, rely=0.6)

    bookID = Entry(labelFrame)
    bookID.place(relx=0.5, rely=0.3, relwidth=0.2, anchor=CENTER)

    # Submit Button
    submit_b = Button(main, text="Return", bg='#163759', fg='white',command=lambda: database.update_database_return(bookID.get(),label2))
    submit_b.place(relx=0.41, rely=0.8)
    submit_b['font'] = my_font

    return main
