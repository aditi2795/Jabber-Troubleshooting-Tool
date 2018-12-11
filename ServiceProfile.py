from xml.dom import minidom
import requests
from UserDetails import *
from xml.dom.minidom import parse
from ManualLogin import *


class service():
    def servicefn(self):
            file = open(manualobj.browseValue+"/service.txt", "w+")
            file1 = open(manualobj.browseValue+"/userdetails.txt", "r").read()
            file2=open(manualobj.browseValue+"/directory_cucm.txt","w+")
            file3=open(manualobj.browseValue+"/cucmservicesummary.txt",'w+')
            file_status = open(manualobj.browseValue+"/serviceprofile_status.txt",'w+')


            try:
                if manualobj.flag!=2:

                    info = file1.split('\n')
                    print info
                    for row in info:


                        if "serviceProfile" in row:
                            servip = row.split('=')[1]
                            break
                        else:
                            print " Service profile not found"
                    print(servip, "serviceip")
                    response = requests.get(servip, verify=False)
                    logging.debug("Service profile debugs")
                    filexml = open(manualobj.browseValue+"/service_profile.xml", "w+")
                    filexml.write(response.text)
                    filexml.close()
                    file3.write("\nFollowing items of Service Profile is not configured\n\n")

                    serviceProfile = minidom.parse(manualobj.browseValue+"/service_profile.xml")
                    voicemail = serviceProfile.getElementsByTagName(("Voicemail"))[0]
                    voiceprimary = voicemail.getElementsByTagName("Primary")[0]
                    vpaddress1 = voiceprimary.getElementsByTagName("Address")[0].firstChild

                    if vpaddress1 != None:
                        file.write("VoiceMail:Primary:" + vpaddress1.data + ":")
                    else:
                        file.write("VoiceMail:Primary:Not Configured:")
                        file3.write("VoiceMail:Primary:Not Configured:\n")
                    vpport1 = voiceprimary.getElementsByTagName("Port")[0].firstChild
                    if vpport1 != None:
                        file.write(vpport1.data + ":")
                    else:
                        file.write("N/A:")
                    vpprotocol1 = voiceprimary.getElementsByTagName("Protocol")[0].firstChild
                    if vpprotocol1 != None:
                        file.write(vpprotocol1.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    voicesecondary = voicemail.getElementsByTagName("Backup1")[0]
                    vpaddress2 = voicesecondary.getElementsByTagName("Address")[0].firstChild

                    if vpaddress2 != None:
                        file.write("VoiceMail:Secondary:" + vpaddress2.data + ":")
                    else:
                        file.write("VoiceMail:Secondary:Not Configured:")

                    vpport2 = voicesecondary.getElementsByTagName("Port")[0].firstChild
                    if vpport2 != None:
                        file.write(vpport2.data + ":")
                    else:
                        file.write("N/A:")
                    vpprotocol2 = voicesecondary.getElementsByTagName("Protocol")[0].firstChild
                    if vpprotocol2 != None:
                        file.write(vpprotocol2.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    voicetertiary = voicemail.getElementsByTagName("Backup2")[0]
                    vpaddress3 = voicetertiary.getElementsByTagName("Address")[0].firstChild

                    if vpaddress3 != None:
                        file.write("VoiceMail:Tertiary:" + vpaddress3.data + ":")
                    else:
                        file.write("VoiceMail:Tertiary:Not Configured:")

                    vpport3 = voicetertiary.getElementsByTagName("Port")[0].firstChild
                    if vpport3 != None:
                        file.write(vpport3.data + ":")
                    else:
                        file.write("N/A:")
                    vpprotocol3 = voicetertiary.getElementsByTagName("Protocol")[0].firstChild
                    if vpprotocol3 != None:
                        file.write(vpprotocol3.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    mailstore = serviceProfile.getElementsByTagName(("MailStore"))[0]
                    mailprimary = mailstore.getElementsByTagName("Primary")[0]
                    maddress1 = mailprimary.getElementsByTagName("Address")[0].firstChild

                    if maddress1 != None:
                        file.write("MailStore:Primary:" + maddress1.data + ":")
                    else:
                        file.write("MailStore:Primary:Not Configured:")
                        file3.write("MailStore:Primary:Not Configured:\n")
                    mport1 = mailprimary.getElementsByTagName("Port")[0].firstChild
                    if mport1 != None:
                        file.write(mport1.data + ":")
                    else:
                        file.write("N/A:")
                    mprotocol1 = mailprimary.getElementsByTagName("Protocol")[0].firstChild
                    if mprotocol1 != None:
                        file.write(mprotocol1.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    mailsecondary = mailstore.getElementsByTagName("Backup1")[0]
                    maddress2 = mailsecondary.getElementsByTagName("Address")[0].firstChild

                    if maddress2 != None:
                        file.write("MailStore:Secondary:" + maddress2.data + ":")
                    else:
                        file.write("MailStore:Secondary:Not Configured:")

                    mport2 = mailsecondary.getElementsByTagName("Port")[0].firstChild
                    if mport2 != None:
                        file.write(mport2.data + ":")
                    else:
                        file.write("N/A:")
                    mprotocol2 = mailsecondary.getElementsByTagName("Protocol")[0].firstChild
                    if mprotocol2 != None:
                        file.write(mprotocol2.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    mailtertiary = mailstore.getElementsByTagName("Backup2")[0]
                    maddress3 = mailtertiary.getElementsByTagName("Address")[0].firstChild

                    if maddress3 != None:
                        file.write("MailStore:" + maddress3.data + ":")
                    else:
                        file.write("MailStore:" + "Tertiary:Not Configured:")

                    mport3 = mailtertiary.getElementsByTagName("Port")[0].firstChild
                    if mport3 != None:
                        file.write("" + mport3.data + ":")
                    else:
                        file.write("N/A:")
                    mprotocol3 = mailtertiary.getElementsByTagName("Protocol")[0].firstChild
                    if mprotocol3 != None:
                        file.write(mprotocol3.data + ":")
                    else:
                        file.write("N/A:\n")

                    conferencing = serviceProfile.getElementsByTagName(("Conferencing"))[0]
                    confprimary = conferencing.getElementsByTagName("Primary")[0]
                    caddress1 = confprimary.getElementsByTagName("Address")[0].firstChild

                    if caddress1 != None:
                        file.write("Conferencing:Primary:" + caddress1.data + ":")
                    else:
                        file.write("Conferencing:" + "Primary:Not Configured:")
                        file3.write("Conferencing:" + "Primary:Not Configured:\n")
                    cport1 = confprimary.getElementsByTagName("Port")[0].firstChild
                    if cport1 != None:
                        file.write(cport1.data + ":")
                    else:
                        file.write("N/A:")
                    cprotocol1 = confprimary.getElementsByTagName("Protocol")[0].firstChild
                    if cprotocol1 != None:
                        file.write(cprotocol1.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    confsecondary = conferencing.getElementsByTagName("Backup1")[0]
                    caddress2 = confsecondary.getElementsByTagName("Address")[0].firstChild

                    if caddress2 != None:
                        file.write("Conferencing:Secondary:" + caddress2.data + ":")
                    else:
                        file.write("Conferencing:Secondary:Not Configured:")

                    cport2 = confsecondary.getElementsByTagName("Port")[0].firstChild
                    if cport2 != None:
                        file.write(cport2.data + " " * (5 - len(str(vpport2.data))) + "|")
                    else:
                        file.write("N/A:")
                    cprotocol2 = confsecondary.getElementsByTagName("Protocol")[0].firstChild
                    if cprotocol2 != None:
                        file.write(cprotocol2.data + ":")
                    else:
                        file.write("N/A:\n")

                    conftertiary = conferencing.getElementsByTagName("Backup2")[0]
                    caddress3 = conftertiary.getElementsByTagName("Address")[0].firstChild

                    if caddress3 != None:
                        file.write("Conferencing:Tertiary :" + caddress3.data + ":")
                    else:
                        file.write("Conferencing:Tertiary" + ":Not Configured:")

                    cport3 = conftertiary.getElementsByTagName("Port")[0].firstChild
                    if cport3 != None:
                        file.write("N/A:")
                    else:
                        file.write("N/A" + ":")
                    cprotocol3 = conftertiary.getElementsByTagName("Protocol")[0].firstChild
                    if cprotocol3 != None:
                        file.write(cprotocol3.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    directory = serviceProfile.getElementsByTagName(("Directory"))[0]
                    dirprimary = directory.getElementsByTagName("Primary")[0]
                    daddress1 = dirprimary.getElementsByTagName("Address")[0].firstChild
                    if daddress1 != None:
                        file.write("Directory:Primary:" + vpaddress1.data + ":")
                    else:
                        file.write("Directory:Primary:Not Configured" + ":")
                        file3.write("Directory:Primary:Not Configured" + ":\n")
                    dport1 = dirprimary.getElementsByTagName("Port")[0].firstChild
                    if dport1 != None:
                        file.write(dport1.data + ":")
                    else:
                        file.write("N/A:")
                    dprotocol1 = dirprimary.getElementsByTagName("Protocol")[0].firstChild
                    if dprotocol1 != None:
                        file.write(dprotocol1.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    dirsecondary = directory.getElementsByTagName("Backup1")[0]
                    daddress2 = dirsecondary.getElementsByTagName("Address")[0].firstChild

                    if daddress2 != None:
                        file.write("Directory:Secondary:" + daddress2.data + ":")
                    else:
                        file.write("Directory:Secondary:Not Configured:")

                    dport2 = dirsecondary.getElementsByTagName("Port")[0].firstChild
                    if dport2 != None:
                        file.write(dport2.data + ":")
                    else:
                        file.write("N/A:")
                    dprotocol2 = dirsecondary.getElementsByTagName("Protocol")[0].firstChild
                    if dprotocol2 != None:
                        file.write(dprotocol2.data + ":\n")
                    else:
                        file.write("N/A:\n")

                    dirtertiary = directory.getElementsByTagName("Backup2")[0]
                    daddress3 = dirtertiary.getElementsByTagName("Address")[0].firstChild

                    if daddress3 != None:
                        file.write("Directory:Tertiary :" + daddress3.data + ":")
                    else:
                        file.write("Directory:Tertiary:Not Configured" + ":")

                    dport3 = dirtertiary.getElementsByTagName("Port")[0].firstChild
                    if dport3 != None:
                        file.write(dport3.data + ":")
                    else:
                        file.write("N/A:")
                    dprotocol3 = dirtertiary.getElementsByTagName("Protocol")[0].firstChild
                    if dprotocol3 != None:
                        file.write(dprotocol3.data + ":\n")
                    else:
                        file.write("N/A:\n")
                    try:
                        useuds=directory.getElementsByTagName("UseUDS")[0].firstChild
                        if useuds!=None:
                            file2.write("UseUDS:"+useuds.data+"\n")
                        else:
                            file2.write("UseUDS:N/A:\n")
                    except:
                        pass
                    try:
                        UseUserCredential = directory.getElementsByTagName("UseUserCredential")[0].firstChild
                        if UseUserCredential != None:
                            file2.write("UseUserCredential:"+UseUserCredential.data + "\n")
                        else:
                            file2.write("UseUserCredential:N/A:\n")
                    except:
                        pass
                    try:
                        DN = directory.getElementsByTagName("DN")[0].firstChild
                        if DN != None:
                            file2.write("DN:"+DN.data + "\n")
                        else:
                            file2.write("DN:N/A:\n")
                    except:
                        pass
                    try:
                        Password = directory.getElementsByTagName("Password")[0].firstChild
                        if Password != None:
                            file2.write("Passsword:"+"*******" + "\n")
                        else:
                            file2.write("Password:N/A:\n")
                    except:
                        pass
                    try:
                        SearchContext1 = directory.getElementsByTagName("SearchContext1")[0].firstChild
                        if SearchContext1 != None:
                            file2.write("SearchContext1:"+SearchContext1.data + "\n")
                        else:
                            file2.write("SearchContext1:N/A:\n")
                    except:
                        pass
                    try:
                        SearchContext2 = directory.getElementsByTagName("SearchContext2")[0].firstChild
                        if SearchContext2 != None:
                            file2.write("SearchContext2:"+SearchContext2.data + "\n")
                        else:
                            file2.write("SearchContext2:N/A:\n")
                    except:
                        pass
                    try:
                        SearchContext3 = directory.getElementsByTagName("SearchContext3")[0].firstChild
                        if SearchContext3 != None:
                            file2.write("SearchContext3:"+SearchContext3.data + "\n")
                        else:
                            file2.write("SearchContext3:N/A:\n")
                    except:
                        pass
                    try:
                        RecursiveSearch1 = directory.getElementsByTagName("RecursiveSearch1")[0].firstChild
                        if RecursiveSearch1 != None:
                            file2.write("RecursiveSearch1:"+RecursiveSearch1.data + "\n")
                        else:
                            file2.write("RecursiveSearch1:N/A:\n")
                    except:
                        pass
                    try:
                        SearchTimeout = directory.getElementsByTagName("SearchTimeout")[0].firstChild
                        if SearchTimeout != None:
                            file2.write("SearchTimeout:"+SearchTimeout.data + "\n")
                        else:
                            file2.write("SearchTimeout:N/A:\n")
                    except:
                        pass
                    try:
                        BaseFilter = directory.getElementsByTagName("BaseFilter")[0].firstChild
                        if BaseFilter != None:
                            file2.write("BaseFilter:"+BaseFilter.data + "\n")
                        else:
                            file2.write("BaseFilter:N/A:\n")
                    except:
                        pass
                    try:
                        PredictiveSearchFilter = directory.getElementsByTagName("PredictiveSearchFilter")[0].firstChild
                        if PredictiveSearchFilter != None:
                            file2.write("PredictiveSearchFilter:"+PredictiveSearchFilter.data + "\n")
                        else:
                            file2.write("PredictiveSearchFilter:N/A:\n")

                    except:
                        pass
                    try:
                        WebConfSSOIdentityProvider = serviceProfile.getElementsByTagName("WebConfSSOIdentityProvider")[0].firstChild
                        if WebConfSSOIdentityProvider != None:
                             file2.write("WebConfSSOIdentityProvider:"+WebConfSSOIdentityProvider.data + "\n")
                        else:
                             file2.write("WebConfSSOIdentityProvider:N/A:\n")
                    except:
                        pass
                    try:
                        VoicemailServiceCredentialsSource =serviceProfile.getElementsByTagName("VoicemailServiceCredentialsSource")[0].firstChild
                        if VoicemailServiceCredentialsSource != None:
                            file2.write("VoicemailServiceCredentialsSource:"+VoicemailServiceCredentialsSource.data + "\n")
                        else:
                            file2.write("VoicemailServiceCredentialsSource:N/A:\n")
                    except:
                        pass
                    try:
                        imp = serviceProfile.getElementsByTagName(("IMandPresence"))[0]
                        impprimary = imp.getElementsByTagName("Primary")[0]
                        iaddress1 = impprimary.getElementsByTagName("Address")[0].firstChild

                        if iaddress1 != None:
                            file.write("IMP:Primary:" + iaddress1.data + ":")
                        else:
                            file.write("IMP:Primary:Not Configured" + ":")
                            file3.write("IMP:Primary:Not Configured" + ":")
                        iport1 = impprimary.getElementsByTagName("Port")[0].firstChild
                        if iport1 != None:
                            file.write(iport1.data + ":")
                        else:
                            file.write("N/A:")
                        iprotocol1 = impprimary.getElementsByTagName("Protocol")[0].firstChild
                        if iprotocol1 != None:
                            file.write(iprotocol1.data + ":\n")
                        else:
                            file.write("N/A:\n")

                        impsecondary = imp.getElementsByTagName("Backup1")[0]
                        iaddress2 = impsecondary.getElementsByTagName("Address")[0].firstChild

                        if iaddress2 != None:
                            file.write("IMP:Secondary:" + iaddress2.data + ":")
                        else:
                            file.write("IMP:Secondary:Not Configured:")
                            file.write("IMP:Secondary:Not Configured:\n")
                        iport2 = impsecondary.getElementsByTagName("Port")[0].firstChild
                        if iport2 != None:
                            file.write(iport2.data + ":")
                        else:
                            file.write("N/A:")
                        iprotocol2 = impsecondary.getElementsByTagName("Protocol")[0].firstChild
                        if iprotocol2 != None:
                            file.write(iprotocol2.data + ":\n")
                        else:
                            file.write("N/A:\n")

                        imptertiary = imp.getElementsByTagName("Backup2")[0]
                        iaddress3 = imptertiary.getElementsByTagName("Address")[0].firstChild

                        if iaddress3 != None:
                            file.write("IMP:Tertiary:" + iaddress3.data + ":")
                        else:
                            file.write("IMP:Tertiary:Not Configured" + ":")
                            file.write("IMP:Tertiary:Not Configured" + ":\n")
                        iport3 = imp.getElementsByTagName("Port")[0].firstChild
                        if iport3 != None:
                            file.write(iport3.data + ":")
                        else:
                            file.write("N/A:")
                        iprotocol3 = imp.getElementsByTagName("Protocol")[0].firstChild
                        if iprotocol3 != None:
                            file.write(iprotocol3.data + ":\n")
                        else:
                            file.write("N/A:\n")

                        cti = serviceProfile.getElementsByTagName(("CTI"))[0]
                        ctiprimary = cti.getElementsByTagName("Primary")[0]
                        ctaddress1 = ctiprimary.getElementsByTagName("Address")[0].firstChild

                        if ctaddress1 != None:
                            file.write("CTI:Primary:" + ctaddress1.data + ":")
                        else:
                            file.write("CTI:Primary:Not Configured" + ":")
                            file3.write("CTI:Primary:Not Configured" + ":\n")
                        ctport1 = ctiprimary.getElementsByTagName("Port")[0].firstChild
                        if ctport1 != None:
                            file.write(ctport1.data + ":")
                        else:
                            file.write("N/A:")
                        ctprotocol1 = ctiprimary.getElementsByTagName("Protocol")[0].firstChild
                        if ctprotocol1 != None:
                            file.write(ctprotocol1.data + ":\n")
                        else:
                            file.write("N/A:\n")

                        ctisecondary = cti.getElementsByTagName("Backup1")[0]
                        ctaddress2 = ctisecondary.getElementsByTagName("Address")[0].firstChild

                        if ctaddress2 != None:
                            file.write("CTI:Secondary:" + ctaddress2.data + ":")
                        else:
                            file.write("CTI:Secondary:Not Configured:")

                        ctport2 = ctisecondary.getElementsByTagName("Port")[0].firstChild
                        if ctport2 != None:
                            file.write(ctport2.data + ":")
                        else:
                            file.write("N/A:")
                        ctprotocol2 = ctisecondary.getElementsByTagName("Protocol")[0].firstChild
                        if ctprotocol2 != None:
                            file.write(ctprotocol2.data + ":\n")
                        else:
                            file.write("N/A:\n")

                        ctitertiary = cti.getElementsByTagName("Backup2")[0]
                        ctaddress3 = ctitertiary.getElementsByTagName("Address")[0].firstChild

                        if ctaddress3 != None:
                            file.write("CTI:Tertiary:" + ctaddress3.data + ":")
                        else:
                            file.write("CTI:Tertiary:Not Configured" + ":")

                        ctport3 = cti.getElementsByTagName("Port")[0].firstChild
                        if ctport3 != None:
                            file.write(ctport3.data + ":")
                        else:
                            file.write("N/A:")
                        ctprotocol3 = cti.getElementsByTagName("Protocol")[0].firstChild
                        if ctprotocol3 != None:
                            file.write(ctprotocol3.data + ":\n")
                        else:
                            file.write("N/A:\n")
                    except:
                        pass
                    try:
                        vcs = serviceProfile.getElementsByTagName(("VideoConferenceSchedulingPortal"))[0]
                        vcsprimary = vcs.getElementsByTagName("Primary")[0]
                        vaddress1 = vcsprimary.getElementsByTagName("Address")[0].firstChild

                        if vaddress1 != None:
                            file.write("VCS:Primary:" + vaddress1.data + ":")
                        else:
                            file.write("VCS:Primary:Not Configured" + ":")
                            file3.write("VCS:Primary:Not Configured" + ":\n")
                        vport1 = vcsprimary.getElementsByTagName("Port")[0].firstChild
                        if vport1 != None:
                            file.write(vport1.data + ":")
                        else:
                            file.write("N/A:")
                        vprotocol1 = vcsprimary.getElementsByTagName("Protocol")[0].firstChild
                        if vprotocol1 != None:
                            file.write(vprotocol1.data + ":\n")
                        else:
                            file.write("N/A:\n")

                        vcssecondary = vcs.getElementsByTagName("Backup1")[0]
                        vaddress2 = vcssecondary.getElementsByTagName("Address")[0].firstChild
                        if vaddress2 != None:
                            file.write("VCS:Secondary:" + vaddress2.data + ":")
                        else:
                            file.write("VCS:Secondary:Not Configured:")

                        vport2 = vcssecondary.getElementsByTagName("Port")[0].firstChild
                        if vport2 != None:
                            file.write(vport2.data + ":")
                        else:
                            file.write("N/A:")
                        vprotocol2 = vcssecondary.getElementsByTagName("Protocol")[0].firstChild
                        if vprotocol2 != None:
                            file.write(vprotocol2.data + ":\n")
                        else:
                            file.write("N/A:\n")

                        vcstertiary = vcs.getElementsByTagName("Backup2")[0]
                        vaddress3 = vcstertiary.getElementsByTagName("Address")[0].firstChild

                        if vaddress3 != None:
                            file.write("VCS:Tertiary:" + vaddress3.data + ":")
                        else:
                            file.write("VCS:Tertiary:Not Configured" + ":")

                        vport3 = vcs.getElementsByTagName("Port")[0].firstChild
                        if vport3 != None:
                            file.write(vport3.data + ":")
                        else:
                            file.write("N/A:")
                        vprotocol3 = vcs.getElementsByTagName("Protocol")[0].firstChild
                        if vprotocol3 != None:
                            file.write(vprotocol3.data + ":\n")
                        else:
                            file.write("N/A:\n")
                        file.close()
                        logging.debug("Servie Profile fetched successfully")
                    except:
                        pass
                else:
                        file3.write("\nIM&P Login is selected and hence no CUCM SERVICE PROFILE\n")

                file_status.write("serviceprofile_success")


            except Exception as e:
                logging.error(str(e))
                file.write("Unable to load Service Profile")
                file.close()
                file_status.write("serviceprofile_fail")

serviceobj = service()
#serviceobj.servicefn()
# serviceobj.out = open("C:/Python27/service.txt", 'r').read()
# if __name__ == "__main__":
#     serviceobj.servicefn()