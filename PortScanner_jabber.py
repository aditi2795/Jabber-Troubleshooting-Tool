import socket
import subprocess
import sys
import multiprocessing
import time
from ManualLogin import *
from ServiceProfile import *

start = time.time()

class port:
    def portfn(self):

      file_port = open(manualobj.browseValue+"/port_scan.txt", 'w+')
      ports_ = open(manualobj.browseValue+"/ports_.txt","w+")
      portsum=open(manualobj.browseValue+"/portsummary.txt",'w+')

      try:
          if manualobj.flag!=2:

              file = open(manualobj.browseValue+"/service.txt", 'r').read()
              info = file.split('\n')
              for row in info:

                  if "IMP" in row:
                      IMP1 = row.split(':')[2]

                      IMP1_IP = socket.gethostbyname(IMP1)
                      print IMP1_IP
                      break

              for row in info:
                  if "CTI" in row:
                      cti1 = row.split(':')[2]
                      cti1_ip = socket.gethostbyname(cti1)
                      print (cti1_ip)
                      break

              for row in info:
                  if "VoiceMail" in row:
                      voice1 = row.split(':')[2]
                      voice1_ip = socket.gethostbyname(voice1)
                      print voice1_ip
                      break


          else:
              file = open(manualobj.browseValue + "/imp_jabber.txt", 'r').read()
              info = file.split('\n')
              for row in info:

                  if "IMP" in row:
                      IMP1 = row.split(':')[2]

                      IMP1_IP = socket.gethostbyname(IMP1)
                      print IMP1_IP
                      break

              for row in info:
                  if "VoiceMail" in row:
                      voice1 = row.split(':')[2]
                      voice1_ip = socket.gethostbyname(voice1)
                      print voice1_ip
                      break

              for row in info:
                  if "CTI" in row:
                      cti1 = row.split(':')[2]
                      cti1_ip = socket.gethostbyname(cti1)
                      print (cti1_ip)
                      break


      except:
        file_port.write("Unable to Load ")

      cucm = [6970, 6972, 3804, 8443, 2748, 5060, 5061]
      dir = [389, 3268, 636, 3269]
      IMP = [443, 5222, 37200, 7336]
      voice = [7080, 7443, 443]
      webex = [80, 443, 8443]

      try:

          #file_port.write("|Port  |STATUS   |\n")
          #file_port.write("|------|---------|\n")
        #cucm_serv =["10.127.230.200","10.127.230.201"]

          for port in cucm:
              sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              result = sock.connect_ex((cti1_ip, port))
              print("res",result)
              if result == 0:
                  file_port.write("CUCM:"+cti1_ip+":"+str(port)+":Open\n")
              else:
                  file_port.write("CUCM:"+cti1_ip+":"+str(port)+":Not Open\n")
                  portsum.write("CUCM:"+cti1_ip+":"+str(port)+"\n")

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
          file_port.write("Unable to reach server")

      try:



          for port in voice:
              sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              result = sock.connect_ex((voice1_ip, port))
              #result = socket.conect(voice1_ip,port)
              print (result)
              if result == 0:
                  file_port.write("VOICEMAIL:"+voice1_ip+":"+str(port)+":Open\n")
              else:
                  file_port.write("VOICEMAIL:"+voice1_ip+":"+str(port)+":NotOpen\n")
                  portsum.write("VOICEMAIL:"+voice1_ip+":"+str(port)+"\n")
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
          file_port.write("Unable to reach server")

      try:



          for port in IMP:
              sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              result = sock.connect_ex((IMP1_IP, port))
              if result == 0:
                  file_port.write("IMP:"+IMP1_IP+":"+str(port)+":Open\n")
              else:
                  file_port.write("IMP:"+IMP1_IP+":"+str(port)+":NotOpen\n")
                  portsum.write("IMP:"+IMP1_IP+":"+str(port)+"\n")
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
          file_port.write("Unable to reach server")


start = time.time()

print("time",time.time()-start)