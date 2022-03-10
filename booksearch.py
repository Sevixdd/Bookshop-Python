from tkinter import *
import database
# this funciton is getting books from database first parameter is taking a selected line from database and the second parameter is a label
def get_text(variable,label_search):
    book_title, bookID, info = database.func()
    if variable.get() in book_title:
        label_search.config(text=info[book_title.index(variable.get())])
    else:
        label_search.config(text="Cartea nu exista!")

