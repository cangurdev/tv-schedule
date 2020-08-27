from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import datetime
from tkinter import *
from tkinter.ttk import Combobox, Scrollbar


window = Tk()
window.title("Tv Schedule")
window.geometry('640x640')
window.resizable(False, False)


def getChannels():
    return ['Show Tv', 'Star Tv', 'Kanal D', 'Fox', 'Trt 1', 'Atv', 'Tv 8', 'CNN Türk', 'Habertürk']


combo = Combobox(window, state="readonly", values=getChannels(), width=10)
combo.current(0)
combo.place(x=240, y=40)
scroll = Scrollbar(window)
scroll.pack(side=RIGHT, fill=Y)
text = Text(window, yscrollcommand=scroll.set)
text.place(x=140, y=90)
text.configure(width=45, height=30)
scroll.config(command=text.yview)


def show_info():
    text.delete('1.0', END)
    text.insert(END, "Schedule for {} at {}\n\n".format(
        combo.get(), datetime.date.today()))
    text.insert(END, "-"*45+"\n")
    for i in getStream(combo.get()):

        text.insert(END, i[0]+"\t"+i[1]+"\n")
        text.insert(END, "-"*45+"\n")


def getStream(channel):

    if channel == "Star Tv":
        channel = "90/2/star-tv/"
    elif channel == "Kanal D":
        channel = "94/0/kanal-d/"
    elif channel == "Fox":
        channel = "87/7/fox/"
    elif channel == "Trt 1":
        channel = "15/5/trt-1/"
    elif channel == "Tv 8":
        channel = "24/8/tv8/"
    elif channel == "Atv":
        channel = "83/4/atv/"
    elif channel == "Show Tv":
        channel = "92/3/show-tv/"
    elif channel == "CNN Türk":
        channel = "20/1/cnn-turk/"
    elif channel == "Habertürk":
        channel = "22/14/haberturk/"

    pasteURL = "https://www.hurriyet.com.tr/tv-rehberi/yayin-akisi/"+channel
    data = urlopen(Request(pasteURL, headers={
                   'User-Agent': 'Mozilla'})).read()
    parse = BeautifulSoup(data, 'html.parser')
    items = parse.find_all('div', "flow-card-content")

    ch = []
    for x in items:
        ch.append([x.contents[1].text,x.contents[3].text])
    return ch

show_info_btn = Button(window, text="Search", command=show_info)
show_info_btn.place(x=330, y=39)
window.mainloop()
