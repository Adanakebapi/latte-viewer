from tkinter import *
import tkinter.filedialog as filedialog
from PIL import ImageTk, Image
import glob

nd = ""
ndvalue = ""

def browse():
    global nd
    listbox.delete(0,END)
    file = filedialog.askopenfilename(filetypes=(("Latte File","*.latte"),("JPEG File","*.jpeg"),("PNG File","*.png"),("JPG File","*.jpg")))
    if not file:
        return
    directory = file.split("/")[:-1]
    nd = ""
    for i in directory:
        nd += i+"/"
    types = ("*.latte","*.jpeg","*.png","*.jpg")
    files = []
    for i in types:
        files.extend(glob.glob(nd+i))
    iPos = 0
    for i in files:
        files[iPos] = i.replace("\\","/")
        iPos += 1
    iPos = 0
    for i in files:
        if i == file:
            z = iPos
        iPos += 1
        listbox.insert("end",i.split("/")[-1])
    listbox.selection_set(z)
    listbox.event_generate("<<ListboxSelect>>")
    
def onselect(evt):
    global photoimg, vall, ndvalue
    w = evt.widget
    index = w.curselection()[0]
    value = w.get(index)
    entry.delete(0,END)
    entry.insert(0,nd+value)
    func()
    ndvalue = nd+value
    if value.split(".")[-1] == "latte":
        vall = True
        change2()
        ilb.configure(image="")
        with open(ndvalue,'r',encoding="utf-8") as f:
            data = f.read()
        textbox.config(state="normal")
        textbox.delete(1.0,END)
        if len(data) < 1000000:
            textbox.insert(END,data)
        else:
            textbox.insert(END,"The size is too big.\nIf you want to see the latte code,\nit can be crash the program.")
        textbox.config(state="disabled")
        img = latte2img2(nd+value)
        width, height = img.size
        if width/height == 29/22:
            nw = 290
            nh = 220
        elif width/height > 29/22:
            nw = 290
            nh = (290*height)/width
        else:
            nw = (220*width)/height
            nh = 220
        img = img.resize((int(nw),int(nh)), Image.ANTIALIAS)
        photoimg = ImageTk.PhotoImage(img)
        ilb.configure(image=photoimg)
    else:
        vall = False
        change1()
        tempimg = Image.open(nd+value)
        width, height = tempimg.size
        if width/height == 29/22:
            nw = 290
            nh = 220
        elif width/height > 29/22:
            nw = 290
            nh = (290*height)/width
        else:
            nw = (220*width)/height
            nh = 220
        tempimg = tempimg.resize((int(nw),int(nh)), Image.ANTIALIAS)
        photoimg = ImageTk.PhotoImage(tempimg)
        ilb.configure(image=photoimg)
        tempimg.close()
        latte = img2latte2(nd+value)
        textbox.config(state="normal")
        textbox.delete(1.0,END)
        if len(latte) < (1024**2):
            textbox.insert(END,latte)
        else:
            textbox.insert(END,"The size is too big.\nIf you want to see the latte code,\nit can be crash the program.")
        textbox.config(state="disabled")

def change1():
    lb1.place(x=50,y=230)
    lb2.place(x=350,y=230)
    lb1.config(fg="black")
    lb2.config(fg="black")
    ilb.place(x=50,y=250)
    textbox.place(x=350,y=250)
    button3.config(text="Save as Latte File")

def change2():
    lb1.place(x=350,y=230)
    lb2.place(x=50,y=230)
    lb1.config(fg="black")
    lb2.config(fg="black")
    ilb.place(x=350,y=250)
    textbox.place(x=50,y=250)
    button3.config(text="Save as Image File")

def pathButton():
    global nd
    x = entry.get()
    if (isFile(x)) and (x.split(".")[-1] in ["latte","jpeg","png","jpg"]):
        listbox.delete(0,END)
        directory = x.split("/")[:-1]
        nd = ""
        for i in directory:
            nd += i+"/"
        types = ("*.latte","*.jpeg","*.png","*.jpg")
        files = []
        for i in types:
            files.extend(glob.glob(nd+i))
        iPos = 0
        for i in files:
            files[iPos] = i.replace("\\","/")
            iPos += 1
        iPos = 0
        for i in files:
            if i == x:
                z = iPos
            iPos += 1
            listbox.insert("end",i.split("/")[-1])
        listbox.selection_set(z)
        listbox.event_generate("<<ListboxSelect>>")
    else:
        if nd != "":
            listbox.event_generate("<<ListboxSelect>>")
        else:
            entry.delete(0,END)

