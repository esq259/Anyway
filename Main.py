import os
import sys
import urllib.request
from xml.dom.minidom import *

from tkinter import *
from tkinter.ttk import *

mod = sys.modules[__name__]

#funcs

def pick(value):
    root.destroy()
    window1 = Tk()
    window1.title("First Step")
    window1.geometry("300x300+200+200")

    if value == 0:
        Go_Anyway()
    elif value == 1:
        Search()
    elif value == 2:
        Recommended()
    else:
        My_Way()

def Go_Anyway():
    print("Go Anyway~~!!")
    areaCode()

def Search():
    print()

def Recommended():
    print()

def My_Way():
    print()
        
def areaCode():
    SKey = 'TxLOsYQQr4DLcuTeyavErkFewwvx4p%2BL1HWchEkacOCyOD41DNIvhdtrNKxpKoHsB%2Bbtf9BEE48ktRRe9cuHvQ%3D%3D'
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?ServiceKey=' + SKey
    url += '&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=TestApp'

    req = urllib.request.Request(url)

    frame1 = Frame()
    frame1.pack(fill=X)
    title = Label(frame1, text="[ Anyway ]")
    title.pack(pady=20)
    frame2 = Frame()
    frame2.pack(fill=X)
    title = Label(frame2, text="[ Select Country ]")
    title.pack(pady=10)
    frame3 = Frame()
    frame3.pack(fill=X)
    
    try:
        resp = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        global Result
        response_body = resp.read()
        area = parseString(response_body.decode('utf-8'))
        List = area.getElementsByTagName('item')
        for aaa in range(10):
            name = List[aaa].getElementsByTagName('name')
            Result = name[0].firstChild.data
            RResult = str(aaa+1) + ".", Result
            xx = aaa+1
            setattr(mod, 'B_{}'.format(aaa), Button(frame3, text=RResult, width=20, command = lambda:country(xx)))


        B_0.grid(row=0, column=0, ipady=2)
        B_1.grid(row=0, column=1, ipady=2)
        B_2.grid(row=1, column=0, ipady=2)
        B_3.grid(row=1, column=1, ipady=2)
        B_4.grid(row=2, column=0, ipady=2)
        B_5.grid(row=2, column=1, ipady=2)
        B_6.grid(row=3, column=0, ipady=2)
        B_7.grid(row=3, column=1, ipady=2)
        B_8.grid(row=4, column=0, ipady=2)
        B_9.grid(row=4, column=1, ipady=2)

def country(self):
    if self == 0:
        print("Go Seoul!!")
        print(Result)
    else:
        print(self)

root = Tk()
root.title("Anyway ver.0.1.1")
root.geometry("300x300+200+200")

#title
frame1 = Frame()
frame1.pack(fill=X)
title = Label(frame1, text="[ Anyway ]")
title.pack(pady=20)

#menu
frame2 = Frame()
frame2.pack(fill=X, pady=10)
guide = Label(frame2, text="Welcome! Go Anyway")
guide.pack(side=LEFT, padx=24)
        
frame3 = Frame()
frame3.pack(pady=5)
b1 = Button(frame3, text="Go Anyway", width=12, command = lambda:pick(0))
b2 = Button(frame3, text="Search", width=12, command = lambda:pick(1))
b3 = Button(frame3, text="Recommended", width=12, command = lambda:pick(2))
b4 = Button(frame3, text="My Way", width=12, command = lambda:pick(3))

b1.grid(row=0, column=0, ipady=2)
b2.grid(row=0, column=1, ipady=2)
b3.grid(row=1, column=0, ipady=2)
b4.grid(row=1, column=1, ipady=2)

frame4 = Frame()
frame4.pack()
ver = Label(frame4, text="ver 0.1.3")
ver.pack()

root.mainloop()
