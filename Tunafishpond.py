from tkinter import *
from tkinter import messagebox , filedialog , colorchooser, ttk
import threading
import time
import math

window = Tk()  #instantiate an instance of a window
window.geometry("700x700")
window.title("Tuna Fishpond")
icon = PhotoImage(file="TunaLogo.png")
window.iconphoto(True,icon)
window.config(background = "white")
fish_button_photo = PhotoImage(file="fishrod.png")
fishcount = 23333 #default when start the game
level = 1
prestigelevel = 11 #default 1
artifactnumber = 0
artifact_bonus = 1 #default 1 (x1.00)/ use function to determine


def configeverything():
    level_label.config(text=f"Your current level is {level}")
    fish_count_number.config(text=f"Current fish: {fishcount}")
    levelup_button.config(text=f"Level up! Cost:{levelupcost}")
    prestige_button.config(
        text= f"Prestige! \n(You will receive {prestige_count(level)} prestige level and {round(prestige_count(level) *5)} artifact)\n(You can only prestige above level 30)")
    prestige_label.config(text=f"Your prestige level is {prestigelevel - 1}")
    artifactnumberlabel.config(text= f"You have {artifactnumber} of artifact!")
    artifact1button.config(text=f"Level up! Cost: {round(artifact1level * 30 + artifact1level ** 1.15)}")
    artifactnumberlabel.config(text=f"You have {artifactnumber} artifact!")
    artifact1label.config(text=f"Better fish bait(Level:{artifact1level})")
    artifact2button.config(text=f"Level up! Cost:{round(artifact2level * 30 + artifact2level ** 1.15)}")
    artifact2label.config(text=f"Better fish rod(Level:{artifact2level})")
    statchecklabel.config(text=f"fish per click ={int((level + round(level * (prestigelevel - 1) * 1.34 / 100))*artifact_bonus)}\nArtifact bonus: {artifactbonusget()}")
def savefile():
    file = filedialog.asksaveasfile(defaultextension = ".txt",
                                    filetypes = [("Text file(.txt)",".txt")],
                                    initialdir = "E:\\pythonProject\\Projects4")
    if file is None:
        return
    else:
        messagebox.showinfo(title = "Success!", message = "Save successfully!")
    filetext = str(f"{fishcount**2}\n{level**2}\n{prestigelevel**2}\n{artifactnumber**2}\n{artifact1level**2}\n{artifact2level**2}")
    file.write(filetext)
    file.close()
def readsave():
    global fishcount,level,prestigelevel,artifactnumber,artifact1level,artifact2level
    filepath = filedialog.askopenfilename(defaultextension = ".txt",
                                          filetypes=[("Text file(.txt)", ".txt")],
                                      initialdir = "E:\\pythonProject\\Projects4")
    try:
        file = open(filepath,'r')
        filetext = file.readlines()
        fishcount = int(math.sqrt(int(filetext[0])))
        level = int(math.sqrt(int(filetext[1])))
        prestigelevel = int(math.sqrt(int(filetext[2])))
        artifactnumber = int(math.sqrt(int(filetext[3])))
        artifact1level = int(math.sqrt(int(filetext[4])))
        artifact2level = int(math.sqrt(int(filetext[5])))
        configeverything()
        if file is None:
            return
        else:
            messagebox.showinfo(title="Success!", message="Load save successfully!")
        file.close()
    except FileNotFoundError:
        return
        #print("File not found")

def windowsizesettingtab():
    windowsizesettingwindow = Toplevel()
    windowsizelistbox = Listbox(windowsizesettingwindow)
    windowsizelistbox.pack()
    windowsizelistbox.insert(1,"600x600")
    windowsizelistbox.insert(2,"700x700")
    windowsizelistbox.insert(3,"800x800")
    windowsizelistbox.config(height = windowsizelistbox.size())
    def submit_windowsize():
        windowsize = windowsizelistbox.get(windowsizelistbox.curselection())
        window.geometry(f"{windowsize}")
        windowsizesettingwindow.destroy()
    windowsize_submitbutton = Button(windowsizesettingwindow,text = "submit",command = submit_windowsize)
    windowsize_submitbutton.pack(side = BOTTOM)
