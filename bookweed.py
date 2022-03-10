import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
import database

# this function is making a bar chart embed in tkinter and is taking a frame as parameter
def bookweed_func(frame):
    # minimum variable assign for most unpopular book
    mini = 1000
    main = Frame(frame)
    logfile = open("log.txt.txt", "r")
    # dictionary for frequency list
    freq = {}
    labelFrame = Frame(main, bg='#23303d')
    labelFrame.place(relx=0.045, rely=0.02, relwidth=0.9, relheight=0.9)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    k=0
    # frequency list to fill the barchart with logfile data
    for i in logfile:
        split = i.split(" ")
        if split[2] in freq:
            freq[split[2]] += 1
        else:
            freq[split[2]] = 1
    for key, value in freq.items():
        ax.bar(key, value)
        if mini > value:
            mini = value
            k = key
    chart = FigureCanvasTkAgg(fig, labelFrame)
    chart.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(chart, labelFrame)
    toolbar.update()
    # Unpopular book label
    label_mini1 = Label(labelFrame, text="Most Unpopular Book Is: ", bg='black', fg='white', font=('Courier', 15))
    label_mini1.place(relx=0.35, rely=0.6)

    label_mini2 = Label(labelFrame, text=" Must be removed ", bg='black', fg='white', font=('Courier', 15))
    label_mini2.place(relx=0.55, rely=0.65)
    if k==0:
        label_mini1 = Label(labelFrame, text="No record available", bg='black', fg='white', font=('Courier', 15))
        label_mini1.place(relx=0.55, rely=0.6)
    else:
        label_mini1 = Label(labelFrame, text=k, bg='black', fg='white', font=('Courier', 15))
        label_mini1.place(relx=0.55, rely=0.6)
    return main