def isFile(x):
    t = x.split("/")[:-1]
    y = ""
    for i in t:
        y += i+"/"
    y += "*"
    for i in glob.glob(y):
        if i.replace("\\","/") == x:
            return True
    return False

def func():
    global is_packed
    if is_packed:
        return
    textbox.pack()
    textbox.config(state="disabled")
    button3.pack()
    button3.place(x=650,y=250)
    is_packed = True

def latte2img2(x):
    with open(x,'r',encoding="utf-8") as f:
        data = f.read()
    a = data.split(",")
    g = int(a[0])
    newX = ""
    for i in a[1:]:
        newX += i+","
    newX = newX[:-1]
    t1 = []
    t2 = (0,0,0)
    r = 1
    for i in newX:
        t2 = list(t2)
        t2[(r-1)%3] = ord(i)
        t2 = tuple(t2)
        if r % 3 == 0:
            t1 += [t2]
            t2 = (0,0,0)
        r += 1
    h = int(((r-1)/3)/g)
    img = Image.new("RGB", (g,h))
    img.putdata(t1)
    return img

def latte2img(x,y):
    with open(x,'r',encoding="utf-8") as f:
        data = f.read()
    a = data.split(",")
    g = int(a[0])
    newX = ""
    for i in a[1:]:
        newX += i+","
    newX = newX[:-1]
    t1 = []
    t2 = (0,0,0)
    r = 1
    for i in newX:
        t2 = list(t2)
        t2[(r-1)%3] = ord(i)
        t2 = tuple(t2)
        if r % 3 == 0:
            t1 += [t2]
            t2 = (0,0,0)
        r += 1
    h = int(((r-1)/3)/g)
    img = Image.new("RGB", (g,h))
    img.putdata(t1)
    img.save(y)
    img.close()

def img2latte2(x):
    img = Image.open(x)
    rgb_img = img.convert("RGB")
    w, h = img.size
    latte = f"{w},"
    for i in range(h):
        for j in range(w):
            tup = rgb_img.getpixel((j,i))
            latte += chr(tup[0])+chr(tup[1])+chr(tup[2])
    return latte

def img2latte(x,y):
    img = Image.open(x)
    rgb_img = img.convert("RGB")
    w, h = img.size
    latte = f"{w},"
    for i in range(h):
        for j in range(w):
            tup = rgb_img.getpixel((j,i))
            latte += chr(tup[0])+chr(tup[1])+chr(tup[2])
    with open(y,'w',encoding="utf-8") as f:
        f.write(latte)

def lattefunc(vall):
    global ndvalue
    if vall == True:
        f = filedialog.asksaveasfilename(defaultextension=".png")
        if f == None:
            return
        latte2img(ndvalue,f)
    else:
        f = filedialog.asksaveasfilename(defaultextension=".latte")
        if f == None:
            return
        img2latte(ndvalue,f)

root = Tk()
root.geometry("800x494")
root.title("Latte Viewer")
root.resizable(0,0)
root.wm_iconbitmap("icon.ico")

frame = Frame(root)
frame.pack()
frame.place(x = 6, y = 9)

listbox = Listbox(frame, height=13, width=25, selectmode = SINGLE, exportselection = 0)
scrollbar = Scrollbar(frame, command = listbox.yview, orient="vertical")
listbox.pack(side="left")
listbox.bind("<<ListboxSelect>>",onselect)

scrollbar.pack(side="right",fill="y")
listbox.configure(yscrollcommand=scrollbar.set)

button = Button(root,text="Browse",command=browse)
button.pack()
button.place(x = 190, y = 47)

entry = Entry(root,font=("Arial",12),width = 60)
entry.pack()
entry.place(x = 190, y = 18)

button2 = Button(root,text=" • ",font=("Arial",7),command=pathButton)
button2.pack()
button2.place(x = 735, y = 18)

lb1 = Label(root,text="Image File",fg="SystemButtonFace",font=("Arial",10,"bold"))
lb1.pack()
lb1.place(x=50,y=230)

lb2 = Label(root,text="Latte File",fg="SystemButtonFace",font=("Arial",10,"bold"))
lb2.pack()
lb2.place(x=350,y=230)

ilb = Label(root,text="")
ilb.pack()
ilb.place(x=50,y=250)

is_packed = False
textbox = Text(root,height=13,width=36)

vall = False
button3 = Button(root,text="Save as Latte File",font=("Arial",8),command=(lambda: lattefunc(vall)))

root.mainloop()