def backgroundcolorsetting():
    backgroundcolor = colorchooser.askcolor()
    tab1.config(bg=f"{backgroundcolor[1]}")
    fish_count_number.config(bg=f"{backgroundcolor[1]}")
    level_label.config(bg=f"{backgroundcolor[1]}")
    prestige_label.config(bg=f"{backgroundcolor[1]}")
    prestige_button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    autolevelup_button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    levelup_button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    fish_button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    check_button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    submit_button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    entry.config(bg=f"{backgroundcolor[1]}")
    tab2.config(bg=f"{backgroundcolor[1]}")
    artifact1label.config(bg=f"{backgroundcolor[1]}")
    artifact2label.config(bg=f"{backgroundcolor[1]}")
    artifact1button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    artifact2button.config(bg=f"{backgroundcolor[1]}",activebackground = f"{backgroundcolor[1]}")
    artifactnumberlabel.config(bg=f"{backgroundcolor[1]}")


menubar = Menu(window)
window.config(menu = menubar)
fileMenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "File",menu = fileMenu)
fileMenu.add_command(label = "Load save",command = readsave)
fileMenu.add_command(label = "Save",command = savefile)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit",command = quit)
settingmenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Setting", menu = settingmenu)
settingmenu.add_command(label = "Window size",command = windowsizesettingtab)
settingmenu.add_command(label = "Background color",command = backgroundcolorsetting)

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1,text = "Game")
notebook.add(tab2, text = "Artifact")
notebook.add(tab3,text="Developer")
notebook.pack(expand = True,fill = "both")



def fish_click():
    global fishcount,level,prestigelevel,fishperclick,artifact_bonus
    artifact_bonus = artifactbonusget()
    fishperclick = int((level + round(level * (prestigelevel - 1) * 1.34 / 100))*artifact_bonus)
    fishcount += fishperclick
    #fishcount += level + round(level*(prestigelevel-1)*1.34/100)
    fish_count_number.config(text=f"Current fish: {fishcount}")
# fish_button = Button(window,text="Fish!",
#               font=("Aero",40),
#               fg = "black",
#               bg ="white",
#               relief=RAISED,
#               bd=10,
#               padx=10,
#               image=fish_button_photo,
#               compound="bottom",
#               command = fish_click)
# fish_button.pack(side=BOTTOM)
# fish_count_number = Label(window,text=f"Current fish: {fishcount}",
#                    font=("Comic Sans", 20))
# fish_count_number.pack()
# level_label = Label(window,text = f"Your current level is {level}")
# level_label.pack(side=TOP)
# prestige_label = Label(window,text = f"Your prestige level is {prestigelevel-1}")
# prestige_label.pack(side=TOP)
levelupcost = round((level **1.3) *3.5)
def levelup():
    global level,fishcount,levelupcost
    levelupcost = round((level **1.15) *3.5)
    if fishcount >=  levelupcost:
        level +=1
        fishcount -=  levelupcost
        configeverything()
#levelup_button = Button(window,text=f"Level up! Cost:{levelupcost}",command = levelup)
#levelup_button.pack(side=BOTTOM)
levelcalcount = 0
fishcalcount = 0
# if prestigelevel >= 10:
#     autolevelup_button.pack(side=BOTTOM)
def autolevelupcost():
    global fishcount,levelcalcount,fishcalcount
    while True:
        fishforcal = fishcount
        levelforcal = level
        levelupcostforcal = round((levelforcal ** 1.15) * 3.5)
        while fishforcal >= levelupcostforcal:
            levelupcostforcal = round((levelforcal ** 1.15) * 3.5)
            fishforcal -= levelupcostforcal
            levelforcal +=1
            levelcalcount +=1
            fishcalcount += levelupcostforcal
        autolevelup_button.config(text =f"Auto Level up! Use {fishcalcount} fish to level up {levelcalcount} times!")
        fishcalcount = 0
        levelcalcount = 0
        time.sleep(1)
