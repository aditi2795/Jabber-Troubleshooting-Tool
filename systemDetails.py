import re
import subprocess
import time
import re
from ManualLogin import *
import subprocess
import os
import sys
import logging
class appinfo:
    vpn=""
    ie=""
    av=""
    jabber=""
    chrome=""
    mozilla=""
    speed=""
    outlook=""
    webex=""

    def SysDetails(self):

        file_sysdetails=open(manualobj.browseValue+"/sysdetails.txt","w+")
        file_sysdetails_complete=open(manualobj.browseValue+"/programs.txt","w+")
        file_sysdetails.write("Installed software details" + "\n")
        file_sysdetails.write("*"*50 + "\n\n")
        try:
            # -*- coding: utf-8 -*-
            proc1 = subprocess.Popen(["C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table"],stdout=file_sysdetails_complete, shell=True)
            time.sleep(5)

            # aman.wait(5)
            proc1.kill()
            info=open(manualobj.browseValue+"/programs.txt","r").read()
            anyconnect = 0

            for row in info.decode('cp1252').split('\n'):
                if "Cisco AnyConnect" in row:

                    if anyconnect != 1:
                        row = row.split()
                        row = (" ".join(str(x) for x in row))
                        row = row.split()
                        row1 = row[0:4]
                        row2 = row[5]
                        name = (" ".join(str(x) for x in row1))

                        file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                        file_sysdetails.write("\n\n")
                        anyconnect = 1

                if "McAfee VirusScan Enterprise" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:3]
                    row2 = row[3]
                    name = (" ".join(str(x) for x in row1))
                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")

                if "Plantronics Hub" in row:
                    print row
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:3]
                    row2 = row[3]
                    name = (" ".join(str(x) for x in row1))
                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")

                if "Kaspersky" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:3]
                    row2 = row[3]
                    name = (" ".join(str(x) for x in row1))
                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")

                if "Norton" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:3]
                    row2 = row[3]
                    name = (" ".join(str(x) for x in row1))
                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")
                if "QuickHeal" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:3]
                    row2 = row[3]
                    name = (" ".join(str(x) for x in row1))
                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")
                if "Cisco Jabber" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:2]
                    row2 = row[2]
                    name = (" ".join(str(x) for x in row1))

                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")
                if "Microsoft Lync" in row:
                    file_sysdetails.write("\n" + row + "\n")
                if "Google Chrome" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:2]
                    row2 = row[2]
                    name = (" ".join(str(x) for x in row1))

                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")

                if "Check Point VPN" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:3]
                    row2 = row[3]
                    name = (" ".join(str(x) for x in row1))

                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")
                if "Mozilla Firefox" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:2]
                    row2 = row[2]
                    name = (" ".join(str(x) for x in row1))

                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")
                if "WebEx Productivity Tools" in row:
                    print
                    row
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:3]
                    row2 = row[3]
                    name = (" ".join(str(x) for x in row1))

                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")
                if "Microsoft Outlook MUI (English)" in row:
                    row = row.split()
                    row = (" ".join(str(x) for x in row))
                    row = row.split()
                    row1 = row[0:5]
                    row2 = row[5]
                    name = (" ".join(str(x) for x in row1))

                    file_sysdetails.write(name + " " * (50 - len(name)) + str(row2))
                    file_sysdetails.write("\n\n")

            try:
                application_info.ie = subprocess.check_output("reg query \"HKEY_LOCAL_MACHINE\Software\Microsoft\Internet Explorer\" /v version | find \"version\"",shell=True)
                application_info.ie = application_info.ie.split("REG_SZ")[1]
                file_sysdetails.write("\n" + "Internet Explorer" + " " * (47 - len("Internet Explorer")) + application_info.ie + "\n")
            except:
                pass
            try:
                application_info.regimp = subprocess.check_output("reg query \"HKEY_LOCAL_MACHINE\Software\IM Providers\"",shell=True)
                imap = re.findall(r'HKEY_LOCAL_MACHINE\\Software\\IM Providers\\(.*)', application_info.regimp, re.I | re.M)
                for line in imap:
                    file_sysdetails.write("IM App" + " " * (44) + line + "\n\n")
            except:
                pass

            try:
                application_info.callint = subprocess.check_output(
                    "reg query \"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\Outlook\Call Integration\"", shell=True)
                application_info.callint = application_info.callint.split("REG_SZ")[1]
                file_sysdetails.write("\n" + "Call Integration IMApplication" + " " * (
                45 - len("Call Integration IMApplication")) + application_info.callint + "\n")

                file_sysdetails.write("\n" + "Hardware details" + "\n")
                file_sysdetails.write("*" * 50 + "\n\n")
            except:
                pass

            # find display_resolution

            try:
                display_resolution = subprocess.check_output("wmic path Win32_VideoController get VideoModeDescription",
                                                         shell=True)
                display_resolution = (display_resolution.decode('utf8').split())
                display_resolution = '{:2} {:2} {:2}'.format(display_resolution[1], display_resolution[2],
                                                         display_resolution[3])
                file_sysdetails.write("\n" + "Display Resolution  " + " "*(50-len('display resolution')) + display_resolution)
            except:
                pass
            # check virtual machine

            try:
                virtual = subprocess.check_output("systeminfo", shell=True)
                vm1 = 0
                for row in virtual.split('\n'):
                    if "System Manufacturer" in row:
                        vm = row.split(":")[1]
                        if "VMware" in vm or "Citrix" in vm:
                            vm1 = 1
                    if "OS Version" in row:
                        file_sysdetails.write("\n\n" + row + "\n\n")
                    if "OS Name" in row:
                        file_sysdetails.write("\n\n" + row + "\n\n")
                    if "Virtual Memory: Available:" in row:
                        file_sysdetails.write("\n\n" + row + "\n\n")
                    if "Available Physical Memory:" in row:
                        file_sysdetails.write("\n\n" + row + "\n\n")

                if vm1 == 1:
                    file_sysdetails.write("\n\n" + "System Manufacturer  " + " "*(5)+vm)
                else:
                    file_sysdetails.write("\n\n" + "System Manufacturer  " + " "*(5)+ vm)
            except:
                pass
            try:
                fips = subprocess.check_output("reg query \"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\FIPSAlgorithmPolicy\" | find \"Enabled\"",shell=True)
                enabled = fips.split("\n")[0]
                enabled_value = enabled.split("REG_DWORD")[1]
                enabled_value = [x.rstrip() for x in enabled_value]
                enabled_value = filter(lambda name: name.strip(), enabled_value)
                enabled_value = ''.join(enabled_value)
                print (enabled_value)
                if enabled_value == "0x0":
                    file_sysdetails.write("\nFIPS                       Disabled\n")
                else:
                    file_sysdetails.write("\nFIPS                       Enabled\n")

            #
            # logonserver = subprocess.check_output(["echo", "%LOGONSERVER%"], shell=True)
            # logonserver = logonserver.split("\\")
            # logonserver = [x.rstrip() for x in logonserver]
            # logonserver = filter(lambda name: name.strip(), logonserver)
            # logonserver = ''.join(logonserver)
            # file_sysdetails.write("\nDomain Controller ", str(logonserver) + "\n")


            # check locale
            except:
                pass
            try:
                locale = subprocess.check_output("systeminfo | findstr /B /C:\"System Locale\"", shell=True)
                locale = locale.decode('utf8').split()[2]
                file_sysdetails.write("\n\n" + "Locale is" + "\t\t\t       " + locale+"\n")
                a = os.system(
                    'reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" > C:\Python27\proxy.txt')
                file = open("C:\Python27\proxy.txt", "r")
                filedata = file.read()
            except:
                pass
            try:
                proxyenable = re.findall(r' ProxyEnable    REG_DWORD    (.*)', filedata, re.I | re.M)
                # print(proxyenable)
                proxyserver = ""
                if proxyenable[0] == "0x0":
                    p0 = "Proxy is not enabled"
                    file_sysdetails.write(p0+"\n")
                    proxyserver = re.findall(r' ProxyServer    REG_SZ   (.*)', filedata, re.I | re.M)
                # print(proxyserver,p0)
                    if proxyserver == []:
                        file_sysdetails.write(p0+"\n")
                    else:
                        file_sysdetails.write(str(p0) + "\tProxy Server: \t\t" + str(proxyserver[0])+"\n")

                elif proxyenable[0] == "0x1":
                    p0 = ("\nProxy is enabled")
                    proxyserver = re.findall(r' ProxyServer    REG_SZ    (.*)', filedata, re.I | re.M)
                    # print(proxyserver)
                    file_sysdetails.write(str(p0) + "\tProxy Server\t\t" + str(proxyserver)+"\n")
            except:
                pass

            logging.debug("System details executed successfully")


    # proxyobject.proxyfn()
        except Exception as e:

            logging.error(str(e))
            file_sysdetails.write("ERROR")

application_info=appinfo()
#application_info.pwshell()
# application_info.sysdetails_out=open("C:/Python27/sysdetails.txt","r").read()
#
# if __name__=="__main__":
#     application_info.pwshell()

