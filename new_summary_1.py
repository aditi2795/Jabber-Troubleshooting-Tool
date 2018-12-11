from ManualLogin import *
class new_summaryclass():
    def new_summaryfn(self):
        dns_file= open(manualobj.browseValue + "/dns.txt",'r').read()
        userdetails_file=open(manualobj.browseValue + "/userdetails_status.txt",'r').read()
        serviceprofile_file = open(manualobj.browseValue + '/serviceprofile_status.txt', "r").read()
        imp_file = open(manualobj.browseValue + '/imp_status.txt', "r").read()
        jabber_config_file= open(manualobj.browseValue + '/jabber_config_status.txt','r').read()
        voice_file = open(manualobj.browseValue + "/voice_status.txt", 'r').read()
        file_new_summary=open(manualobj.browseValue + '/authentication_summary.txt', "w")
        enable_imp_file=open(manualobj.browseValue + '/userdetails.txt','r').read()
        if manualobj.flag==0:
            dnsinfo1 = dns_file.split('\n')
            dnsinfo2 = dns_file.split('\n')
            print dnsinfo1
            uds=0
            cup=0
            for row in dnsinfo1:
                print row
                if "_cisco-uds._tcp.:SRV:NO RECORDS FOUND" in row:
                    uds=1
                    break
            for row in dnsinfo2:
                if "_cuplogin._tcp.:SRV:NO RECORDS FOUND" in row:
                       cup=1
                       break

            print uds,cup,"uds andcup"

            if uds==1 and cup==1:
                file_new_summary.write("DNS"+(50-len('DNS'))*" "+": UDS AND CUP FAILED\n")
            elif uds==0 and cup==1:
                file_new_summary.write("DNS"+(50-len('DNS'))*" "+": UDS passed AND CUP FAILED\n")
            elif uds==1 and cup==0:
                file_new_summary.write("DNS"+(50-len('DNS'))*" "+": UDS FAILED AND CUP PASSED\n")
            elif uds==0 and cup==0:
                file_new_summary.write("DNS"+(50-len('DNS'))*" "+": PASSED\n")
        if manualobj.flag!=2:
            userdetailsinfo = userdetails_file.split('\n')
            for row in userdetailsinfo:
                if "userdetails_success" in row:
                    file_new_summary.write("Communications Manager Authentication"+(50-len("Communications Manager Authentication"))*" "+": Passed\n")
                    break
                elif "authentication_fail" in row:
                    file_new_summary.write("Communications Manager Authentication"+(50-len("Communications Manager Authentication"))*" "+": Failed\n")
                    break
                else:
                    file_new_summary.write("Communications Manager Authentication"+(50-len("Communications Manager Authentication"))*" "+": Unable to contact server\n")
                    break

            voiceinfo = voice_file.split('\n')
            for row in voiceinfo:
                if "voicemail_success" in row:
                    file_new_summary.write("Voicemail" + (50 - len('Voicemail')) * " " + ": Passed\n")
                    break
                elif "voicemail_fail" in row:
                    file_new_summary.write(
                        "Voicemail" + (50 - len('voicemail')) * " " + ": Unable to reach the server\n")
                    break

                else:
                    file_new_summary.write(
                        "Voicemail" + (50 - len('voicemail')) * " " + ": Unable to reach the server\n")
                    break

            enable_flag = 0
            enableinfo = enable_imp_file.split('\n')
            for row in enableinfo:
                if "enable" in row:
                    row = row.split('=')
                    row1 = row[1]
                    enable_flag = 1
                    if str(row1) == "true":
                        file_new_summary.write(
                            "User Enabled for Presence" + (50 - len('user enabled for presence')) * " " + ": TRUE\n")
                        break
                    else:
                        file_new_summary.write(
                            "User Enabled for Presence" + (50 - len('user enabled for presence')) * " " + ": FALSE\n")
                        break
            if enable_flag == 0:
                file_new_summary.write(
                    "User Enabled for Presence" + (50 - len('user enabled for presence')) * " " + ": FALSE\n")

        impinfo = imp_file.split('\n')
        for row in impinfo:
            if "imp_success" in row:
                file_new_summary.write("IM and Presence Authentication"+(50-len("IM and Presence Authentication"))*" "+": Passed\n")
                break
            elif "imp_unreachable" in row:
                file_new_summary.write("IM and Presence Authentication" + (
                50 - len("IM and Presence Authentication")) * " " + ": UNABLE TO REACH IM&P SERVER \n")
                break

            else:
                file_new_summary.write("IM and Presence Authentication"+(50-len("IM and Presence Authentication"))*" "+": failed\n")
                break




        serviceprofileinfo = serviceprofile_file.split('\n')
        for row in serviceprofileinfo:
            if "serviceprofile_success" in row:
                file_new_summary.write("User Service Profile"+(50-len('user service profile'))*" "+": Passed\n")
                break
            elif "serviceprofile_fail" in row:
                file_new_summary.write("User Service Profile"+(50-len('user service profile'))*" "+": Failed\n")
                break

        jabber_configinfo = jabber_config_file.split('\n')
        for row in jabber_configinfo:
            if "jabber_config_success" in row:
                file_new_summary.write("Jabber Configuration file"+(50-len("Jabber configuration file"))*" "+": Found\n")
                break
            elif "jabber_config_fail" in row:
                file_new_summary.write("Jabber Configuration file"+(50-len('jabber configuration file'))*" "+": Not Found\n")
                break
