# update the variables in real time
def func():
    database = open("database.txt.txt", 'r+')
    book_title = []
    info = []
    bookID = []
    for i in database:
        split = i.split(" ")
        book_title.append(split[2])
        bookID.append(split[0])
        info.append(i)
    database.close()
    return book_title, bookID, info

# making the text in database as it was before
def back_to_normal(k):
    v = k[0]
    for i in k[1:]:
        v = v + " " + i
    v = v + "\n"
    return v

# search for book database, first parameter takes the memberID the second takes the ID of selected book and third is label
def update_database(taken, line, label_taken):
    book_title, bookID, info = func()
    database_write = open("database.txt.txt", "w")
    database = open("database.txt.txt", 'r+')
    logfile = open("log.txt.txt", "a")
    for i in info:
        split = i.split(" ")
        if split[0] == str(line):
            if split[5] == '0\n':
                split[5] = taken
                i = back_to_normal(split)
                label_taken.config(text="Book is ready to take")
                logfile.write(i)
            else:
                label_taken.config(text="Error,book it's taken")
        database_write.write(i)
    database_write.close()
    database.close()

# return the book database first parameter takes the ID of the book and the second is a label
def update_database_return(line,label):
    book_title, bookID, info = func()
    database_write = open("database.txt.txt", "w")
    database = open("database.txt.txt", 'r+')
    for i in info:
        split = i.split(" ")
        if split[0] == str(line):
            if split[5] != '0\n':
                split[5] = '0'
                i = back_to_normal(split)
                label.config(text="Book has been returned")
            else:
                label.config(text="Error, doesn't exist or already available")
        database_write.write(i)
    database_write.close()
    database.close()
