import Tkinter
import ttk
import re
from ManualLogin import *
import tkHyperlinkManager
import webbrowser


# from Thread1 import *


class RunnerUI():
    def MainApp(self):
        root = Tk()

        try:
            root.wm_iconbitmap('img1.ico')
        except TclError:
            print ('No ico file found')

        root.title("ttk.Notebook")
        root.title("Jabber Validation Report")
        root.geometry("1500x500")

        nb = ttk.Notebook(root)

        w = Label(root, text="Copyright 1992-2017 Cisco and/or its affiliates. All rights reserved")
        w.pack(side=BOTTOM, fill=BOTH, expand=YES)

        if manualobj.flag == 0:
            # adding Frames as pages for the ttk.Notebook
            # first page, which would get widgets gridded into it
            page1 = ttk.Frame(nb, borderwidth=110, width=1000, height=1000)
            page2 = ttk.Frame(nb, borderwidth=110, width=1000, height=1000)
            page3 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page4 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page5 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page6 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page7 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page8 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page9 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page10 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page11 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page12 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page13 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page14 = ttk.Frame(nb, borderwidth=110, width=200, height=500)


            nb.add(page11, text='Summary')
            nb.add(page1, text='System Details')
            nb.add(page2, text='User Details')
            nb.add(page3, text='DNS Information')
            nb.add(page4, text='Service Profile')
            nb.add(page5, text='Devices')
            nb.add(page6, text='Jabber Config')
            nb.add(page7, text='Certificates')
            nb.add(page8, text='IM and Presence')

            nb.add(page9, text='Directory-cucm')

            nb.add(page10, text='SSO')

            nb.add(page12, text='Port Scanner')
            nb.add(page13, text='Open Caveats')
            #nb.add(page14, text='Sequence Diagram')
            nb.add(page14,text="About")

            nb.pack(expand=1, fill="both")


            # Adding Image

            # img = tk.PhotoImage(file=manualobj.browseValue + "/code_flow.gif")
            #
            #
            #
            #
            #
            #
            # scrollbary = Scrollbar(page14, orient=VERTICAL)
            # text = Text(page14, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)
            #
            # text.image_create(tk.END, image=img)
            #
            # text.pack(side=LEFT, fill=BOTH, expand=YES)
            # scrollbary = Scrollbar(page14, orient=VERTICAL, command=text.yview)
            # scrollbary.pack(side=RIGHT, fill=Y)
            # text["yscrollcommand"] = scrollbary.set



            #############################################################################
            # dns
            ###########################################################################

            # def Process2 () :

            file_dns = open(manualobj.browseValue + "/dns.txt", "r").read()
            tree_dns = ttk.Treeview(page3, height=10)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_dns.tag_configure("Treeview", background="black")
            tree_dns['columns'] = ('Server', 'IP', 'Port', 'Weight', 'Priority')
            tree_dns.heading("#0", text="SRV")
            tree_dns.column("#0", width=50, anchor=Tkinter.W)

            treescrolldns = ttk.Scrollbar(page3, command=tree_dns.yview)
            treescrolldns.configure(command=tree_dns.yview)
            tree_dns.configure(yscrollcommand=treescrolldns.set)
            treescrolldns.pack(side='right', fill='y')

            tree_dns.heading("Server", text="Server")
            tree_dns.column('Server', anchor='center', width=100)

            tree_dns.heading("IP", text="IP")
            tree_dns.column('IP', anchor='center', width=50)
            # tree_dns.pack(expand=YES, fill=BOTH)

            tree_dns.heading("Port", text="Port")
            tree_dns.column('Port', anchor='center', width=60)

            tree_dns.heading("Weight", text="Weight")
            tree_dns.column('Weight', anchor='center', width=50)

            tree_dns.heading("Priority", text="Priority")
            tree_dns.column('Priority', anchor='center', width=50)
            tree_dns.pack(expand=YES, fill=BOTH)

            list = re.findall(r'_cisco-uds._tcp.:SRV:(.*?)\n', file_dns, re.M | re.I)
            print("new", list)
            if list[0] == "NO RECORDS FOUND":
                tree_dns.insert("", 'end', text="_cisco-uds._tcp.", values=["NO", "RECORDS", "FOUND"])
            else:

                print("list", list)
                li_index = 0
                for line in list:
                    item = list[li_index].split(':')
                    tree_dns.insert("", 'end', text="_cisco-uds._tcp.",
                                    values=[item[0], item[4], item[1], item[2], item[3]])
                    li_index += 1


                    # index += 1

            # cuplogin
            list = re.findall(r'_cuplogin._tcp.:SRV:(.*?)\n', file_dns, re.M | re.I)
            if list[0] == "NO RECORDS FOUND":
                tree_dns.insert("", 'end', text="_cuplogin._tcp.", values=["NO", "RECORDS", "FOUND"])
            else:
                li_index = 0
                for line in list:
                    item = list[li_index].split(':')
                    tree_dns.insert("", 'end', text="_cuplogin._tcp.",
                                    values=[item[0], item[4], item[1], item[2], item[3]])
                    li_index += 1

            # index += 1
            # _collab-edge_tcp:SRV:
            list = re.findall(r'_collab-edge_tcp:SRV:(.*?)\n', file_dns, re.M | re.I)
            if list[0] == "NO RECORDS FOUND":
                # tree_dns.heading('#0',text="No records")
                tree_dns.insert("", 'end', text="collab-edge_tcp", values=["NO", "RECORDS", "FOUND"])
            else:
                li_index = 0
                for line in list:
                    item = list[li_index].split(':')
                    tree_dns.insert("", 'end', text="collab-edge_tcp",
                                    values=[item[0], item[4], item[1], item[2], item[3]])
                    li_index += 1

            # _gc._tcp.:SRV
            # index+=1

            list = re.findall(r'_gc._tcp.:SRV:(.*?)\n', file_dns, re.M | re.I)

            if list[0] == "NO RECORDS FOUND":
                tree_dns.insert("", 'end', text="_gc._tcp. ", values=["NO", "RECORDS", "FOUND"])
            else:
                li_index = 0
                for line in list:
                    item = list[li_index].split(':')
                    tree_dns.insert("", 'end', text="_gc._tcp.", values=[item[0], item[4], item[1], item[2], item[3]])
                    li_index += 1

            # index+=1

            # ldap
            list = re.findall(r'_ldap._tcp.:SRV:(.*?)\n', file_dns, re.M | re.I)
            # tree_dns.insert("",'end',values ="hi")
            if list[0] == "NO RECORDS FOUND":
                tree_dns.insert("", 'end', text="_ldap._tcp.", values=["NO", "RECORDS", "FOUND"])
            else:
                li_index = 0
                print("ldap", list)
                for line in list:
                    item = list[li_index].split(':')
                    tree_dns.insert("", 'end', text="_ldap._tcp.", values=[item[0], item[4], item[1], item[2], item[3]])
                    li_index += 1

                    #########################################################################################
                    # User Details
                    ########################################################################################

            userDetails = open(manualobj.browseValue + "/userdetails.txt", "r").read()
            tree_user = ttk.Treeview(page2, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")

            tree_user.tag_configure("Treeview", background="black")
            tree_user['columns'] = ('Attributes', 'Values')
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_user['show'] = 'headings'
            tree_user.column("#0", width=50, anchor=Tkinter.W)
            tree_user.heading("Attributes", text="Attributes")
            tree_user.column('Attributes', anchor='center', width=100)
            tree_user.heading("Values", text="Values")
            tree_user.column('Values', anchor='w', width=100)
            treescrolluser = ttk.Scrollbar(page2, command=tree_user.yview)
            treescrolluser.configure(command=tree_user.yview)
            tree_user.configure(yscrollcommand=treescrolluser.set)
            treescrolluser.pack(side='right', fill='y')
            att = re.findall(r'(.*?)=', userDetails, re.I | re.M)
            value = re.findall(r'=(.*?)\n', userDetails, re.I | re.M)
            index = 0

            # print("new123", att, " ",value)

            for line in att:
                if line != "serviceProfile":
                    tree_user.insert("", 0, values=[line, value[index]])
                    index += 1

            tree_user.pack(expand=YES, fill=BOTH)
            #################################################################################################
            # Service Profile
            ##################################################################################################
            ServicePro = open(manualobj.browseValue + "/service.txt", "r").read()
            tree_service = ttk.Treeview(page4, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_service.tag_configure("Treeview", background="black")
            tree_service['columns'] = ('Function', 'Server', 'Address', 'Port', 'Protocol')
            treescroll = ttk.Scrollbar(page4, command=tree_service.yview)
            treescroll.configure(command=tree_service.yview)
            tree_service.configure(yscrollcommand=treescroll.set)
            treescroll.pack(side='right', fill='y')

            # tree_dns.heading("#0", text="SRV")
            # tree_dns.column("#0", width=50, anchor=Tkinter.W)

            tree_service['show'] = 'headings'
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            tree_service.heading("Function", text="Function")
            tree_service.column('Function', anchor='center', width=100)

            tree_service.heading("Server", text="Server")
            tree_service.column('Server', anchor='center', width=100)

            tree_service.heading("Address", text="Address")
            tree_service.column('Address', anchor='center', width=100)

            tree_service.heading("Port", text="Port")
            tree_service.column('Port', anchor='center', width=100)

            tree_service.heading("Protocol", text="Protocol")
            tree_service.column('Protocol', anchor='center', width=100)

            tree_service.pack(expand=YES, fill=BOTH)

            treescroll = ttk.Scrollbar(page4, command=tree_service.yview)
            treescroll.configure(command=tree_service.yview)
            tree_service.configure(yscrollcommand=treescroll.set)
            treescroll.pack(side='right', fill='y')

            voice = re.findall(r'VoiceMail(.*?)\n', ServicePro, re.I | re.M)

            # tree_service.heading("#0", text="SRV")
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            # for line in voice :
            #     list_voice = line.split('')

            print(voice)

            tree_service.insert("", 0, values="Voicemail")
            for line in voice:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_service.insert("", 'end', values="Mailstore")

            mailstore = re.findall(r'MailStore(.*?)\n', ServicePro, re.I | re.M)
            for line in mailstore:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            Conferencing = re.findall(r'Conferencing(.*?)\n', ServicePro, re.I | re.M)

            tree_service.insert("", 'end', values="Conferencing")

            for line in Conferencing:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_service.insert("", 'end', values="Directory")

            directory = re.findall(r'Directory(.*?)\n', ServicePro, re.I | re.M)

            for line in directory:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_service.insert("", 'end', values="IMP")

            imp = re.findall(r'IMP(.*?)\n', ServicePro, re.I | re.M)

            for line in imp:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            cti = re.findall(r'CTI(.*?)\n', ServicePro, re.I | re.M)

            tree_service.insert("", 'end', values="CTI")

            for line in cti:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            vcs = re.findall(r'VCS(.*?)\n', ServicePro, re.I | re.M)

            tree_service.insert("", 'end', values="VCS")

            for line in vcs:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])
            ##################################################################################
            # System Details
            #################################################################################

            sysdetails = open(manualobj.browseValue + "/sysdetails.txt", "r").read()

            scrollbary = Scrollbar(page1, orient=VERTICAL)
            text = Text(page1, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)

            text.config(state=NORMAL)
            text.insert(INSERT, sysdetails)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbary = Scrollbar(page1, orient=VERTICAL, command=text.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbary.set

            ###########################################################################
            # devices
            ##############################################################################
            final_dev = open(manualobj.browseValue + "/Final_devices.txt", "r").read()


            text = Text(page5, foreground="BLACK", width=110, height=15)
            scrollbar_devices = Scrollbar(page5, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, final_dev)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_devices.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_devices.set

            #####################################################################################
            # jabber config
            #####################################################################################
            jabber_config = open(manualobj.browseValue + "/jabber_config.txt", "r").read()
            jabber_config_local = open(manualobj.browseValue + "/jabber_local_config.txt", "r").read()
            text = Text(page6, foreground="BLACK", width=110, height=15)
            scrollbar_jabberconfig = Scrollbar(page6, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, jabber_config)
            text.insert(INSERT,"\n\n\n")
            text.insert(INSERT, jabber_config_local)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_jabberconfig.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_jabberconfig.set

            #################################################
            # IM&P
            ############################################
            imp_process = open(manualobj.browseValue + "\imp_login.txt", "r").read()

            scrollbary = Scrollbar(page8, orient=VERTICAL, command=text.yview)
            text = Text(page8, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)
            text.config(state=NORMAL)
            text.insert(INSERT, imp_process)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbary.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbary.set

            ##################################################
            # SSO
            ##################################################
            sso = open(manualobj.browseValue + "/sso_voicemail.txt", "r").read()
            sso_callmanager = open(manualobj.browseValue + "/sso_cucm.txt", 'r').read()
            sso_imp = open(manualobj.browseValue + "/sso_imp.txt", 'r').read()


            text = Text(page10, foreground="BLACK", width=110, height=15)
            scrollbar_sso = Scrollbar(page10, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)

            text.insert(INSERT, "CallManager\n")
            text.insert(END, "------------------------------------------------------------------------------\n")
            text.insert(INSERT, sso_callmanager)
            text.insert(END, "")
            # text.insert(END, "\n\n****************************************************************\n")
            text.insert(INSERT, "\n\nVoiceMail\n")
            text.insert(END, "------------------------------------------------------------------------------\n")
            text.insert(INSERT, sso)
            text.insert(END, "")
            text.insert(INSERT, "\n\nIMP\n")
            text.insert(END, "------------------------------------------------------------------------------\n")
            text.insert(INSERT, sso_imp)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_sso.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_sso.set

            ########################################################################
            # Summary
            ########################################################################

            default = open(manualobj.browseValue + "/jabber_summary.txt", 'r').read()
            auth_summary = open(manualobj.browseValue + '\\authentication_summary.txt', 'r').read()
            cucm_service = open(manualobj.browseValue + '/cucmservicesummary.txt', 'r').read()
            imp_service = open(manualobj.browseValue + "/impservicesummary.txt", 'r').read()
            port = open(manualobj.browseValue + "/portsummary.txt", 'r').read()
            summary = open(manualobj.browseValue + "/summary.txt", 'r').read()
            impsummary = open(manualobj.browseValue + "/imp_summary.txt", 'r').read()
            fqdn = open(manualobj.browseValue + "/fqdn.txt", 'r').read()
            text = Text(page11, foreground="BLACK", width=110, height=15)


            def software_details():
                webbrowser.open_new(r'https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html')

            def port_details():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html")

            def parameters_reference_guide():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html")
            def ipv6():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_6/cjab_b_planning-guide-cisco-jabber-116/cjab_b_planning-guide-cisco-jabber-116_chapter_010.html#reference_AEEDA51FE1A43E22D7D7D90308568C19")

            text["yscrollcommand"] = scrollbary.set

            text.config(state=NORMAL)
            hyperlink = tkHyperlinkManager.HyperlinkManager(text)
            text.insert(INSERT,"-" * 50)
            text.insert(INSERT, "\n")
            text.insert(INSERT,"JABBER VALIDATION STATUS")
            text.insert(INSERT, "\n\n")
            text.insert(INSERT,"-" * 50)
            text.insert(INSERT, "\n\n")
            text.insert(INSERT,auth_summary)
            text.insert(END, "\n\n")
            text.insert(INSERT, "\nThe following software(s) are either not supported or version is incompatible with. Please refer to the ")
            text.insert(INSERT, "Release notes" ,hyperlink.add(software_details))
            text.insert(INSERT, "\n\n\n")
            text.insert(INSERT, summary + "\n")
            text.insert(INSERT,"Reference link IPv6", hyperlink.add(ipv6))
            text.insert(END, "\n\n")
            text.insert(INSERT,"Below are the Parameters which are not having default Values.Check the")
            text.insert(INSERT, " Parameters Reference Guide ", hyperlink.add(parameters_reference_guide))
            text.insert(INSERT, " for Cisco Jabber to evaluate if this impair Jabber features\n\n\n")
            text.insert(INSERT,default)
            text.insert(END,'\n\n')
            text.insert(INSERT, "Following ports are not open which would affect the functionality of Jabber. Please refer ")
            text.insert(INSERT,"Ports and Protocols ",hyperlink.add(port_details))
            text.insert(INSERT,"section of Release notes for more details\n\n\n")
            text.insert(INSERT, port)
            text.insert(END, "\n\n")

            text.insert(INSERT, cucm_service)
            text.insert(INSERT, "\n\n")

            text.insert(INSERT, fqdn + " ")
            text.insert(END, "\n")


            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbar_summary = Scrollbar(page11, orient=VERTICAL, command=text.yview)
            text["yscrollcommand"] = scrollbar_summary.set
            scrollbar_summary.pack(side=RIGHT, fill=Y)
            scrollbary.pack(side=RIGHT, fill=Y)


            ####################################################################################
            # Directory cucm
            ####################################################################################
            file_dir_cucm = open(manualobj.browseValue + "/directory_cucm.txt", 'r').read()

            tree_dir_cucm = ttk.Treeview(page9, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_dir_cucm.tag_configure("Treeview", background="black")
            tree_dir_cucm['columns'] = ('Name', 'Values')
            treescrolldircucm = ttk.Scrollbar(page9, command=tree_dir_cucm.yview)
            treescrolldircucm.configure(command=tree_dir_cucm.yview)
            tree_dir_cucm.configure(yscrollcommand=treescrolldircucm.set)
            treescrolldircucm.pack(side='right', fill='y')

            tree_dir_cucm['show'] = 'headings'

            tree_dir_cucm.heading("Name", text="Name")
            tree_dir_cucm.column('Name', anchor='center', width=50)

            tree_dir_cucm.heading("Values", text="Values")
            tree_dir_cucm.column('Values', anchor='center', width=200)

            tree_dir_cucm.pack(expand=YES, fill=BOTH)

            # line = file_enterprise.split(':')
            index = 0

            file_dir_cucm = file_dir_cucm.split('\n')
            print("***")
            for line in file_dir_cucm:
                # print(line)
                item = line.split(':')
                print(item)
                x = len(item)
                index = 0
                # while index <= x :
                if x == 3:
                    tree_dir_cucm.insert("", 'end', values=[item[0], item[1], item[2]])
                elif x == 2:
                    tree_dir_cucm.insert("", 'end', values=[item[0], item[1]])
                    ##################################################################################
                    # Directory Imp
                    #################################################################################



                    ############################################################
                    # Port scan
                    #########################################################
            port_ = open(manualobj.browseValue + "/port_scan.txt", "r").read()

            tree_port = ttk.Treeview(page12, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_port.tag_configure("Treeview", background="black")
            tree_port['columns'] = ('Server', "Ip", 'Port', 'Status')

            tree_port['show'] = 'headings'
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            tree_port.heading("Server", text="Server")
            tree_port.column('Server', anchor='center', width=100)

            tree_port.heading("Ip", text="Ip")
            tree_port.column('Ip', anchor='center', width=100)

            tree_port.heading("Port", text="Port")
            tree_port.column('Port', anchor='center', width=100)

            tree_port.heading("Status", text="Status")
            tree_port.column('Status', anchor='center', width=100)

            treescrollport = ttk.Scrollbar(page12, command=tree_port.yview)
            treescrollport.configure(command=tree_port.yview)
            tree_port.configure(yscrollcommand=treescrollport.set)
            treescrollport.pack(side='right', fill='y')

            tree_port.pack(expand=YES, fill=BOTH)

            port = re.findall(r'CUCM(.*?)\n', port_, re.I | re.M)



            print(voice)

            tree_port.insert("", 0, values="CUCM")
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            port = re.findall(r'VOICEMAIL(.*?)\n', port_, re.I | re.M)

            tree_port.insert("", 'end', values="VOICEMAIL")
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            tree_port.insert("", 'end', values="IMP")

            port = re.findall(r'IMP(.*?)\n', port_, re.I | re.M)
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])



            ############################################################################
            # certificates
            ###########################################################################
            certificate_voice = open(manualobj.browseValue + "/certdatavoice.txt", "r").read()
            certificate_imp = open(manualobj.browseValue + "/certdataimp.txt", "r").read()
            certificate_cti = open(manualobj.browseValue + "/certdata.txt", 'r').read()
            trusted_cert = open(manualobj.browseValue + "/trusted certificates.txt", 'r').read()


            text = Text(page7, foreground="BLACK", width=110, height=15)
            scrollbar_certificates = Scrollbar(page7, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, "CUCM\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_cti)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(INSERT, "\n\nVOICEMAIL\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_voice)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(INSERT, "\n\nIM&P\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_imp)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(END, "")
            text.insert(INSERT, "\n\nTRUSTED CERTIFICATES\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, trusted_cert)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_certificates.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_certificates.set

            # Caveats
            file_list_of_programs = open(manualobj.browseValue + "\\sysdetails.txt", 'r').read()

            info = file_list_of_programs.decode('cp1252').split('\n')

            # hyperlink = tkHyperlinkManager.HyperlinkManager(text)
            version=0
            for row in info:
                if "Cisco Jabber" in row:
                    value = row
                    list = value.split()
                    list = filter(None, list)
                    version = list[2]
                    print version
                    break
                    #print value
            if version!=0:

                if "11.8" == version[:4]:
                    file_caveats = open("caveats_11.8.txt", 'r').read()
                    print " version match"
                    # i=1
                    # click={1:a,2:b,3:c,4:d,5:e,6:f,7:g,8:h,9:i,10:j,11:k,12:l,13:m}

                    # print row
                    # text.insert(INSERT, row)
                    #
                    # text.insert(INSERT, " " + "Click Here" , hyperlink.add(click[i]))
                    # text.insert(INSERT,"\n\n")
                    # i=i+1


                    tree_caveats = ttk.Treeview(page13, height=20)
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")

                    tree_caveats.tag_configure("Treeview", background="black")
                    tree_caveats['columns'] = ('Identifier', 'Severity', 'Description')
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")
                    tree_caveats['show'] = 'headings'
                    tree_caveats.column("#0", width=50, anchor=Tkinter.W)
                    tree_caveats.heading("Identifier", text="Identifier")
                    tree_caveats.column('Identifier', anchor='center', width=100)
                    tree_caveats.heading("Severity", text="Severity")
                    tree_caveats.column('Severity', anchor='center', width=10)
                    tree_caveats.heading("Description", text="Description")
                    tree_caveats.column('Description', anchor='w', width=100)
                    treescrollcaveats = ttk.Scrollbar(page13, command=tree_caveats.yview)
                    treescrollcaveats.configure(command=tree_caveats.yview)
                    tree_caveats.configure(yscrollcommand=treescrollcaveats.set)
                    treescrollcaveats.pack(side='right', fill='y')
                    for line in file_caveats.split("\n"):
                        item = line.split('=')
                        tree_caveats.insert("", 0, values=[item[0], item[1], item[2]])
                        print item[0], item[1], item[2]

                    tree_caveats.pack(expand=YES, fill=BOTH)


                elif "11.9" == version[:4]:
                    file_caveats = open("caveats_11.9.txt", 'r').read()
                    print " version match"
                    tree_caveats = ttk.Treeview(page13, height=20)
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")

                    tree_caveats.tag_configure("Treeview", background="black")
                    tree_caveats['columns'] = ('Identifier', 'Severity', 'Description')
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")
                    tree_caveats['show'] = 'headings'
                    tree_caveats.column("#0", width=50, anchor=Tkinter.W)
                    tree_caveats.heading("Identifier", text="Identifier")
                    tree_caveats.column('Identifier', anchor='center', width=100)
                    tree_caveats.heading("Severity", text="Severity")
                    tree_caveats.column('Severity', anchor='center', width=100)
                    tree_caveats.heading("Description", text="Description")
                    tree_caveats.column('Description', anchor='center', width=100)
                    treescrollcaveats = ttk.Scrollbar(page13, command=tree_caveats.yview)
                    treescrollcaveats.configure(command=tree_caveats.yview)
                    tree_caveats.configure(yscrollcommand=treescrollcaveats.set)
                    treescrollcaveats.pack(side='right', fill='y')
                    for line in file_caveats.split("\n"):
                        item = line.split('=')
                        tree_caveats.insert("", 0, values=[item[0], item[1], item[2]])
                        print item[0], item[1], item[2]

                    tree_caveats.pack(expand=YES, fill=BOTH)





                #caveats

            # file_11_8=open(manualobj.browseValue + "/caveats_11.8.txt", "r").read()
            # hyper_11_8 = open(manualobj.browseValue + "/hyperlink_11.8.txt", "r").read()
            # info = file_11_8.decode('cp1252').split('\n')
            # info_hyper = hyper_11_8.decode('cp1252').split('\n')



                ######About

            about = open("about.txt", "r").read()
            text = Text(page14, foreground="BLACK", width=110, height=15)
            scrollbar_about = Scrollbar(page14, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT,"IMPORTANT NOTICES AND DISCLAIMERS - PLEASE READ\n\n")
            text.insert(INSERT, about)
            text.insert(INSERT, "\n\n\n")
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbar_about.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_about.set


        elif manualobj.flag == 1:
            # adding Frames as pages for the ttk.Notebook
            # first page, which would get widgets gridded into it
            page1 = ttk.Frame(nb, borderwidth=110, width=1000, height=1000)
            page2 = ttk.Frame(nb, borderwidth=110, width=1000, height=1000)
            page3 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page4 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page5 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page6 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page7 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page8 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page9 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page10 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page11 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page12 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page13 = ttk.Frame(nb, borderwidth=110, width=200, height=500)

            nb.add(page11, text='Summary')
            nb.add(page1, text='System Details')
            nb.add(page2, text='User Details')
            #nb.add(page3, text='DNS Information')
            nb.add(page4, text='Service Profile')
            nb.add(page5, text='Devices')
            nb.add(page6, text='Jabber Config')
            nb.add(page7, text='Certificates')
            nb.add(page8, text='IM and Presence')

            nb.add(page9, text='Directory-cucm')

            nb.add(page10, text='SSO')

            nb.add(page12, text='Port Scanner')
            nb.add(page3, text='Open Caveats')
            nb.add(page13,text= "About")

            nb.pack(expand=1, fill="both")
            #############################################################################
            # dns
            ###########################################################################


                    #########################################################################################
                    # User Details
                    ########################################################################################

            userDetails = open(manualobj.browseValue + "/userdetails.txt", "r").read()
            tree_user = ttk.Treeview(page2, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            # ttk.Style().configure("Treeview.Heading", fieldbackground="black")
            # tree.columnconfigure("",'Port',background = "black")
            tree_user.tag_configure("Treeview", background="black")
            tree_user['columns'] = ('Attributes', 'Values')
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            # tree_user.heading("#0", text="")
            tree_user['show'] = 'headings'
            tree_user.column("#0", width=50, anchor=Tkinter.W)
            tree_user.heading("Attributes", text="Attributes")
            tree_user.column('Attributes', anchor='center', width=100)
            tree_user.heading("Values", text="Values")
            tree_user.column('Values', anchor='center', width=100)
            treescrolluser = ttk.Scrollbar(page2, command=tree_user.yview)
            treescrolluser.configure(command=tree_user.yview)
            tree_user.configure(yscrollcommand=treescrolluser.set)
            treescrolluser.pack(side='right', fill='y')
            att = re.findall(r'(.*?)=', userDetails, re.I | re.M)
            value = re.findall(r'=(.*?)\n', userDetails, re.I | re.M)
            index = 0

            # print("new123", att, " ",value)

            for line in att:
                if line != "serviceProfile":
                    tree_user.insert("", 0, values=[line, value[index]])
                    index += 1

            tree_user.pack(expand=YES, fill=BOTH)
            #################################################################################################
            # Service Profile
            ##################################################################################################
            ServicePro = open(manualobj.browseValue + "/service.txt", "r").read()
            tree_service = ttk.Treeview(page4, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_service.tag_configure("Treeview", background="black")
            tree_service['columns'] = ('Function', 'Server', 'Address', 'Port', 'Protocol')
            treescroll = ttk.Scrollbar(page4, command=tree_service.yview)
            treescroll.configure(command=tree_service.yview)
            tree_service.configure(yscrollcommand=treescroll.set)
            treescroll.pack(side='right', fill='y')

            # tree_dns.heading("#0", text="SRV")
            # tree_dns.column("#0", width=50, anchor=Tkinter.W)

            tree_service['show'] = 'headings'
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            tree_service.heading("Function", text="Function")
            tree_service.column('Function', anchor='center', width=100)

            tree_service.heading("Server", text="Server")
            tree_service.column('Server', anchor='center', width=100)

            tree_service.heading("Address", text="Address")
            tree_service.column('Address', anchor='center', width=100)

            tree_service.heading("Port", text="Port")
            tree_service.column('Port', anchor='center', width=100)

            tree_service.heading("Protocol", text="Protocol")
            tree_service.column('Protocol', anchor='center', width=100)

            tree_service.pack(expand=YES, fill=BOTH)

            treescroll = ttk.Scrollbar(page4, command=tree_service.yview)
            treescroll.configure(command=tree_service.yview)
            tree_service.configure(yscrollcommand=treescroll.set)
            treescroll.pack(side='right', fill='y')

            voice = re.findall(r'VoiceMail(.*?)\n', ServicePro, re.I | re.M)

            # tree_service.heading("#0", text="SRV")
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            # for line in voice :
            #     list_voice = line.split('')

            print(voice)

            tree_service.insert("", 0, values="Voicemail")
            for line in voice:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_service.insert("", 'end', values="Mailstore")

            mailstore = re.findall(r'MailStore(.*?)\n', ServicePro, re.I | re.M)
            for line in mailstore:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            Conferencing = re.findall(r'Conferencing(.*?)\n', ServicePro, re.I | re.M)

            tree_service.insert("", 'end', values="Conferencing")

            for line in Conferencing:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_service.insert("", 'end', values="Directory")

            directory = re.findall(r'Directory(.*?)\n', ServicePro, re.I | re.M)

            for line in directory:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_service.insert("", 'end', values="IMP")

            imp = re.findall(r'IMP(.*?)\n', ServicePro, re.I | re.M)

            for line in imp:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            cti = re.findall(r'CTI(.*?)\n', ServicePro, re.I | re.M)

            tree_service.insert("", 'end', values="CTI")

            for line in cti:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            vcs = re.findall(r'VCS(.*?)\n', ServicePro, re.I | re.M)

            tree_service.insert("", 'end', values="VCS")

            for line in vcs:
                item = line.split(':')
                tree_service.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])
            ##################################################################################
            # System Details
            #################################################################################

            sysdetails = open(manualobj.browseValue + "/sysdetails.txt", "r").read()

            scrollbary = Scrollbar(page1, orient=VERTICAL)
            text = Text(page1, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)

            text.config(state=NORMAL)
            text.insert(INSERT, sysdetails)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbary = Scrollbar(page1, orient=VERTICAL, command=text.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbary.set

            ###########################################################################
            # devices
            ##############################################################################
            final_dev = open(manualobj.browseValue + "/Final_devices.txt", "r").read()

            text = Text(page5, foreground="BLACK", width=110, height=15)
            scrollbar_devices = Scrollbar(page5, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, final_dev)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_devices.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_devices.set

            #####################################################################################
            # jabber config
            #####################################################################################
            jabber_config = open(manualobj.browseValue + "/jabber_config.txt", "r").read()
            jabber_config_local = open(manualobj.browseValue + "/jabber_local_config.txt", "r").read()
            text = Text(page6, foreground="BLACK", width=110, height=15)
            scrollbar_jabberconfig = Scrollbar(page6, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, jabber_config)
            text.insert(INSERT,"\n\n\n")
            text.insert(INSERT,jabber_config_local)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_jabberconfig.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_jabberconfig.set

            #################################################
            # IM&P
            ############################################
            imp_process = open(manualobj.browseValue + "\imp_login.txt", "r").read()

            scrollbary = Scrollbar(page8, orient=VERTICAL, command=text.yview)
            text = Text(page8, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)
            text.config(state=NORMAL)
            text.insert(INSERT, imp_process)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbary.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbary.set

            ##################################################
            # SSO
            ##################################################
            sso = open(manualobj.browseValue + "/sso_voicemail.txt", "r").read()
            sso_callmanager = open(manualobj.browseValue + "/sso_cucm.txt", 'r').read()
            sso_imp = open(manualobj.browseValue + "/sso_imp.txt", 'r').read()

            text = Text(page10, foreground="BLACK", width=110, height=15)
            scrollbar_sso = Scrollbar(page10, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)

            text.insert(INSERT, "CallManager\n")
            text.insert(END, "------------------------------------------------------------------------------\n")
            text.insert(INSERT, sso_callmanager)
            text.insert(END, "")
            # text.insert(END, "\n\n****************************************************************\n")
            text.insert(INSERT, "\n\nVoiceMail\n")
            text.insert(END, "------------------------------------------------------------------------------\n")
            text.insert(INSERT, sso)
            text.insert(END, "")
            text.insert(INSERT, "\n\nIMP\n")
            text.insert(END, "------------------------------------------------------------------------------\n")
            text.insert(INSERT, sso_imp)
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_sso.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_sso.set

            ########################################################################
            # Summary
            ########################################################################

            default = open(manualobj.browseValue + "/jabber_summary.txt", 'r').read()
            auth_summary = open(manualobj.browseValue + '\\authentication_summary.txt', 'r').read()
            cucm_service = open(manualobj.browseValue + '/cucmservicesummary.txt', 'r').read()
            imp_service = open(manualobj.browseValue + "/impservicesummary.txt", 'r').read()
            port = open(manualobj.browseValue + "/portsummary.txt", 'r').read()
            summary = open(manualobj.browseValue + "/summary.txt", 'r').read()
            impsummary = open(manualobj.browseValue + "/imp_summary.txt", 'r').read()
            fqdn = open(manualobj.browseValue + "/fqdn.txt", 'r').read()
            text = Text(page11, foreground="BLACK", width=110, height=15)
            def software_details():
                webbrowser.open_new(r'https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html')

            def port_details():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html")

            def parameters_reference_guide():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html")
            def ipv6():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_6/cjab_b_planning-guide-cisco-jabber-116/cjab_b_planning-guide-cisco-jabber-116_chapter_010.html#reference_AEEDA51FE1A43E22D7D7D90308568C19")

            text["yscrollcommand"] = scrollbary.set

            text.config(state=NORMAL)
            hyperlink = tkHyperlinkManager.HyperlinkManager(text)
            text.insert(INSERT,"-" * 50)
            text.insert(INSERT, "\n")
            text.insert(INSERT,"JABBER VALIDATION STATUS")
            text.insert(INSERT, "\n\n")
            text.insert(INSERT,"-" * 50)
            text.insert(INSERT, "\n\n")
            text.insert(INSERT, auth_summary)
            text.insert(END, "\n\n")
            text.insert(INSERT,
                        "\nThe following software(s) are either not supported or version is incompatible. Please refer to the ")
            text.insert(INSERT, "Release notes", hyperlink.add(software_details))
            text.insert(INSERT, "\n\n\n")
            text.insert(INSERT, summary + "\n")
            text.insert(INSERT,"Reference link IPv6", hyperlink.add(ipv6))
            text.insert(END, "\n\n")
            text.insert(INSERT, "Below are the Parameters which are having Non - default Values.Check the")
            text.insert(INSERT, " Parameters Reference Guide ", hyperlink.add(parameters_reference_guide))
            text.insert(INSERT, " for Cisco Jabber to evaluate if this impair Jabber features\n\n\n")
            text.insert(INSERT, default)
            text.insert(END, '\n\n')
            text.insert(INSERT,
                        "Following ports are not open which would affect the functionality of Jabber. Please refer ")
            text.insert(INSERT, "Ports and Protocols ", hyperlink.add(port_details))
            text.insert(INSERT, "section of Release notes for more details\n\n\n")
            text.insert(INSERT, port)
            text.insert(END, "\n\n")

            text.insert(INSERT, cucm_service)
            text.insert(INSERT,"\n\n")

            text.insert(INSERT, fqdn + " ")
            text.insert(END, "\n")


            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbar_summary = Scrollbar(page11, orient=VERTICAL, command=text.yview)
            text["yscrollcommand"] = scrollbar_summary.set
            scrollbar_summary.pack(side=RIGHT, fill=Y)
            scrollbary.pack(side=RIGHT, fill=Y)

            ####################################################################################
            # Directory cucm
            ####################################################################################
            file_dir_cucm = open(manualobj.browseValue + "/directory_cucm.txt", 'r').read()

            tree_dir_cucm = ttk.Treeview(page9, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_dir_cucm.tag_configure("Treeview", background="black")
            tree_dir_cucm['columns'] = ('Name', 'Values')
            treescrolldircucm = ttk.Scrollbar(page9, command=tree_dir_cucm.yview)
            treescrolldircucm.configure(command=tree_dir_cucm.yview)
            tree_dir_cucm.configure(yscrollcommand=treescrolldircucm.set)
            treescrolldircucm.pack(side='right', fill='y')

            tree_dir_cucm['show'] = 'headings'

            tree_dir_cucm.heading("Name", text="Name")
            tree_dir_cucm.column('Name', anchor='center', width=50)

            tree_dir_cucm.heading("Values", text="Values")
            tree_dir_cucm.column('Values', anchor='center', width=200)

            tree_dir_cucm.pack(expand=YES, fill=BOTH)

            # line = file_enterprise.split(':')
            index = 0

            file_dir_cucm = file_dir_cucm.split('\n')
            print("***")
            for line in file_dir_cucm:
                # print(line)
                item = line.split(':')
                print(item)
                x = len(item)
                index = 0
                # while index <= x :
                if x == 3:
                    tree_dir_cucm.insert("", 'end', values=[item[0], item[1], item[2]])
                elif x == 2:
                    tree_dir_cucm.insert("", 'end', values=[item[0], item[1]])
                    ##################################################################################
                    # Directory Imp
                    #################################################################################



                    ############################################################
                    # Port scan
                    #########################################################
            port_ = open(manualobj.browseValue + "/port_scan.txt", "r").read()

            tree_port = ttk.Treeview(page12, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_port.tag_configure("Treeview", background="black")
            tree_port['columns'] = ('Server', "Ip", 'Port', 'Status')

            tree_port['show'] = 'headings'
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            tree_port.heading("Server", text="Server")
            tree_port.column('Server', anchor='center', width=100)

            tree_port.heading("Ip", text="Ip")
            tree_port.column('Ip', anchor='center', width=100)

            tree_port.heading("Port", text="Port")
            tree_port.column('Port', anchor='center', width=100)

            tree_port.heading("Status", text="Status")
            tree_port.column('Status', anchor='center', width=100)

            treescrollport = ttk.Scrollbar(page12, command=tree_port.yview)
            treescrollport.configure(command=tree_port.yview)
            tree_port.configure(yscrollcommand=treescrollport.set)
            treescrollport.pack(side='right', fill='y')

            tree_port.pack(expand=YES, fill=BOTH)

            port = re.findall(r'CUCM(.*?)\n', port_, re.I | re.M)

            print(voice)

            tree_port.insert("", 0, values="CUCM")
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            port = re.findall(r'VOICEMAIL(.*?)\n', port_, re.I | re.M)

            tree_port.insert("", 'end', values="VOICEMAIL")
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            tree_port.insert("", 'end', values="IMP")

            port = re.findall(r'IMP(.*?)\n', port_, re.I | re.M)
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            ############################################################################
            # certificates
            ###########################################################################
            certificate_voice = open(manualobj.browseValue + "/certdatavoice.txt", "r").read()
            certificate_imp = open(manualobj.browseValue + "/certdataimp.txt", "r").read()
            certificate_cti = open(manualobj.browseValue + "/certdata.txt", 'r').read()
            trusted_cert = open(manualobj.browseValue + "/trusted certificates.txt", 'r').read()

            text = Text(page7, foreground="BLACK", width=110, height=15)
            scrollbar_certificates = Scrollbar(page7, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, "CUCM\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_cti)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(INSERT, "\n\nVOICEMAIL\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_voice)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(INSERT, "\n\nIM&P\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_imp)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(END, "")
            text.insert(INSERT, "\n\nTRUSTED CERTIFICATES\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, trusted_cert)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_certificates.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_certificates.set

            #Caveats

            # caveats = open(manualobj.browseValue + "/jabber_caveats.txt", "r").read()
            # scrollbary = Scrollbar(page3, orient=VERTICAL, command=text.yview)
            #
            # text = Text(page3, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)
            # text.config(state=NORMAL)
            # text.insert(INSERT, caveats)
            # text.insert(END, "")
            # text.config(state=DISABLED)
            # text.pack(side=LEFT, fill=BOTH, expand=YES)
            # scrollbary = Scrollbar(page3, orient=VERTICAL, command=text.yview)
            # scrollbary.pack(side=RIGHT, fill=Y)
            # text["yscrollcommand"] = scrollbary.set

            # hyperlink links
            # def a():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc87612")
            #
            # def b():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf31386")
            #
            # def c():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf24293")
            #
            # def d():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf26291")
            #
            # def e():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf32185")
            #
            # def f():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve57321")
            #
            # def g():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc40856")
            #
            # def h():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc70085")
            #
            # def i():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc71805")
            #
            # def j():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc72240")
            #
            # def k():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc79355")
            #
            # def l():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc86254")
            #
            # def m():
            #     webbrowser.open_new(r"https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvc99283")

            file_list_of_programs = open(manualobj.browseValue + "\\sysdetails.txt", 'r').read()
            file_jabber_caveats = open("jabber_caveats.txt", 'w')
            info = file_list_of_programs.split('\n')
            # hyperlink = tkHyperlinkManager.HyperlinkManager(text)
            version=0
            for row in info:
                if "Cisco Jabber" in row:
                    value = row

                    print value
                    list = value.split()
                    list = filter(None, list)
                    version = list[2]
                    print version
                    break
            if version!=0:
                if "11.8" == version[:4]:
                    file_caveats = open("caveats_11.8.txt",'r').read()
                    print " version match"
                    # i=1
                    # click={1:a,2:b,3:c,4:d,5:e,6:f,7:g,8:h,9:i,10:j,11:k,12:l,13:m}

                        # print row
                        # text.insert(INSERT, row)
                        #
                        # text.insert(INSERT, " " + "Click Here" , hyperlink.add(click[i]))
                        # text.insert(INSERT,"\n\n")
                        # i=i+1


                    tree_caveats = ttk.Treeview(page3, height=20)
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")

                    tree_caveats.tag_configure("Treeview", background="black")
                    tree_caveats['columns'] = ('Identifier', 'Severity' , 'Description')
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")
                    tree_caveats['show'] = 'headings'
                    tree_caveats.column("#0", width=50, anchor=Tkinter.W)
                    tree_caveats.heading("Identifier", text="Identifier")
                    tree_caveats.column('Identifier', anchor='center', width=100)
                    tree_caveats.heading("Severity", text="Severity")
                    tree_caveats.column('Severity', anchor='center', width=100)
                    tree_caveats.heading("Description", text="Description")
                    tree_caveats.column('Description', anchor='w', width=100)
                    treescrollcaveats = ttk.Scrollbar(page3, command=tree_caveats.yview)
                    treescrollcaveats.configure(command=tree_caveats.yview)
                    tree_caveats.configure(yscrollcommand=treescrollcaveats.set)
                    treescrollcaveats.pack(side='right', fill='y')
                    for line in file_caveats.split("\n"):
                        item = line.split('=')
                        tree_caveats.insert("", 0, values=[item[0], item[1], item[2]])
                        print item[0],item[1],item[2]


                    tree_caveats.pack(expand=YES, fill=BOTH)


                elif "11.9" == version[:4]:
                    file_caveats = open("caveats_11.9.txt", 'r').read()
                    print " version match"

                    tree_caveats = ttk.Treeview(page3, height=20)
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")

                    tree_caveats.tag_configure("Treeview", background="black")
                    tree_caveats['columns'] = ('Identifier', 'Severity', 'Description')
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")
                    tree_caveats['show'] = 'headings'
                    tree_caveats.column("#0", width=50, anchor=Tkinter.W)
                    tree_caveats.heading("Identifier", text="Identifier")
                    tree_caveats.column('Identifier', anchor='center', width=100)
                    tree_caveats.heading("Severity", text="Severity")
                    tree_caveats.column('Severity', anchor='center', width=100)
                    tree_caveats.heading("Description", text="Description")
                    tree_caveats.column('Description', anchor='center', width=100)
                    treescrollcaveats = ttk.Scrollbar(page3, command=tree_caveats.yview)
                    treescrollcaveats.configure(command=tree_caveats.yview)
                    tree_caveats.configure(yscrollcommand=treescrollcaveats.set)
                    treescrollcaveats.pack(side='right', fill='y')
                    for line in file_caveats.split("\n"):
                        item = line.split('=')
                        tree_caveats.insert("", 0, values=[item[0], item[1], item[2]])
                        print item[0], item[1], item[2]

                    tree_caveats.pack(expand=YES, fill=BOTH)

                # hyperlink links


                ######About

            about = open("about.txt", "r").read()
            text = Text(page13, foreground="BLACK", width=110, height=15)
            scrollbar_about = Scrollbar(page13, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, "IMPORTANT NOTICES AND DISCLAIMERS - PLEASE READ\n\n")
            text.insert(INSERT, about)
            text.insert(INSERT, "\n\n\n")
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbar_about.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_about.set







        else:
            # adding Frames as pages for the ttk.Notebook
            # first page, which would get widgets gridded into it
            page1 = ttk.Frame(nb, borderwidth=110, width=1000, height=1000)
            page2 = ttk.Frame(nb, borderwidth=110, width=1000, height=1000)
            page3 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page4 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page5 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page6 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page7 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page8 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page9 = ttk.Frame(nb, borderwidth=110, width=200, height=500)
            page10 = ttk.Frame(nb, borderwidth=110, width=200, height=500)


            nb.add(page2, text='Summary')
            nb.add(page1, text='System Details')
            # nb.add(page2, text='User Details')
            #nb.add(page2, text='DNS Information')
            # nb.add(page4, text='Service Profile')
            # nb.add(page4, text='Devices')
            # nb.add(page6, text='Jabber Config')
            nb.add(page4, text='Certificates')
            nb.add(page5, text='IM and Presence')
            nb.add(page6, text='IMP Service Profile')
            nb.add(page7, text='IMP Enterprise Parameters')
            # nb.add(page11, text='Directory-cucm')
            nb.add(page8, text='Directory IM&P')
            # nb.add(page9, text='SSO')

            nb.add(page9, text='Port Scanner')
            nb.add(page3, text='Open Caveats')
            nb.add(page10, text = "About")
            # uiobj.nb.add(uiobj.page9, text='Port Scanner')
            nb.pack(expand=1, fill="both")


                    #########################################################################################
                    # User Details
                    ########################################################################################

            ##################################################################################
            # System Details
            #################################################################################

            sysdetails = open(manualobj.browseValue + "/sysdetails.txt", "r").read()

            scrollbary = Scrollbar(page1)
            scrollbary = Scrollbar(page1, orient=VERTICAL)
            text = Text(page1, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)
            text.config(state=NORMAL)
            text.insert(INSERT, sysdetails)
            text.insert(END, "")
            text.config(state=DISABLED)

            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbary.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbary.set



            #################################################################################
            # IMP service profile
            ################################################################################

            # file_enterprise = open("c:/Python27/imp_enterprise.txt","r").read()
            file_service_imp = open(manualobj.browseValue + "/imp_jabber.txt", "r").read()
            # imp_serv = open("C:\Python27\service.txt", "r").read()
            tree_imp_jabber = ttk.Treeview(page6, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_imp_jabber.tag_configure("Treeview", background="black")
            tree_imp_jabber['columns'] = ('Function', 'Server', 'Address', 'Port', 'Protocol')
            treescrollimp = ttk.Scrollbar(page6, command=tree_imp_jabber.yview)
            treescrollimp.configure(command=tree_imp_jabber.yview)
            tree_imp_jabber.configure(yscrollcommand=treescrollimp.set)
            treescrollimp.pack(side='right', fill='y')

            tree_imp_jabber['show'] = 'headings'
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            tree_imp_jabber.heading("Function", text="Function")
            tree_imp_jabber.column('Function', anchor='center', width=100)

            tree_imp_jabber.heading("Server", text="Server")
            tree_imp_jabber.column('Server', anchor='center', width=100)

            tree_imp_jabber.heading("Address", text="Address")
            tree_imp_jabber.column('Address', anchor='center', width=100)

            tree_imp_jabber.heading("Port", text="Port")
            tree_imp_jabber.column('Port', anchor='center', width=100)

            tree_imp_jabber.heading("Protocol", text="Protocol")
            tree_imp_jabber.column('Protocol', anchor='center', width=100)

            tree_imp_jabber.pack(expand=YES, fill=BOTH)

            voice = re.findall(r'VoiceMail(.*?)\n', file_service_imp, re.I | re.M)
            tree_imp_jabber.insert("", 0, values="Voicemail")
            for line in voice:
                item = line.split(':')
                tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_imp_jabber.insert("", 'end', values="Mailstore")

            mailstore = re.findall(r'MailStore(.*?)\n', file_service_imp, re.I | re.M)
            for line in mailstore:
                item = line.split(':')
                tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            Conferencing = re.findall(r'Conferencing(.*?)\n', file_service_imp, re.I | re.M)

            tree_imp_jabber.insert("", 'end', values="Conferencing")

            for line in Conferencing:
                item = line.split(':')
                tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_imp_jabber.insert("", 'end', values="Directory")

            directory = re.findall(r'Directory(.*?)\n', file_service_imp, re.I | re.M)

            for line in directory:
                item = line.split(':')
                tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tree_imp_jabber.insert("", 'end', values="IMP")

            imp = re.findall(r'IMP(.*?)\n', file_service_imp, re.I | re.M)

            for line in imp:
                item = line.split(':')
                tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            cti = re.findall(r'CTI(.*?)\n', file_service_imp, re.I | re.M)

            tree_imp_jabber.insert("", 'end', values="CTI")

            for line in cti:
                item = line.split(':')
                tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            tftp = re.findall(r'TFTP(.*?)\n', file_service_imp, re.I | re.M)

            tree_imp_jabber.insert("", 'end', values="TFTP")

            for line in tftp:
                item = line.split(':')
                tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

            vcs = re.findall(r'VCS(.*?)\n', file_service_imp, re.I | re.M)

            tree_imp_jabber.insert("", 'end', values="VCS")

            for line in vcs:
                item = line.split(':')
                len_item = len(item)
                if len_item != 0:
                    tree_imp_jabber.insert("", 'end', values=[item[0], item[1], item[2], item[3], item[4]])

                    ################################################################################################
                    # service enterprise
                    ################################################################################################
            file_enterprise = open(manualobj.browseValue + "/imp_enterprise.txt", "r").read()
            tree_imp_enterprise = ttk.Treeview(page7, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_imp_enterprise.tag_configure("Treeview", background="black")
            tree_imp_enterprise['columns'] = ('Name', 'Attributes')
            treescrollenter = ttk.Scrollbar(page7, command=tree_imp_enterprise.yview)
            treescrollenter.configure(command=tree_imp_enterprise.yview)
            tree_imp_enterprise.configure(yscrollcommand=treescrollenter.set)
            treescrollenter.pack(side='right', fill='y')

            tree_imp_enterprise['show'] = 'headings'

            tree_imp_enterprise.heading("Name", text="Name")
            tree_imp_enterprise.column('Name', anchor='center', width=100)

            tree_imp_enterprise.heading("Attributes", text="Attributes")
            tree_imp_enterprise.column('Attributes', anchor='center', width=100)

            tree_imp_enterprise.pack(expand=YES, fill=BOTH)

            # line = file_enterprise.split(':')
            index = 0

            print(file_enterprise)
            file_enterprise = file_enterprise.split('\n')
            print("***")
            for line in file_enterprise:
                # print(line)
                item = line.split(':')
                print(item)
                x = len(item)
                index = 0

                if x == 3:
                    tree_imp_enterprise.insert("", 'end', values=[item[0], item[1], item[2]])
                elif x == 2:
                    tree_imp_enterprise.insert("", 'end', values=[item[0], item[1]])

                    #################################################
                    # IM&P
                    ############################################
            imp_process = open(manualobj.browseValue + "\imp_login.txt", "r").read()

            scrollbary = Scrollbar(page5)

            text = Text(page5, foreground="BLACK", yscrollcommand=scrollbary.set, width=110, height=15)
            text.config(state=NORMAL)
            text.insert(INSERT, imp_process)
            text.insert(END, "")
            text.config(state=DISABLED)
            scrollbary = Scrollbar(page5, orient=VERTICAL)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbary.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbary.set



            ########################################################################
            # Summary
            ########################################################################

            default = open(manualobj.browseValue + "/jabber_summary.txt", 'r').read()
            auth_summary = open(manualobj.browseValue + '\\authentication_summary.txt', 'r').read()
            cucm_service = open(manualobj.browseValue + '/cucmservicesummary.txt', 'r').read()
            imp_service = open(manualobj.browseValue + "/impservicesummary.txt", 'r').read()
            port = open(manualobj.browseValue + "/portsummary.txt", 'r').read()
            summary = open(manualobj.browseValue + "/summary.txt", 'r').read()
            impsummary = open(manualobj.browseValue + "/imp_summary.txt", 'r').read()
            fqdn = open(manualobj.browseValue + "/fqdn.txt", 'r').read()
            text = Text(page2, foreground="BLACK", width=110, height=15)

            def software_details():
                webbrowser.open_new(r'https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html')

            def port_details():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-release-notes-list.html")

            def parameters_reference_guide():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html")
            def ipv6():
                webbrowser.open_new(r"https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_6/cjab_b_planning-guide-cisco-jabber-116/cjab_b_planning-guide-cisco-jabber-116_chapter_010.html#reference_AEEDA51FE1A43E22D7D7D90308568C19")

            text["yscrollcommand"] = scrollbary.set

            text.config(state=NORMAL)
            hyperlink = tkHyperlinkManager.HyperlinkManager(text)
            text.insert(INSERT,"-"*50)
            text.insert(INSERT, "\n")
            text.insert(INSERT,"JABBER VALIDATION STATUS")
            text.insert(INSERT, "\n\n")
            text.insert(INSERT,"-" * 50)
            text.insert(INSERT, "\n\n")
            text.insert(INSERT, auth_summary)
            text.insert(END, "\n\n")
            text.insert(INSERT,"\nThe following software(s) are either not supported or version is incompatible with Jabber. Please refer to the ")
            text.insert(INSERT, "Release notes", hyperlink.add(software_details))
            text.insert(INSERT, "\n\n\n")
            text.insert(INSERT, summary+"\n")
            text.insert(INSERT,"Reference link IPv6", hyperlink.add(ipv6))
            text.insert(END, "\n\n")
            text.insert(INSERT, "Below are the Parameters which are not having default Values.Check the")
            text.insert(INSERT, " Parameters Reference Guide ", hyperlink.add(parameters_reference_guide))
            text.insert(INSERT, " for Cisco Jabber to evaluate if this impair Jabber features \n\n\n")
            text.insert(INSERT, default)
            text.insert(END, '\n\n')
            text.insert(INSERT,
                        "Following ports are not open which would affect the functionality of Jabber. Please refer ")
            text.insert(INSERT, "Ports and Protocols ", hyperlink.add(port_details))
            text.insert(INSERT, "section of Release notes for more details\n\n\n")
            text.insert(INSERT, port)
            text.insert(END, "\n\n")

            text.insert(INSERT, imp_service)

            text.insert(INSERT, fqdn + " ")
            text.insert(END, "\n")


            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbar_summary = Scrollbar(page2, orient=VERTICAL, command=text.yview)
            text["yscrollcommand"] = scrollbar_summary.set
            scrollbar_summary.pack(side=RIGHT, fill=Y)
            scrollbary.pack(side=RIGHT, fill=Y)

            #         ##################################################################################
            #         # Directory Imp
            #         #################################################################################
            #
            file_dir_imp = open(manualobj.browseValue + "/directory_imp.txt", 'r').read()

            tree_dir_imp = ttk.Treeview(page8, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_dir_imp.tag_configure("Treeview", background="black")
            tree_dir_imp['columns'] = ('Name', 'Values')
            treescrolldirimp = ttk.Scrollbar(page8, command=tree_dir_imp.yview)
            treescrolldirimp.configure(command=tree_dir_imp.yview)
            tree_dir_imp.configure(yscrollcommand=treescrolldirimp.set)
            treescrolldirimp.pack(side='right', fill='y')

            tree_dir_imp['show'] = 'headings'

            tree_dir_imp.heading("Name", text="Name")
            tree_dir_imp.column('Name', anchor='center', width=100)

            tree_dir_imp.heading("Values", text="Values")
            tree_dir_imp.column('Values', anchor='center', width=100)

            tree_dir_imp.pack(expand=YES, fill=BOTH)

            # line = file_enterprise.split(':')
            index = 0

            file_dir_imp = file_dir_imp.split('\n')
            print("***")
            for line in file_dir_imp:
                # print(line)
                item = line.split(':')
                print(item)
                x = len(item)
                index = 0
                # while index <= x :
                if x == 3:
                    tree_dir_imp.insert("", 'end', values=[item[1], item[2]])
                elif x == 2:
                    tree_dir_imp.insert("", 'end', values=[item[1], item[2]])






                    ############################################################
                    # Port scan
                    #########################################################
            port_ = open(manualobj.browseValue + "/port_scan.txt", "r").read()

            tree_port = ttk.Treeview(page9, height=20)
            ttk.Style().configure("TreeView", background="gainsboro",
                                  foreground="black", fieldbackground="red")
            tree_port.tag_configure("Treeview", background="black")
            tree_port['columns'] = ('Server', "Ip", 'Port', 'Status')

            tree_port['show'] = 'headings'
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            tree_port.heading("Server", text="Server")
            tree_port.column('Server', anchor='center', width=100)

            tree_port.heading("Ip", text="Ip")
            tree_port.column('Ip', anchor='center', width=100)

            tree_port.heading("Port", text="Port")
            tree_port.column('Port', anchor='center', width=100)

            tree_port.heading("Status", text="Status")
            tree_port.column('Status', anchor='center', width=100)

            treescrollport = ttk.Scrollbar(page9, command=tree_port.yview)
            treescrollport.configure(command=tree_port.yview)
            tree_port.configure(yscrollcommand=treescrollport.set)
            treescrollport.pack(side='right', fill='y')

            tree_port.pack(expand=YES, fill=BOTH)

            port = re.findall(r'CUCM(.*?)\n', port_, re.I | re.M)

            # tree_service.heading("#0", text="SRV")
            # tree_service.column("#0", width=50, anchor=Tkinter.W)

            # for line in voice :
            #     list_voice = line.split('')

            print(voice)

            tree_port.insert("", 0, values="CUCM")
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            port = re.findall(r'VOICEMAIL(.*?)\n', port_, re.I | re.M)

            tree_port.insert("", 'end', values="VOICEMAIL")
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            tree_port.insert("", 'end', values="IMP")

            port = re.findall(r'IMP(.*?)\n', port_, re.I | re.M)
            for line in port:
                item = line.split(':')
                print("item", item[1])
                tree_port.insert("", 'end', values=[item[0], item[1], item[2], item[3]])

            treescrollport = ttk.Scrollbar(page9, command=tree_port.yview)
            treescrollport.configure(command=tree_port.yview)
            tree_port.configure(yscrollcommand=treescrollport.set)
            treescrollport.pack(side='right', fill='y')

            ############################################################################
            # certificates
            ###########################################################################
            certificate_voice = open(manualobj.browseValue + "/certdatavoice.txt", "r").read()
            certificate_imp = open(manualobj.browseValue + "/certdataimp.txt", "r").read()
            certificate_cti = open(manualobj.browseValue + "/certdata.txt", 'r').read()
            trusted_cert = open(manualobj.browseValue + "/trusted certificates.txt", 'r').read()

            text = Text(page4, foreground="BLACK", width=110, height=15)
            scrollbar_certificates = Scrollbar(page4, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, "CUCM\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_cti)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(INSERT, "\n\nVOICEMAIL\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_voice)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(INSERT, "\n\nIM&P\n\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, certificate_imp)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.insert(END, "")
            text.insert(INSERT, "\n\nTRUSTED CERTIFICATES\n")
            text.insert(END, "-" * 50 + "\n\n")
            text.insert(INSERT, trusted_cert)
            text.insert(INSERT, "\n\n" + "-" * 50)
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)

            scrollbar_certificates.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_certificates.set

            file_list_of_programs = open(manualobj.browseValue + "\\sysdetails.txt", 'r').read()
            file_jabber_caveats = open(manualobj.browseValue + "\\jabber_caveats.txt", 'w')
            info = file_list_of_programs.split('\n')
            # hyperlink = tkHyperlinkManager.HyperlinkManager(text)
            for row in info:
                if "Cisco Jabber" in row:
                    value = row
                    print value
                    list = value.split()
                    list = filter(None, list)
                    version = list[2]
                    print version
                    break
            if version!=0:
                if "11.8" == version[:4]:
                    file_caveats = open("caveats_11.8.txt", 'r').read()
                    print " version match"
                    # i=1
                    # click={1:a,2:b,3:c,4:d,5:e,6:f,7:g,8:h,9:i,10:j,11:k,12:l,13:m}

                    # print row
                    # text.insert(INSERT, row)
                    #
                    # text.insert(INSERT, " " + "Click Here" , hyperlink.add(click[i]))
                    # text.insert(INSERT,"\n\n")
                    # i=i+1


                    tree_caveats = ttk.Treeview(page3, height=20)
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")

                    tree_caveats.tag_configure("Treeview", background="black")
                    tree_caveats['columns'] = ('Identifier', 'Severity', 'Description')
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")
                    tree_caveats['show'] = 'headings'
                    tree_caveats.column("#0", width=50, anchor=Tkinter.W)
                    tree_caveats.heading("Identifier", text="Identifier")
                    tree_caveats.column('Identifier', anchor='center', width=100)
                    tree_caveats.heading("Severity", text="Severity")
                    tree_caveats.column('Severity', anchor='center', width=100)
                    tree_caveats.heading("Description", text="Description")
                    tree_caveats.column('Description', anchor='w', width=100)
                    treescrollcaveats = ttk.Scrollbar(page3, command=tree_caveats.yview)
                    treescrollcaveats.configure(command=tree_caveats.yview)
                    tree_caveats.configure(yscrollcommand=treescrollcaveats.set)
                    treescrollcaveats.pack(side='right', fill='y')
                    for line in file_caveats.split("\n"):
                        item = line.split('=')
                        tree_caveats.insert("", 0, values=[item[0], item[1], item[2]])
                        print item[0], item[1], item[2]

                    tree_caveats.pack(expand=YES, fill=BOTH)


                elif "11.9" == version[:4]:
                    file_caveats = open("caveats_11.9.txt", 'r').read()
                    print " version match"

                    tree_caveats = ttk.Treeview(page3, height=20)
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")

                    tree_caveats.tag_configure("Treeview", background="black")
                    tree_caveats['columns'] = ('Identifier', 'Severity', 'Description')
                    ttk.Style().configure("TreeView", background="gainsboro",
                                          foreground="black", fieldbackground="red")
                    tree_caveats['show'] = 'headings'
                    tree_caveats.column("#0", width=50, anchor=Tkinter.W)
                    tree_caveats.heading("Identifier", text="Identifier")
                    tree_caveats.column('Identifier', anchor='center', width=100)
                    tree_caveats.heading("Severity", text="Severity")
                    tree_caveats.column('Severity', anchor='center', width=100)
                    tree_caveats.heading("Description", text="Description")
                    tree_caveats.column('Description', anchor='w', width=100)
                    treescrollcaveats = ttk.Scrollbar(page3, command=tree_caveats.yview)
                    treescrollcaveats.configure(command=tree_caveats.yview)
                    tree_caveats.configure(yscrollcommand=treescrollcaveats.set)
                    treescrollcaveats.pack(side='right', fill='y')
                    for line in file_caveats.split("\n"):
                        item = line.split('=')
                        tree_caveats.insert("", 0, values=[item[0], item[1], item[2]])
                        print item[0], item[1], item[2]

                    tree_caveats.pack(expand=YES, fill=BOTH)

                ######About

            about = open("about.txt", "r").read()
            text = Text(page10, foreground="BLACK", width=110, height=15)
            scrollbar_about = Scrollbar(page10, orient=VERTICAL, command=text.yview)
            text.config(state=NORMAL)
            text.insert(INSERT, "IMPORTANT NOTICES AND DISCLAIMERS - PLEASE READ\n\n")
            #text.insert(INSERT, about)
            text.insert(INSERT, "\n\n\n")
            text.insert(END, "")
            text.config(state=DISABLED)
            text.pack(side=LEFT, fill=BOTH, expand=YES)
            scrollbar_about.pack(side=RIGHT, fill=Y)
            text["yscrollcommand"] = scrollbar_about.set


        root.mainloop()

        #         #
        # uirun = RunnerUI()
        # uirun.MainApp()
        # #demo()