def autolevelup():
    global level,fishcount,levelupcost
    levelupcost = round((level ** 1.15) * 3.5)
    while fishcount >= levelupcost:
        level += 1
        fishcount -=levelupcost
        levelupcost = round((level ** 1.15) * 3.5)
        configeverything()
        autolevelup_button.config(text =f"Auto Level up! Use {fishcalcount} fish to level up {levelcalcount} times!")
autolevelup_button = Button(tab1,text =f"Auto Level up! Use {fishcalcount} fish to level up {levelcalcount} times!",command = autolevelup)

autolevelupcostcal = threading.Thread(target = autolevelupcost, daemon= True)
if prestigelevel >= 10:
    autolevelupcostcal.start()

# entry = Entry(window,font=("Arial",20))
# entry.pack(side=LEFT)
# entry.insert(0,"Username")
def submit():
    username = entry.get()
    print(f"Hello {username}")
    messagebox.showinfo(title = "Welcome!", message =f"Hello! {username}")
    #entry.delete(0, END)
    entry.config(state=DISABLED)
# submit_button = Button(window,text = "submit", command = submit)
# submit_button.pack(side=RIGHT)
autofishingonoff = IntVar()
#def auto_fishing_func ():
    #if autofishingonoff.get() == 1 :
        #print("Auto Fishing On!")

def autofishingthread():  #autofishing that give fishclick *3 per second
    global fishcount,level,prestigelevel
    while True:
        while autofishingonoff.get() ==1:
            fishperclick = int((level + round(level * (prestigelevel - 1) * 1.34 / 100))*artifact_bonus)
            fishcount += fishperclick*3
            #fishcount += round((level + round(level*(prestigelevel-1)*1.34/100))*3)
            fish_count_number.config(text=f"Current fish: {fishcount}")
            time.sleep(1)
        else:
            pass



# check_button = Checkbutton(window,text="Auto Fishing on",
#                            variable = autofishingonoff,
#                            onvalue = 1,
#                            offvalue = 0)
autofishingthread = threading.Thread(target=autofishingthread,args=(),daemon=True)
if prestigelevel >= 8:
    #check_button.pack(side=BOTTOM)
    autofishingthread.start()
def prestige_count(level):
    prelvl = round(level ** 0.6) - 5 + round(level/33)
    if prelvl <= 0:
        return 0
    else:
        return prelvl

def prestige():
    global fishcount,level,prestigelevel,levelupcost,artifactnumber
    if level >= 30:
        prestigelevel += prestige_count(level)
        artifactnumber += round(prestige_count(level) *5)
        messagebox.showinfo(title="Success!", message=f"You gain {prestige_count(level)} prestige level and {round(prestige_count(level) *5)} of artifact!")
        fishcount = 30
        level = 1
        levelupcost = round((level ** 1.15) * 3.5)
        configeverything()
    elif level < 30:
        messagebox.showerror(title = "Can't prestige!", message = "You need at least level 30 to prestige!")
artifact1level = 0
artifact2level = 0


def artifact1levelup():
    global artifact1level,artifactnumber
    artifactlevelupcost = round(artifact1level *30 + artifact1level**1.15)
    if artifactnumber >= artifactlevelupcost:
        artifactnumber -= artifactlevelupcost
        artifact1level +=1
        artifact1button.config(text=f"Level up! Cost: {round(artifact1level *30 + artifact1level**1.15)}")
        artifactnumberlabel.config(text= f"You have {artifactnumber} artifact!")
        artifact1label.config(text= f"Better fish bait(Level:{artifact1level})")

def artifact2levelup():
    global artifact2level,artifactnumber
    artifactlevelupcost = round(artifact2level *30 + artifact2level**1.15)
    if artifactnumber >= artifactlevelupcost:
        artifactnumber -= artifactlevelupcost
        artifact2level +=1
        artifact2button.config(text=f"Level up! Cost:{round(artifact2level *30 + artifact2level**1.15)}")
        artifactnumberlabel.config(text=f"You have {artifactnumber} artifact!")
        artifact2label.config(text=f"Better fish rod(Level:{artifact2level})")

