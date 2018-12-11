# calling dns, serviceprofile, userdetails and manual login

import threading
import ManualLogin

from UserDetails import *
from ServiceProfile import *
from portScanner import port

from jabber_version_caveats import *
from systemDetails import *
from Devices import devices
# from JabberConfig import JabberConf
from jabber import jabber_
import ttk
import tkinter as tk
import Tkinter
from GetDns import dnsclass
from systemDetails import appinfo
from UI import RunnerUI
from ServiceProfile import service
from ImAndPresence import impclass
from ImpService import impservice
from sso import ssoclass
from ssoCallManager import ssoclass_
from JabberSummary import jabbercomp
from summary import summary
from PortScanner_jabber import port
from imp_sso import sso_impclass
from fqdn_or_ip import fqdnclass
from new_summary_1 import new_summaryclass
# from sequence_generator import seqclass
from allCerts import *
import time
import threading
from threading import Thread
import shutil


class Threads():
    def thread1(self, master):

        dnsobj = dnsclass()
        dnsobj.dns_fn()  # Running dns query and writing to file dns.txt

        userobj = system()
        ret = userobj.usersys()# Runnin(g userdetails and writing into userdetails.txt, getting the xml into userConfig
        # print("returned value", ret)
        # if ret == 1 :
        #     print ("returned 1 lol")
        #     tkMessageBox.showerror("INVALID","LOGIN FAILED")

        serviceobj = service()
        serviceobj.servicefn()  # Running serviceProfile and writing into service.txt

        sys = appinfo()
        sys.SysDetails()

        devicesobj = devices()
        devicesobj.devicesfn()

        # jabberObj = JabberConf()
        # jabberObj.jabberConf()

        jabberobj = jabber_()
        jabberobj.jabber()

        impobj = impclass()
        impobj.impfn()

        impserviceob = impservice()
        impserviceob.impservicefn()

        ssoobj = ssoclass_()
        ssoobj.ssofn()

        ssoclassObj = ssoclass()
        ssoclassObj.ssofn()

        ssoimpobj = sso_impclass()
        ssoimpobj.ssoimpfn()

        jabobj = jabbercomp()
        jabobj.jabbercompfn()

        portobj = port()
        portobj.portfn()

        summ = summary()
        summ.summaryfn()

        caveatsobj = caveatsclass()
        caveatsobj.caveatsfn()

        fqdnobj = fqdnclass()
        fqdnobj.fqdnfn()

        # seqobj = seqclass()
        # seqobj.seqfn()

        new_summaryobj = new_summaryclass()
        new_summaryobj.new_summaryfn()

        certobj = Certs()

        certobject.certImp()
        certobject.certVoice()
        certobject.certCucm()
        certobject.certdTrusted()

        shutil.make_archive("zip_file", 'zip', manualobj.browseValue)

        try:
            # t.frame.destroy()
            master.destroy()
        except:
            print ("failed")
        e1.set()

    def thread2(self, master):
        e1.wait(5)
        uiobj = RunnerUI()
        uiobj.MainApp()

    def task(self, master):
        master.title("Loading")
        master.geometry("250x100")
        try:
            master.wm_iconbitmap('img1.ico')
        except TclError:
            print ('No ico file found')
        t.frame = tk.Frame(master, width=100, height=100)
        t.frame.pack()
        label = tk.Label(t.frame, text="Please wait for a few minutes...", font="Helvetica 8 bold")
        label.grid(row=1, column=2, padx=10, pady=10)

        pr = ttk.Progressbar(t.frame, orient='horizontal', length=200, mode='indeterminate')
        # pr.pack(expand = True, fill = Tkinter.BOTH, side = Tkinter.TOP)
        pr.grid(row=3, column=2, padx=4, pady=10)
        pr.start(2)
        master.mainloop()


if __name__ == "__main__":
    t = Threads()
    e1 = threading.Event()

    master = tk.Tk()

    start = time.time()

    thread1 = Thread(target=t.thread1, args=(master,))
    thread1.start()
    t.task(master)
    # Thread1.join()
    Thread2 = Thread(target=t.thread2, args=(master,))
    Thread2.start()



