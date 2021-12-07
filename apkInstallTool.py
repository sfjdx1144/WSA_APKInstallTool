import tkinter
from tkinter import *
import os
import ctypes
from tkinter import ttk
from tkinter.messagebox import showinfo
import windnd
from tkinter import filedialog
import time
from win32.win32api import GetSystemMetrics
import subprocess

st=subprocess.STARTUPINFO()
st.dwFlags=subprocess.STARTF_USESHOWWINDOW
st.wShowWindow=subprocess.SW_HIDE


workplace=os.path.dirname(os.path.abspath(__file__))
config=eval(open('./config.json','r',encoding='utf-8').read())
port=config['port']



global apk_file
apk_file=''

global connectFlag
connectFlag=False
def connect_adb():
    url='127.0.0.1:'+port
    cmd=workplace+'/adb.exe connect "'+ url+'"'
    result = subprocess.Popen(cmd,stdout=subprocess.PIPE,startupinfo=st)
    res = result.stdout.readline().decode('utf-8')
    r=''
    for line in res.splitlines():
        r+=line+'\n'
    if 'already connected to' in r:
        global connectFlag
        connectFlag=True
connect_adb()


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return str(round(fsize,2))
def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)



root = tkinter.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/72)

root.title('apkInstallTool')
root.iconbitmap('icon.ico')
T1 = Text(root,relief='solid',bd=1, font=('Arial', 10))
T1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.72)

if connectFlag:
    T1.insert(1.0,'The APK file can be dragged here.')
else:
    T1.insert(1.0,'Connecting adb failed, please check whether WSA is running, and restart the app.')
T1.config(state=DISABLED)


screen_width=GetSystemMetrics(0)
screen_height=GetSystemMetrics(1)

form_width=int(screen_width/4)
form_height=int(screen_height/4)
root.config(bg='white')
root.geometry('%dx%d+%d+%d' % (form_width, form_height, (screen_width-form_width)/2,(0.95*screen_height-form_height)/2))

s = ttk.Style()
s.configure('TButton', font=('Arial', 10),activebackground='black')

def draf_file(files):
    T1.config(state=NORMAL)
    T1.delete(1.0,tkinter.END)
    global apk_file
    apk_file=''
    file=files[0].decode()
    apk_file=file
    if 'apk' != file.split('.')[-1]:
        showinfo('Info','Please drag "Android application package(.apk)" file!')
    else:
        FileSize=get_FileSize(file)
        FileCreateTime=get_FileCreateTime(file)
        T1.insert(1.0,'File Path: '+file+'\n\nFile Size: '+FileSize+'Mb\n\nCreated Time: '+FileCreateTime)
    T1.config(state=DISABLED)


def get_file():
    global apk_file
    apk_file=''
    file = filedialog.askopenfilename(title=u'Choose File', filetypes=[('Android application package', '*.apk')])
    apk_file=file
    if file:
        T1.config(state=NORMAL)
        T1.delete(1.0,tkinter.END)
        FileSize=get_FileSize(file)
        FileCreateTime=get_FileCreateTime(file)
        T1.insert(1.0,'File Path: '+file+'\n\nFile Size: '+FileSize+'Mb\n\nCreated Time: '+FileCreateTime)
    T1.config(state=DISABLED)


def installapk():
    T1.config(state=NORMAL)
    global apk_file
    if apk_file:
        cmd=workplace+'/adb.exe install "'+ apk_file+'"'
        result = subprocess.Popen(cmd,stdout=subprocess.PIPE,startupinfo=st)
        res = result.stdout.readline().decode('utf-8')
        r=''
        for line in res.splitlines():
            r+=line+'\n'
        r+='\nCurrent File: '+ apk_file
        T1.delete(1.0,tkinter.END)
        T1.insert(1.0,r)
    else:
        showinfo('Info','No file selected!')
    T1.config(state=DISABLED)

def connect_adb_button():
    T1.config(state=NORMAL)
    url='127.0.0.1:'+port
    cmd=workplace+'/adb.exe connect "'+ url+'"'
    result = subprocess.Popen(cmd,stdout=subprocess.PIPE,startupinfo=st)
    res = result.stdout.readline().decode('utf-8')
    r=''
    for line in res.splitlines():
        r+=line+'\n'
    if 'already connected to' not in r:
        showinfo('Info','Connecting adb failed, please check whether WSA is running.')
    else:
        T1.delete(1.0,tkinter.END)
        showinfo('Info','Success!')
        T1.insert(1.0,'The APK file can be dragged here.')
    T1.config(state=DISABLED)


B0 = ttk.Button(root,text='Connect',command=connect_adb_button)
B0.place(relx=0.1,rely=0.82,relwidth=0.2,relheight=0.1)
B1 = ttk.Button(root,text='Open',command=get_file)
B1.place(relx=0.4,rely=0.82,relwidth=0.2,relheight=0.1)
B2 = ttk.Button(root,text='Install',command=installapk)
B2.place(relx=0.7,rely=0.82,relwidth=0.2,relheight=0.1)


windnd.hook_dropfiles(root,func=draf_file)


root.mainloop()
