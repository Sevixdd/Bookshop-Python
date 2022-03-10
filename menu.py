from tkinter import *
from tkinter import ttk
import tkinter.font as font
import booksearch
import bookcheckout
import bookreturn
import database
import bookweed

root = Tk()
root.title("Library")

#taking variables from database
book_title, bookID, info = database.func()

#switch frames function
def swap_frames(frame):
    frame.tkraise()

#font
my_font = font.Font(family='Helvetica', size=24, weight='bold')
my_font2 = font.Font(family='Helvetica', size=18, weight='bold')
my_font3 = font.Font(family='Helvetica', size=12, weight='bold')
my_font4 = font.Font(family='Helvetica', size=10, weight='bold')
#frames
menu_frame_left = Frame(root,bg='#23303d')
menu_frame_left.place(relx=0, relwidth=1, relheight=1)
search_frame = Frame(root,bg='#23303d')
search_frame.place(relwidth=1, relheight=1)
return_frame = bookreturn.bookreturn_func(root)
return_frame.place(relwidth=1, relheight=1)
bookweed_frame = bookweed.bookweed_func(root)
bookweed_frame.place(relwidth=1, relheight=1)
frames = [search_frame, bookweed_frame]

#Open search frame
search_B_menu = Button(menu_frame_left, text="Search for a book", bg='#163759', fg='white', font=my_font,  command=lambda: swap_frames(search_frame))
search_B_menu.place(relx=0.1, rely=0.1)
#Open return frame
return_B_menu = Button(menu_frame_left, text="Return a book", bg='#163759', fg='white', font=my_font, command=lambda: swap_frames(return_frame))
return_B_menu.place(relx=0.1, rely=0.2)
#Open bookweed frame
bookweed_B_menu = Button(menu_frame_left, text="Books Popularity", bg='#163759', fg='white', font=my_font, command=lambda: swap_frames(bookweed_frame))
bookweed_B_menu.place(relx=0.1, rely=0.3)

table=ttk.Treeview(menu_frame_left)
#Columns
table['columns']=("ISBN","Book Title","Author","Date","Availability")

#Formate columns
table.column("#0",width=50)
table.column("ISBN",width=160)
table.column("Book Title",width=120)
table.column("Author",width=120)
table.column("Date",width=120)
table.column("Availability",width=70)

#Create Headings
table.heading("#0",text="ID",anchor=W)
table.heading("ISBN",text="ISBN",anchor=W)
table.heading("Book Title",text="Book Title",anchor=W)
table.heading("Author",text="Author",anchor=W)
table.heading("Date",text="Date",anchor=W)
table.heading("Availability",text="Availability",anchor=W)

#Table Data
k=0
for i in info:
    split=i.split(" ")
    table.insert(parent='',index='end',iid=k,text=split[0],values=(split[1],split[2],split[3],split[4],split[5]))
    k+=1
#Refresh Table
def refresh_table():
    for i in table.get_children():
        table.delete(i)
    k=0
    for i in info:
        split = i.split(" ")
        table.insert(parent='', index='end',iid=k,text=split[0],values=(split[1], split[2], split[3], split[4], split[5]))
        k+= 1
table.pack(pady=20)
#Refresh Table button
update_table=Button(menu_frame_left,text="Refresh Table",bg='#163759', fg='white', font=my_font,command=refresh_table)
update_table.place(relx=0.4,rely=0.3)

#Search for book button
search = Entry(search_frame, width=50)
search.place(relx=0.5, rely=0.12, anchor=CENTER)
label_return_info = Label(search_frame, text='ID / ISBN / Book Title  / Author / Date / Availability',bg='#23303d', fg='white', font=my_font4)
label_return_info.pack(pady=20)
label_search = Label(search_frame, text='',bg='#23303d', fg='white', font=my_font3)
label_search.pack(pady=10)
search_B = Button(search_frame, text="Search",bg='#163759', fg='white', font=my_font, command=lambda: booksearch.get_text(search, label_search))
search_B.place(relx=0.5, rely=0.20, anchor=CENTER)

#Member ID check button
member_id_check = Entry(search_frame, width=40)
member_id_check.place(relx=0.5, rely=0.27, anchor=CENTER)
check_ID = Button(search_frame, text="Check Member ID",bg='#163759', fg='white', font=my_font,command=lambda: bookcheckout.bookcheckout(int(member_id_check.get()), label_ID))
check_ID.place(relx=0.5, rely=0.34, anchor=CENTER)
label_ID = Label(search_frame, text='',bg='#23303d', fg='white', font=my_font2)
label_ID.place(relx=0.5, rely=0.42, anchor=CENTER)

#Withdraw button
checkout = Button(search_frame, text="Withdraw",bg='#163759', fg='white', font=my_font, command=lambda: database.update_database(str(member_id_check.get()), book_title.index(search.get()) + 1, label_taken))
checkout.place(relx=0.5, rely=0.49, anchor=CENTER)
label_taken = Label(search_frame, text='',bg='#23303d', fg='white', font=my_font2)
label_taken.place(relx=0.5, rely=0.59, anchor=CENTER)

#Back button
for i in frames:
    back_B = Button(i, text="Back",bg='#163759', fg='white', command=lambda: swap_frames(menu_frame_left))
    back_B.place(relx=0.5, rely=0.8, anchor=CENTER)
    back_B['font'] = my_font

#Back button for return frame
back_button_return = Button(return_frame, text="Back",bg='#163759', fg='white',command=lambda: swap_frames(menu_frame_left))
back_button_return.place(relx=0.53, rely=0.8)
back_button_return['font'] = my_font

#Taking window values
width_canvas = root.winfo_screenwidth()
height_canvas = root.winfo_screenheight()
root.geometry("%dx%d" % (width_canvas, height_canvas))

#Quit button
quit = Button(menu_frame_left, text="Quit App",bg='#163759', fg='white', font=my_font, command=exit)
quit.place(relx=0.5, rely=0.7, anchor=CENTER)

menu_frame_left.tkraise()
root.mainloop()

