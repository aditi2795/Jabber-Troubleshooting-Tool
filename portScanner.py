
import socket
import subprocess
import sys
import multiprocessing
from threading import Thread
import time
import re

import tkinter
import ttk
import threading
from multiprocessing import Process
from UI import *
#from ServiceProfile import *

start = time.time()


class port():
    def cucm(self):
      file_port = open("C:/Python27/port_scanner.txt", 'a+')
      fileportsummary=open("")
      #ports_ = open("C:/Python27/ports_.txt","w+")
      try:
          file = open("c:/Python27/service.txt", 'r').read()
          info = file.split('\n')
          cucm_port = [6970, 6972, 3804, 8443, 2748, 5060, 5061]
          item = re.findall(r'CTI:(.*?)\n',file,re.I |re.M)
          #print("88",item[2])
          for line in item :
              cucm_ = line.split(':')
              if cucm_[1] != "Not Configured":
                  cti = socket.gethostbyname(cucm_[1])
                  #print("hi",cucm_[1])
                  for ports in cucm_port:
                      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                      result = sock.connect_ex((cti, ports))
                      print("\ncucm Server: "+str(cti)+" Ports:"+str(ports)+"\n")
                      print result
                      if result == 0:
                          file_port.write("CUCM:"+cti+":"+str(ports)+":Open\n")
                      else:
                          file_port.write("CUCM:"+cti+":"+str(ports)+":Not Open\n")
                      sock.close()
      except KeyboardInterrupt:
        file_port.write("You pressed Ctrl+C")
        sys.exit()

      except socket.gaierror:
        file_port.write('Hostname could not be resolved. Exiting')
        sys.exit()

      except socket.error:
        file_port.write("Couldn't connect to server")
        sys.exit()
      except:
        file_port.write("Unable to Load Service Profile")


    def imp(self):
      file_port = open("C:/Python27/port_scanner.txt", 'a+')
      #ports_ = open("C:/Python27/ports_.txt","w+")
      try:
          file = open("c:/Python27/service.txt", 'r').read()
          info = file.split('\n')
          imp_port = [443, 5222, 37200, 7336]
          item = re.findall(r'IMP:(.*?)\n',file,re.I |re.M)
          #print("88",item[2])
          for line in item :
              imp_ = line.split(':')
              if imp_[1] != "Not Configured":
                  cti = socket.gethostbyname(imp_[1])
                 # print("hi",imp_[1])
                  for ports in imp_port:
                      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                      result = sock.connect_ex((cti, ports))
                      print("\nIMP Server: " + str(cti) + " Ports:" +str(ports) + "\n")

                      print result
                      if result == 0:
                          file_port.write("IMP:"+cti+":"+str(ports)+":Open\n")
                      else:
                          file_port.write("IMP:"+cti+":"+str(ports)+":Not Open\n")
                      sock.close()
      except KeyboardInterrupt:
        file_port.write("You pressed Ctrl+C")
        sys.exit()

      except socket.gaierror:
        file_port.write('Hostname could not be resolved. Exiting')
        sys.exit()

      except socket.error:
        file_port.write("Couldn't connect to server")
        sys.exit()
      except:
        file_port.write("Unable to Load Service Profile")

    def voice(self):
        file_port = open("C:/Python27/port_scanner.txt", 'a+')
        # ports_ = open("C:/Python27/ports_.txt","w+")
        try:
            file = open("c:/Python27/service.txt", 'r').read()
            info = file.split('\n')
            voice_port = [7080, 7443, 443]
            item = re.findall(r'VoiceMail:(.*?)\n', file, re.I | re.M)
           # print("88", item[2])
            for line in item:
                voice_ = line.split(':')
                if voice_[1] != "Not Configured":
                    cti = socket.gethostbyname(voice_[1])
                    #print("hi", voice_[1])
                    for ports in voice_port:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex((cti, ports))
                        print("Voice Server: " + str(cti) + " Ports:" + str(ports) + "\n")

                        print result
                        if result == 0:
                            file_port.write("VoiceMail:" + cti + ":" + str(ports) + ":Open\n")
                        else:
                            file_port.write("VoiceMail:" + cti + ":" + str(ports) + ":Not Open\n")
                        sock.close()
        except KeyboardInterrupt:
            file_port.write("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            file_port.write('Hostname could not be resolved. Exiting')
            sys.exit()

        except socket.error:
            file_port.write("Couldn't connect to server")
            sys.exit()
        except:
            file_port.write("Unable to Load Service Profile")

    def run(self):

        file_port = open("C:/Python27/port_scanner.txt","w+")
        # t1 = Thread(target=self.cucm)
        # t2 = Thread(target= self.imp)
        # t3 = Thread(target=self.voice)
        #
        # t1.start()
        # t2.start()
        # t3.start()
        self.cucm()
        self.imp()
        self.voice()

        # x = threading.enumerate()
        # print("Live threads ",x)
        # portobj.t1.join(port)
        # t2.join()
        # t3.join()
        # x = threading.enumerate()
        # print("done threads ", x)
        # if x == 1:
        #     print("Done")


        # if t1.isAlive()  == True :
        #     print("Thread2 is done")
        # if t3.isAlive() == True :
        #     print("thread 3 is done")
        # if t1.isAlive() == False and t2.isAlive()== False and t3.isAlive()==False :
        #     print("DOne")
        #     window = tk.Tk()
        #     label = ttk.Label(window, text = "New Window")
        #     label.pack()
        #     window.mainloop()
        #uiobj.event2.set()
        # uiobj.text = Text(uiobj.page9, foreground="BLACK", yscrollcommand=uiobj.scrollbar_ff.set, width=80, height=15)
        # uiobj.text.config(state=NORMAL)
        # #uiobj.text.insert(INSERT, file_portScan)
        # uiobj.text.insert(END, "HI")
        # uiobj.text.config(state=DISABLED)
        # uiobj.text.grid(row=0, column=2)
        # if t1.isAlive() == False :
        #     print("T1 ended")
        # if t2.isAlive() == False :
        #     print("T2 ended")
        # if t2.isAlive() == False:
        #     print("T2 ended")
        # portobj.port_value = 1

        # time.sleep(1)

        # scrollbar_ff.grid(row=0, column=3)
        # text = Text(page9, foreground="BLACK", yscrollcommand=scrollbar_ff.set, width=80, height=15)
        # text.config(state=NORMAL)
        # text.insert(INSERT, file_portScan)
        # text.insert(END, "")
        # text.config(state=DISABLED)
        # text.grid(row=0, column=2)
        # scrollbar_ff.config(command=text.yview)

#
#

portobj = port()
#portobj.run()
print("port time", time.time()-start)

#portobj = port()

