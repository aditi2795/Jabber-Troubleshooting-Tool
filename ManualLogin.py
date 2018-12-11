from Tkinter import *
from tkinter.filedialog import  askdirectory
import base64
import requests
import tkMessageBox

class manualclass():
    global flag

    flag=0


    def manual(self) :
        root = Tk()
        root.title("ttk.Notebook")
        root.title("Jabber Validation Report")
        root.geometry("900x500")
        try:
            root.wm_iconbitmap('img1.ico')

        except TclError:
            print ('No ico file found')

        browseValue=''
        manualobj.browseValue=''


        def choose():
            if entry_browse.get() == "":
                tkMessageBox.showerror("FIELD CANNOT BE EMPTY", "PLEASE CHOOSE A FOLDER")
                return

            if entry_username.get() == "" or entry_password.get() == "" :
                tkMessageBox.showerror("LOGIN FAILED","CREDENTIALS CAN NOT BE EMPTY")
                return
            filecred = open(manualobj.browseValue+"/credentials.txt","w")
            print ("browse", entry_browse.get())

            if flag == 1:
                if entry.get() == "" :
                    tkMessageBox.showerror("FAILED","FIELD CAN NOT BE EMPTY")
                    return

            if flag == 2:
                if entryimp.get() =="":
                    tkMessageBox.showerror("FAILED","PLEASE ENTER FIELD")
                    return



            ########################### checking for valid credentials #########################


            filecred.write("Username:"+entry_username.get()+"\n"+"Password:"+base64.b64encode(entry_password.get())+"\n")

            if flag==1:
                manualobj.impflag = 0


                manualobj.flag=1
                manualobj.server=str(entry.get())

                print manualobj.server
                root.destroy()
            elif flag==2:
                manualobj.server_imp=str(entryimp.get())
                manualobj.flag=2
                print manualobj.server_imp
                manualobj.impflag = 1
                root.destroy()
            else:
                manualobj.impflag = 0
                manualobj.flag=0
                root.destroy()

        def manual_login():
            global flag
            flag=1
            entry.config(state="normal")
            entryimp.config(state="disabled")


        def auto_login():
            global flag
            flag=0
            entryimp.config(state="disabled")
            entry.config(state="disabled")


        def manual_imp_login():
            global flag
            flag=2
            manualobj.impflag=1
            entryimp.config(state="normal")
            entry.config(state="disabled")

        def browse() :
            global browseValue
            browseValue = askdirectory()
            print(browseValue)
            #global manualobj.browseValue
            manualobj.browseValue= str(browseValue)
            entry_browse.insert(0, manualobj.browseValue)
            #pass
        # def event():

    # def sub ():
    #     choose()
    #     fo = open("C:/Python27/aditi.txt","w+")
    #     x = event()
    #     fo.write(x)
        label_account = Label(root, text="Select your account type", font="Helvetica 14")
        label_account.grid(row=0, column=0, padx=10, pady=20, sticky='W')

        var=IntVar()
        auto = Radiobutton(root, text="Automatic CUCM(Recommended)",variable=var, font = "Helvetica 10",value = 0,command=auto_login)
        auto.grid(row = 1, column =0, padx = 10,sticky = 'W')
        manual_cucm = Radiobutton(root, text="Manual Entry CUCM",variable=var, font = "Helvetica 10",value = 1,command=manual_login)
        manual_cucm.grid(row= 2, column =0 , padx = 10, pady  = 0,sticky = 'W')

        manual_imp = Radiobutton(root, text="Manual IMP",variable=var,font="Helvetica 10 ", value=3,
                               command=manual_imp_login)
        manual_imp.grid(row=4, column=0, padx=10, pady=0, sticky='W')

        label_ = Label(root,text = "Choose the destination folder", font = "Helvetica 10 ")
        label_.grid(row = 1,column = 4, padx = 100, pady = 20)

        label_username = Label(root,text ="Username", font = "Helvetica 10 ")
        label_username.grid(row = 2, column = 4)

        label_password = Label(root,text="Password", font = "Helvetica 10 ")
        label_password.grid(row = 3, column = 4 )

        entry_browse = Entry(root,bd = 2)
        entry_browse.grid(row=1, column = 5, padx = 1, pady= 20)

        entry_username = Entry(root,bd=2)
        entry_username.grid(row=2, column = 5)

        entry_password = Entry(root,bd= 2,show ="*")
        entry_password.grid(row = 3, column = 5,pady = 20)


        # entry_user = Entry(root,bd = 2)
        # entry_user.grid(row = 3, column = 5, padx = 1, pady = 30)

        button_ = Button(root,text = "Browse" ,font = "Helvetica 10",command=browse)
        button_.grid(row=1, column =6, padx = 50, pady = 20)

        label_server = Label(root, text = "Login Server", font = "Helvetica 14 ")
        label_server.grid(row = 5, column = 0, padx = 0, pady = 50,sticky ='W')

        label_serv = Label(root, text = " CUCM Server Address", font = "Helvetica 10")
        label_serv.grid(row = 6,column = 0)
        label_imp=Label(root,text="IMP SERVER",font ="Helvetica 10").grid(row=9,column=0)

        button = Button(root, text="Submit", font="Helvetica 10",command=choose)
        button.grid(row=7, column=6)
        entry = Entry(root, bd=2,state="disabled")
        entry.grid(row=7, column=0, pady=0)

        entryimp=Entry(root,bd=2,state='disabled')

        entryimp.grid(row=10,column=0,pady=0)



        root.mainloop()

manualobj=manualclass()
manualobj.manual()
#mockObj.gui()