def artifactbonusget():
    global artifact_bonus,artifact1level,artifact2level
    artifact_bonus = 1 + artifact1level*0.05 + artifact2level*0.05
    return artifact_bonus


#prestige_button = Button(window,text= f"Prestige! \n(You will receive {prestige_count(level)} prestige level)\n(You can only prestige above level 30)",command=prestige)
#prestige_button.pack(side=BOTTOM)

#---pack everything(tab1)------------------------------------
fish_button = Button(tab1, text="Fish!",
                     font=("Aero", 40),
                     fg="black",
                     bg="white",
                     relief=RAISED,
                     bd=10,
                     padx=10,
                     image=fish_button_photo,
                     compound="bottom",
                     command=fish_click)
fish_button.pack(side=BOTTOM)
fish_count_number = Label(tab1,text=f"Current fish: {fishcount}",
                   font=("Comic Sans", 20))
fish_count_number.pack()
level_label = Label(tab1,text = f"Your current level is {level}")
level_label.pack(side=TOP)
prestige_label = Label(tab1,text = f"Your prestige level is {prestigelevel-1}")
prestige_label.pack(side=TOP)
submit_button = Button(tab1,text = "submit", command = submit)
submit_button.pack(side=RIGHT)
levelup_button = Button(tab1,text=f"Level up! Cost:{levelupcost}",command = levelup)
levelup_button.pack(side=BOTTOM)
#autolevelup_button = Button(tab1,text =f"Auto Level up! Use {fishcalcount} fish to level up {levelcalcount} times!",command = autolevelup)
if prestigelevel >= 10:
    autolevelup_button.pack(side=BOTTOM)

entry = Entry(tab1,font=("Arial",20))
entry.pack(side=LEFT)
entry.insert(0,"Username")
#autolevelup_button = Button(tab1,text =f"Auto Level up! Use {fishcalcount} fish to level up {levelcalcount} times!",command = autolevelup) #break the reset

check_button = Checkbutton(tab1,text="Auto Fishing on",
                           variable = autofishingonoff,
                           onvalue = 1,
                           offvalue = 0)
if prestigelevel >= 8:
    check_button.pack(side=BOTTOM)
prestige_button = Button(tab1,text= f"Prestige! \n(You will receive {prestige_count(level)} prestige level and {round(prestige_count(level) *5)} artifact)\n(You can only prestige above level 30)",command=prestige)
prestige_button.pack(side=BOTTOM)
#---pack everything(tab2)------------------------------------
artifactnumberlabel = Label(tab2,text= f"You have {artifactnumber} artifact!")
artifactnumberlabel.grid(row=0,column=0)
artifact1label = Label(tab2,text= f"Better fish bait(Level:{artifact1level})")
artifact1label.grid(row=1,column = 0)
artifact2label = Label(tab2,text= f"Better fish rod(Level:{artifact2level})")
artifact2label.grid(row=2,column = 0)
artifact1button = Button(tab2,text=f"Level up! Cost: {round(artifact1level *30 + artifact1level**1.15)}",command = artifact1levelup)
artifact1button.grid(row = 1,column = 1)
artifact2button = Button(tab2,text=f"Level up! Cost:{round(artifact2level *30 + artifact2level**1.15)}", command = artifact2levelup)
artifact2button.grid(row = 2,column = 1)
#---developer stuff-------------------------------------------
statchecklabel = Label(tab3,text=f"fish_per_click ={int((level + round(level * (prestigelevel - 1) * 1.34 / 100))*artifact_bonus)}")
statchecklabel.pack(side=TOP)
statchange = Entry(tab3)
statchange.pack()
def submitstatchange():
    statchangeentry = statchange.get()
    statchangeentry = int(statchangeentry)
    global level,prestigelevel,fishcount
    level = statchangeentry
    prestigelevel = statchangeentry
    fishcount = statchangeentry*100
    configeverything()
submitstatchangebutton= Button(tab3,text="submit",command = submitstatchange)
submitstatchangebutton.pack()
#---Start/Thread counter---------------------------------------------------
print(threading.active_count())
window.mainloop()  #place window on computer screen
