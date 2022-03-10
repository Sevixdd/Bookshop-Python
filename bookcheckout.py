from tkinter import *

# Check member ID first parameter is the member id from Entry and the second is taking a label
def bookcheckout(memberID,label_id):
    if int(memberID) <9999 or int(memberID) >1000:
        label_id.config(text="Valid Member")
    else:
        label_id.config(text="Error,Not Member")

