from Tkinter import *
import ttk
import os
import shlex,subprocess
import sys
import base64

class mockLogin :

    def __init__(self,root=None):
        pass

    def event (self):
      username = self.userName.get()
      password = self.passWord.get()
      #password = base64.b64encode(bytes(password))
      l1 = [username,password]
      return l1

    def calling(self,root):
        self.event()
        root.quit()


    def gui(self) :
        root = Tk()
        root.title("Jabber Login")
        try:
            root.wm_iconbitmap('img1.ico')

        except TclError:
            print 'No ico file found'

        features_frame = Frame(root, width=150, height=50)
        features_frame.grid(row=0, column=0, sticky='N')
        self.userName = Entry(root)
        self.passWord = Entry(root, show="*")
        self.userName.grid(row=0, column=1,padx =50)
        self.passWord.grid(row=1, column=1,padx =50)
        # self.username = self.userName.get()
        # self.password = self.passWord.get()
        # self.password = base64.b64decode(bytes(self.password))
        # self.username = self.userName.get()
        # self.password = self.passWord.get()
        # self.password = base64.b64decode(bytes(self.password))
        # self.creds= [self.username, self.password]
        # print(self.username)
        Label(root, text="Username").grid(row=0)
        Label(root, text="Password").grid(row=1)


        #Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
        Button(root, text='Submit',command = root.quit).grid(row=5, column=1, sticky=W, pady=25)
        root.mainloop()

mockObj = mockLogin()
