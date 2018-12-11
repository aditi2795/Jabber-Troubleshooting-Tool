import subprocess
import socket
import time
from ManualLogin import *
import requests
from xml.dom import minidom
import shlex
import logging


class dnsclass:
    def dns_fn(self):
        try:
            FILE_LOG = open(manualobj.browseValue+'Logs.log',"w")
            FILE_LOG.write("")
            file_status= open(manualobj.browseValue+'/dns_status.txt',"w")
            logging.basicConfig(filename=manualobj.browseValue + '/Logs.log', level=logging.DEBUG)
            output = subprocess.check_output("ipconfig /all", shell=True)
            domain = ""
            flag = 0
            file_dns = open(manualobj.browseValue+"/dns.txt", "w+")
            for row in output.split('\n'):
                if "Primary Dns Suffix" in row:
                    domain = row.split(': ')[1]
                    domain = domain.split('\r')[0]
                    dnsobject.domain = domain
                    flag = 1
                    logging.debug("Domain is present")
                    break
                else:
                    flag = 0

            file_dns.write(str(flag)+"\n")
            file_dns.write(str(domain)+"\n")
            if flag== 0 :
                logging.error("Domain is not there")

        except Exception as e:
            logging.error(str(e))
            print ("Error in dns")
            return

        if manualobj.flag == 0:
            if flag == 1:

                try:
                    command = "nslookup -q=SRV _cisco-uds._tcp." + domain
                    c=0
                    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = p.communicate()
                    # if running on Windows, split for ("\r\n")
                    for line in out.split("\n"):

                        if "priority" in line:
                            uds_priority = line.split("=")[1]
                            print uds_priority
                            c=1
                        if "weight" in line:
                            uds_weight = line.split("=")[1]
                        if "port" in line:
                            print line
                            uds_port = line.split("=")[1]
                        if "svr hostname" in line:
                            uds_hostName = line.split("=")[1]
                            i = uds_hostName.split()
                            uds_ip = socket.gethostbyname(i[0])
                            dnsobject.uds=uds_ip
                            print uds_ip
                            file_dns.write("\n_cisco-uds._tcp.:SRV:" + str(uds_hostName) + ":" + str(uds_port) + ":" + str(
                                uds_weight) + ":" + str(uds_priority) + ":" + str(uds_ip)+"\n")

                    if c!=1:
                        logging.debug("_cisco-uds._tcp.NO RECORDS FOUND")
                        file_dns.write("\n_cisco-uds._tcp.:SRV:NO RECORDS FOUND\n")
                    else :
                        logging.debug("_cisco-uds._tcp.RECORDS FOUND")

                except Exception as e:
                    logging.error(str(e))
                    file_dns.write("\n_cisco-uds._tcp.:SRV:NO RECORDS FOUND\n")
                    dnsobject.uds=""

                try:
                    command = "nslookup -q=SRV _cuplogin._tcp." + domain
                    b=0
                    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = p.communicate()
                    # if running on Windows, split for ("\r\n")
                    for line in out.split("\n"):

                        if "priority" in line:
                            cup_priority = line.split("=")[1]
                            b=1

                        if "weight" in line:
                            cup_weight = line.split("=")[1]
                        if "port" in line:
                            print line
                            cup_port = line.split("=")[1]
                        if "svr hostname" in line:
                            cup_hostName = line.split("=")[1]
                            i = cup_hostName.split()
                            cup_ip = socket.gethostbyname(i[0])
                            print cup_ip
                            file_dns.write("\n_cuplogin._tcp.:SRV:" + str(cup_hostName) + ":" + str(cup_port) + ":" + str(
                                cup_weight) + ":" + str(cup_priority) + ":" + str(cup_ip)+"\n")

                    if b!=1:
                        logging.debug("_cuplogin._tcp. NO RECORDS FOUND")
                        file_dns.write(
                            "\n_cuplogin._tcp.:SRV:NO RECORDS FOUND\n")
                    else :
                        logging.debug("_cuplogin._tcp. RECORDS FOUND")

                except Exception as e:
                    logging.error(str(e))
                    file_dns.write(
                        "\n_cuplogin._tcp.:SRV:NO RECORDS FOUND\n")

                try:
                    command = "nslookup -q=SRV _collab._tcp." + domain
                    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = p.communicate()
                    a1=0
                    a2=0
                    # if running on Windows, split for ("\r\n")
                    for line in out.split("\n"):


                        if "priority" in line:
                            col_priority = line.split("=")[1]
                            a=1

                        if "weight" in line:
                            col_weight = line.split("=")[1]
                        if "port" in line:
                            print line
                            col_port = line.split("=")[1]
                        if "svr hostname" in line:
                            col_hostName = line.split("=")[1]
                            i = col_hostName.split()
                            col_ip = socket.gethostbyname(i[0])
                            print col_ip
                            file_dns.write("\n_collab-edge_tcp:SRV:" + str(col_hostName) + ":" + str(col_port) + ":" + str(
                                col_weight) + ":" + str(col_priority) + ":" + str(col_ip)+"\n")

                    if a!=1:
                        logging.debug("_collab-edge_tcp NO RECORDS FOUND")
                        file_dns.write("\n_collab-edge_tcp:SRV:NO RECORDS FOUND\n")
                    else :
                        logging.debug("_collab-edge_tcp RECORDS FOUND")


                except Exception as e :
                    logging.error(str(e))
                    file_dns.write("\n_collab-edge_tcp:SRV:NO RECORDS FOUND\n")
                try:
                    command = "nslookup -q=SRV _ldap._tcp." + domain
                    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = p.communicate()
                    e=0
                    # if running on Windows, split for ("\r\n")
                    for line in out.split("\n"):

                        if "priority" in line:
                            ld_priority = line.split("=")[1]
                            print ld_priority
                        if "weight" in line:
                            ld_weight = line.split("=")[1]
                        if "port" in line:
                            print line
                            e=1
                            ld_port = line.split("=")[1]
                        if "svr hostname" in line:
                            ld_hostName = line.split("=")[1]
                            i = ld_hostName.split()
                            ld_ip = socket.gethostbyname(i[0])
                            print ld_ip
                            file_dns.write("\n_gc._tcp.:SRV:" + str(ld_hostName) + ":" + str(ld_port) + ":" + str(
                                ld_weight) + ":" + str(ld_priority) + ":" + str(ld_ip)+"\n")

                    if e!=1:
                         file_dns.write(
                             "\n_ldap._tcp.:SRV:NO RECORDS FOUND\n")
                         logging.debug("_ldap._tcp.NO RECORDS FOUND")
                    else :
                        logging.debug("_ldap._tcp. RECORDS FOUND")


                except Exception as e:
                    file_dns.write(
                        "\n_ldap._tcp.:SRV:NO RECORDS FOUND\n")
                    logging.error(str(e))

                try:
                    command = "nslookup -q=SRV _gc._tcp." + domain
                    d=0
                    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = p.communicate()
                    # if running on Windows, split for ("\r\n")
                    for line in out.split("\n"):

                        if "priority" in line:
                            gc_priority = line.split("=")[1]

                        if "weight" in line:
                            d=1
                            gc_weight = line.split("=")[1]
                        if "port" in line:
                            print line
                            gc_port = line.split("=")[1]
                        if "svr hostname" in line:
                            gc_hostName = line.split("=")[1]
                            i = gc_hostName.split()
                            gc_ip = socket.gethostbyname(i[0])
                            print gc_ip
                            file_dns.write("\n_ldap._tcp.:SRV:" + str(gc_hostName) + ":" + str(gc_port) + ":" + str(
                                gc_weight) + ":" + str(gc_priority) + ":" + str(gc_ip)+"\n")



                    if d!=1:
                        file_dns.write("\n_gc._tcp.:SRV:NO RECORDS FOUND\n")
                    else  :
                        logging.debug("_gc._tcp. RECORDS FOUND")

                except:
                    file_dns.write("\n_gc._tcp.:SRV:NO RECORDS FOUND\n")
            else:
                #logging.error("Domain is not there")
                file_dns.write("NO DOMAIN FOUND\n")
                file_dns.write("_cisco-uds._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")
                file_dns.write("_cuplogin._tcp.:SRV:NO RECORDS FOUND:-:-:-:\n")
                file_dns.write("_collab-edge_tcp:SRV:NO RECORDS FOUND:-:-:-::\n")
                file_dns.write("_gc._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")
                file_dns.write("_ldap._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")

        elif manualobj.flag == 1:
            dnsobject.uds = manualobj.server

            file_dns.write("_cisco-uds._tcp.:SRV:hostname:-:-:-:" + str(manualobj.server) + "\n")
            file_dns.write("_cuplogin._tcp.:SRV:NO RECORDS FOUND:-:-:-:\n")
            file_dns.write("_collab-edge_tcp:SRV:NO RECORDS FOUND:-:-:-::\n")
            file_dns.write("_gc._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")
            file_dns.write("_ldap._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")
        elif manualobj.flag == 2:
            fileimp=open(manualobj.browseValue+"/impmanualip.txt",'w+')
            dnsobject.impip = manualobj.server_imp
            fileimp.write(dnsobject.impip)
            file_dns.write("_cisco-uds._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")
            file_dns.write("_cuplogin._tcp.:SRV:hostname:-:-:-:" + str(manualobj.server_imp) + "\n")
            file_dns.write("_collab-edge_tcp:SRV:NO RECORDS FOUND:-:-:-::\n")
            file_dns.write("_gc._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")
            file_dns.write("_ldap._tcp.:SRV:NO RECORDS FOUND:-:-:-::\n")
        try:
            dnsobject.server = dnsobject.uds
            response = requests.get("https://"+dnsobject.server+"/cucm-uds/servers",verify=False)
            filex=open(manualobj.browseValue+"/servers.xml",'w+')
            filex.write(response.text)
            filex.close()

            servers = minidom.parse(manualobj.browseValue+"/servers.xml")


            server=servers.getElementsByTagName("server")
            serverslength = server.length
            print serverslength
            filey=open(manualobj.browseValue+"/server.txt",'w+')
            for j in range(serverslength):
                filey.write(servers.getElementsByTagName("server")[j].firstChild.data+"\n")
            filey.close()

            dnsobject.serv = []
            filez=open(manualobj.browseValue+"/server.txt",'r').read()
            for row in filez.split('\n'):
                dnsobject.serv.append(row)
            dnsobject.serv= filter(lambda name: name.strip(),dnsobject.serv)
            print dnsobject.serv
            file_status.write("dns_success")

        except:
             dnsobject.server=""
             file_status.write("dns_fail")


start = time.time()
dnsobject = dnsclass()

#dnsobject.dns_fn()
# dnsobject.file = open('c:\Python27\dns.txt', 'r').read()
# if __name__ == "__main__":
#     print("TIME TAKEN ", time, "**")
#     # dnsobject.dns_fn()
#     time = time.time() - start
#     print(time)