import re
from ManualLogin import *
class default():
    def defaultfn(self):
        file=open("parameters.txt",'r')
        file1=open(manualobj.browseValue+"/jabber_default.txt",'w+')
        file_read=file.read()
        for row in file_read.split('\n'):
            if "AllowUserSelectChatsFileDirectory" in row:
                file1.write("AllowUserSelectChatsFileDirectory:true")
                file1.write("\n")
            if "AutoAcceptFileTransfer" in row:
                file1.write("AutoAcceptFileTransfer:false")
                file1.write("\n")
            # if "AutosaveChatsLocation" in row:
            #     file1.write("AutosaveChatsLocation:Local_Path")
            #     file1.write("\n")
            if "CachePasswordMobile" in row:
                file1.write("CachePasswordMobile:true")
                file1.write("\n")
            if "ChatAlert" in row:
                file1.write("ChatAlert:true")
                file1.write("\n")
            if "ChatTelephonyEscalationLimit" in row:
                file1.write("ChatTelephonyEscalationLimit:25")
                file1.write("\n")

            if "DefaultActionOfContactList" in row:
                file1.write("DefaultActionOfContactList:Chat")

                file1.write("\n")
            if "Disable_IM_History" in row:
                file1.write("Disable_IM_History:false")
                file1.write("\n")
            if "EnableAutosave" in row:
                file1.write("EnableAutosave:false")
                file1.write("\n")
            if "EnableInImages" in row:
                file1.write("EnableInImages:true")
                file1.write("\n")
            if "EnableFecc" in row:
                file1.write("EnableFecc:true")
                file1.write("\n")
            if "EnablePrt" in row:
                file1.write("EnablePrt:true")
                file1.write("\n")
            # if "ForceLogoutTimerMobile" in row:
            #     file1.write("ForceLogoutTimerMobile:")
            #     file1.write("\n")
            if "MaxNumberOfBookmarks" in row:
                file1.write("MaxNumberOfBookmarks:30")
                file1.write("\n")

            if "Mention_GroupChat" in row:
                file1.write("Mention_GroupChat:true")
                file1.write("\n")
            if "Mention_P2Pchat" in row:
                file1.write("Mention_P2Pchat:true")
                file1.write("\n")
            if "Mention_PersistentChat" in row:
                file1.write("Mention_PersistentChat:true")
                file1.write("\n")
            if "pChatMeeting" in row:
                file1.write("pChatMeeting:true")
                file1.write("\n")
            if "pChatShare" in row:
                file1.write("pChatShare:true")
                file1.write("\n")
            if "Persistent_Chat_Enabled" in row:
                file1.write("Persistent_Chat_Enabled:false")
                file1.write("\n")
            if "PersistentChatTelephonyEnabled" in row:
                file1.write("PersistentChatTelephonyEnabled:true")
                file1.write("\n")
            if "RestoreChatOnLogin" in row:
                file1.write("RestoreChatOnLogin:false")
                file1.write("\n")
            if "ShowRecentsTab" in row:
                file1.write("ShowRecentsTab:true")
                file1.write("\n")
            if "spell_check_language" in row:
                file1.write("spell_check_language:false")
                file1.write("\n")
            if "SwapDisplayNameOrder" in row:
                file1.write("SwapDisplayNameOrder:true")
                file1.write("\n")
            if "SystemIdleDuringCalls" in row:
                file1.write("SystemIdleDuringCalls:false")
                file1.write("\n")
            # if "UpdateURL" in row:
            #     file1.write("UpdateURL:")
            #     file1.write("\n")
            if "UseAnonymousBinding" in row:
                file1.write("UseAnonymousBinding:false")
                file1.write("\n")
            if "AllowUserCustomTabs" in row:
                file1.write("AllowUserCustomTabs:true")
                file1.write("\n")
            if "CalendarAutoRefreshTime" in row:
                file1.write("CalendarAutoRefreshTime:0")
                file1.write("\n")
            # if "CalendarIntegrationType" in row:
            #     file1.write("CalendarIntegrationType:")
            #     file1.write("\n")
            # if "Callhistory_Expire_Days" in row:
            #     file1.write("Callhistory_Expire_Days:")
            #     file1.write("\n")
            # if "ConfMediaType" in row:
            #     file1.write("ConfMediaType:")
            #     file1.write("\n")
            if "DockedWindowPosition" in row:
                file1.write("DockedWindowPosition:TopCenter")
                file1.write("\n")
            if "DockedWindowVisible" in row:
                file1.write("DockedWindowVisible:true")
                file1.write("\n")
            if "EnableBridgeConferencing" in row:
                file1.write("EnableBridgeConferencing:false")
                file1.write("\n")
            if "EnableLoadAddressBook" in row:
                file1.write("EnableLoadAddressBook:false")
                file1.write("\n")
            if "EnableSaveChatHistoryToExchange" in row:
                file1.write("EnableSaveChatHistoryToExchange:false")
                file1.write("\n")
            if "ExchangeAuthenticateWithSystemAccount" in row:
                file1.write("ExchangeAuthenticateWithSystemAccount:true")
                file1.write("\n")
            # if "ExchangeAutodiscoverDomain" in row:
            #     file1.write("ExchangeAutodiscoverDomain:")
            #     file1.write("\n")
            if "Exchange_UseCredentialsFrom" in row:
                file1.write("Exchange_UseCredentialsFrom:")
                file1.write("\n")
            # if "ExternalExchangeServer" in row:
            #     file1.write("ExternalExchangeServer:")
            #     file1.write("\n")
            # if "InternalExchangeServer" in row:
            #     file1.write("InternalExchangeServer:")
            #     file1.write("\n")
            if "Location_Enabled" in row:
                file1.write("Location_Enabled:true")
                file1.write("\n")
            if "LOCATION_MATCHING_MODE" in row:
                file1.write("LOCATION_MATCHING_MODE:MacAddressOnly")
                file1.write("\n")
            if "Location_Mode" in row:
                file1.write("Location_Mode:ENABLED")
                file1.write("\n")
            if "Set_Status_Away_On_Inactive" in row:
                file1.write("Set_Status_Away_On_Inactive:DisabledByPolicy:true")
                file1.write("\n")
            if "Set_Status_Away_On_Lock_OS" in row:
                file1.write("Set_Status_Away_On_Lock_OS:true")
                file1.write("\n")
            if "Set_Status_Inactive_Timeout" in row:
                file1.write("Set_Status_Inactive_Timeout:15")
                file1.write("\n")
            if "ShowContactPictures" in row:
                file1.write("ShowContactPictures:true")
                file1.write("\n")
            if "ShowOffContacts" in row:
                file1.write("ShowOffContacts:true")
                file1.write("\n")
            if "StartCallWithVideo" in row:
                file1.write("StartCallWithVideo:true")
                file1.write("\n")
            if "Start_Client_On_Start_OS" in row:
                file1.write("Start_Client_On_Start_OS:false")
                file1.write("\n")
            if "UseBridgeForConferenceCalls" in row:
                file1.write("UseBridgeForConferenceCalls:true")
                file1.write("\n")
            # if "CcmcipServer1" in row:
            #     file1.write("CcmcipServer1:")
            #     file1.write("\n")
            # if "CcmcipServer2" in row:
            #     file1.write("CcmcipServer2:")
            #     file1.write("\n")
            # if "CtiServer1" in row:
            #     file1.write("CtiServer1:")
            #     file1.write("\n")
            # if "CtiServer2" in row:
            #     file1.write("CtiServer2:")
            #     file1.write("\n")
            if "EnableCallPark" in row:
                file1.write("EnableCallPark:true")

                file1.write("\n")
            if "EnableDSCPPacketMarking" in row:
                file1.write("EnableDSCPPacketMarking:true")
                file1.write("\n")
            if "MakeCallHotKey" in row:
                file1.write("MakeCallHotKey:true")
                file1.write("\n")
            # if "Meeting_Server_Address" in row:
            #     file1.write("Meeting_Server_Address:")
            #     file1.write("\n")
            # if "Meeting_Server_Address_Backup" in row:
            #     file1.write("Meeting_Server_Address_Backup:")
            #     file1.write("\n")
            # if "Meeting_Server_Address2" in row:
            #     file1.write("Meeting_Server_Address2:")
            #     file1.write("\n")
            # if "TftpServer1" in row:
            #     file1.write("TftpServer1:")
            #     file1.write("\n")
            # if "TftpServer2" in row:
            #     file1.write("TftpServer2:")
            #     file1.write("\n")
            # if "useCUCMGroupForCti" in row:
            #     file1.write("useCUCMGroupForCti:false")
            #     file1.write("\n")
            # if "DisableMFTForConversationTypes" in row:
            #     file1.write("DisableMFTForConversationTypes:")
            #     file1.write("\n")
            # if "Disallowed_File_Transfer_Types" in row:
            #     file1.write("Disallowed_File_Transfer_Types:")
            #     file1.write("\n")
            if "File_Transfer_Enabled" in row:
                file1.write("File_Transfer_Enabled:true")
                file1.write("\n")
            # if "PreferredFT" in row:
            #     file1.write("PreferredFT:")
            #     file1.write("\n")
            if "Screen_Capture_Enabled" in row:
                file1.write("Screen_Capture_Enabled:true")
                file1.write("\n")
            if "AddContactProtocolRateLimit" in row:
                file1.write("AddContactProtocolRateLimit:3")
                file1.write("\n")
            if "AlertOnAvailableEnabled" in row:
                file1.write("AlertOnAvailableEnabled:true")
                file1.write("\n")
            if "CiscoTelProtocolCrossLaunchBackSchema" in row:
                file1.write("CiscoTelProtocolCrossLaunchBackSchema:none")
                file1.write("\n")
            if "ClickToCallProtocolPermissionEnabled" in row:
                file1.write("ClickToCallProtocolPermissionEnabled:true")
                file1.write("\n")
            if "CTIWindowBehaviour" in row:
                file1.write("CTIWindowBehaviour:OnCall")
                file1.write("\n")
            if "DeskPhoneModeWindowBehavior" in row:
                file1.write("DeskPhoneModeWindowBehavior:OnCall")
                file1.write("\n")
            if "EnableBFCPVideoDesktopShare" in row:
                file1.write("EnableBFCPVideoDesktopShare:true")
                file1.write("\n")
            if "Disallow_File_Transfer_On_Mobile" in row:
                file1.write("Disallow_File_Transfer_On_Mobile:false")
                file1.write("\n")
            if "EnableCallPickup" in row:
                file1.write("EnableCallPickup:false")
                file1.write("\n")
            if "EnableCiscoChatProtocol" in row:
                file1.write("EnableCiscoChatProtocol:true")
                file1.write("\n")
            if "EnableCiscoIMGroupProtocol" in row:
                file1.write("EnableCiscoIMGroupProtocol:true")
                file1.write("\n")
            if "EnableCiscoIMProtocol" in row:
                file1.write("EnableCiscoIMProtocol:true")
                file1.write("\n")
            if "EnableCiscoTelConfProtocol" in row:
                file1.write("EnableCiscoTelConfProtocol:true")
                file1.write("\n")
            if "EnableCiscoTelProtocol" in row:
                file1.write("EnableCiscoTelProtocol:true")
                file1.write("\n")
            if "EnableClickToCallProtocol" in row:
                file1.write("EnableClickToCallProtocol:true")
                file1.write("\n")
            if "EnableForensicsContactData" in row:
                file1.write("EnableForensicsContactData:true")
                file1.write("\n")
            if "EnableGroupCallPickup" in row:
                file1.write("EnableGroupCallPickup:false")
                file1.write("\n")
            if "EnableHuntGroup" in row:
                file1.write("EnableHuntGroup:false")
                file1.write("\n")
            if "EnableIMProtocol" in row:
                file1.write("EnableIMProtocol:true")
                file1.write("\n")
            if "EnableLocalAddressBookSearch" in row:
                file1.write("EnableLocalAddressBookSearch:true")
                file1.write("\n")
            if "EnableLotusNotesContactResolution" in row:
                file1.write("EnableLotusNotesContactResolution:false")
                file1.write("\n")
            if "EnableMediaStatistics" in row:
                file1.write("EnableMediaStatistics:true")
                file1.write("\n")
            if "EnableOtherGroupPickup" in row:
                file1.write("EnableOtherGroupPickup:false")
                file1.write("\n")
            if "EnableP2PDesktopShare" in row:
                file1.write("EnableP2PDesktopShare:true")
                file1.write("\n")
            if "EnableProfileProtocol" in row:
                file1.write("EnableProfileProtocol:true")
                file1.write("\n")
            if "EnableProvisionProtocol" in row:
                file1.write("EnableProvisionProtocol:true")
                file1.write("\n")
            if "EnableSaveChatToFile" in row:
                file1.write("EnableSaveChatToFile:true")
                file1.write("\n")
            if "EnableShareProtocol" in row:
                file1.write("EnableShareProtocol:true")
                file1.write("\n")
            if "EnableSIPProtocol" in row:
                file1.write("EnableSIPProtocol:true")
                file1.write("\n")
            if "EnableSIPURIDialling" in row:
                file1.write("EnableSIPURIDialling:false")
                file1.write("\n")
            if "EnableStatusProtocol" in row:
                file1.write("EnableStatusProtocol:true")
                file1.write("\n")
            if "EnableTelephonyProtocolRateLimit" in row:
                file1.write("EnableTelephonyProtocolRateLimit:true")
                file1.write("\n")
            if "EnableTelProtocol" in row:
                file1.write("EnableTelProtocol:true")
                file1.write("\n")
            if "CiscoTelProtocolPermissionEnabled" in row:
                file1.write("CiscoTelProtocolPermissionEnabled:true")
                file1.write("\n")
            if "EnableVideo" in row:
                file1.write("EnableVideo:true")
                file1.write("\n")
            if "EnableXMPPProtocol" in row:
                file1.write("EnableXMPPProtocol:true")
                file1.write("\n")
            if "ForceC2XDirectoryResolution" in row:
                file1.write("ForceC2XDirectoryResolution:true")
                file1.write("\n")
            if "ForceFontSmoothing" in row:
                file1.write("ForceFontSmoothing:true")
                file1.write("\n")
            if "InitialPhoneSelection" in row:
                file1.write("InitialPhoneSelection:softphone")
                file1.write("\n")
            if "LogWritingDesktop" in row:
                file1.write("LogWritingDesktop:Always")
                file1.write("\n")
            if "LogWritingMobile" in row:
                file1.write("LogWritingMobile:Always")
                file1.write("\n")
            if "Meetings_Enabled" in row:
                file1.write("Meetings_Enabled:true")
                file1.write("\n")
            if "PreferP2PDesktopShare" in row:
                file1.write("PreferP2PDesktopShare:false")
                file1.write("\n")
            if "PresenceProtocolRateLimit" in row:
                file1.write("PresenceProtocolRateLimit:3")
                file1.write("\n")
            if "PresenceProtocolTimeLimit" in row:
                file1.write("PresenceProtocolTimeLimit:15")
                file1.write("\n")
            if "PreventDecOnHuntCall" in row:
                file1.write("PreventDecOnHuntCall:false")
                file1.write("\n")
            if "PrintIMEnabled" in row:
                file1.write("PrintIMEnabled:true")
                file1.write("\n")
            if "ProfileProtocolRateLimit" in row:
                file1.write("ProfileProtocolRateLimit:3")
                file1.write("\n")
            if "ProfileProtocolTimeLimit" in row:
                file1.write("ProfileProtocolTimeLimit:15")
                file1.write("\n")

            if "Recent_Chats_Enabled" in row:
                file1.write("Recent_Chats_Enabled:true")
                file1.write("\n")


            # if "ScreenShareAuditMessages" in row:
            #     file1.write("ScreenShareAuditMessages:false")
            #     file1.write("\n")
            # if "selfcareURL" in row:
            #     file1.write("selfcareURL:")
            #     file1.write("\n")
            #
            # if "ServiceDiscoveryExcludedServices" in row:
            #     file1.write("ServiceDiscoveryExcludedServices:")
            #     file1.write("\n")
            # if "ServicesDomainSsoEmailPrompt" in row:
            #     file1.write("ServicesDomainSsoEmailPrompt:")
            #     file1.write("\n")
            if "ShareProtocolRateLimit" in row:
                file1.write("ShareProtocolRateLimit:3")
                file1.write("\n")
            if "ShareProtocolTimeLimit" in row:
                file1.write("ShareProtocolTimeLimit:15")
                file1.write("\n")
            if "ShowSelfCarePortal" in row:
                file1.write("ShowSelfCarePortal:true")
                file1.write("\n")
            if "SoftPhoneModeWindowBehavior" in row:
                file1.write("SoftPhoneModeWindowBehavior:OnCall")
                file1.write("\n")
            if "SSO_Enabled" in row:
                file1.write("SSO_Enabled:TRUE")
                file1.write("\n")
            if "TelemetryEnabled" in row:
                file1.write("TelemetryEnabled:true")
                file1.write("\n")
            if "TelemetryEnabledOverCellularData" in row:
                file1.write("TelemetryEnabledOverCellularData:true")
                file1.write("\n")





            # if "TelemetryCustomerID" in row:
            #     file1.write("TelemetryCustomerID:")
            #     file1.write("\n")
            if "TelephonyProtocolRateLimit" in row:
                file1.write("TelephonyProtocolRateLimit:2")
                file1.write("\n")
            if "TelephonyProtocolTimeLimit" in row:
                file1.write("TelephonyProtocolTimeLimit:10")
                file1.write("\n")
            if "Telephony_Enabled" in row:
                file1.write("Telephony_Enabled:true")
                file1.write("\n")
            if "UserDefinedRemoteDestinations" in row:
                file1.write("UserDefinedRemoteDestinations:false")
                file1.write("\n")
            if "Voicemail_Enabled" in row:
                file1.write("Voicemail_Enabled:true")
                file1.write("\n")
            if "CalendarWebExMeetingPresence" in row:
                file1.write("CalendarWebExMeetingPresence:false")
                file1.write("\n")
            if "LoginResource" in row:
                file1.write("LoginResource:multiResource")
                file1.write("\n")
            # if "PresenceServerAddress" in row:
            #     file1.write("PresenceServerAddress:")
            #     file1.write("\n")
            if "ForwardVoicemail" in row:
                file1.write("ForwardVoicemail:true")
                file1.write("\n")
            # if "VoicemailBackup1Server" in row:
            #     file1.write("VoicemailBackup1Server:")
            #     file1.write("\n")
            #
            #
            # if "VoicemailBackup2Server" in row:
            #     file1.write("VoicemailBackup2Server:")
            #     file1.write("\n")
            # if "VoicemailPrimaryServer" in row:
            #     file1.write("VoicemailPrimaryServer:")
            #     file1.write("\n")
            # if "PrimaryServerName" in row:
            #     file1.write("PrimaryServerName:")
            #     file1.write("\n")
            # if "SecondaryServerName" in row:
            #     file1.write("SecondaryServerName:")
            #     file1.write("\n")
            # if "ConnectionUsername" in row:
            #     file1.write("ConnectionUsername:")
            #     file1.write("\n")
            # if "ConnectionPassword" in row:
            #     file1.write("ConnectionPassword:")
            #     file1.write("\n")
            if "UseANR" in row:
                file1.write("UseANR:True")
                file1.write("\n")
            if "BaseFilter" in row:
                file1.write("BaseFilter:(&(objectCategory=person)( objectClass=user).")
                file1.write("\n")
            if "DisableSecondaryNumberLookups" in row:
                file1.write("DisableSecondaryNumberLookups:0")
                file1.write("\n")
            if "SearchTimeout" in row:
                file1.write("SearchTimeout:5")
                file1.write("\n")
            if "UseWildcards" in row:
                file1.write("UseWildcards:0")
                file1.write("\n")
            # if "SipUri" in row:
            #     file1.write("SipUri:")
            #     file1.write("\n")
            # if "UriPrefix" in row:
            #     file1.write("UriPrefix:")
            #     file1.write("\n")
            # if "UseSIPURIToResolveContacts" in row:
            #     file1.write("UseSIPURIToResolveContacts:")
            #     file1.write("\n")
            # if "UdsPhotoUriWithToken" in row:
            #     file1.write("UdsPhotoUriWithToken:")
            #     file1.write("\n")
            # if "UdsServer" in row:
            #     file1.write("UdsServer:")
            #     file1.write("\n")
            # if "PresenceDomain" in row:
            #     file1.write("PresenceDomain:")
            #     file1.write("\n")
            # if "PhoneNumberMasks" in row:
            #     file1.write("PhoneNumberMasks:")
            #     file1.write("\n")
            #
            #
            # if "PhotoSource" in row:
            #     file1.write("PhotoSource:")
            #     file1.write("\n")
            # if "PhotoUriSubstitutionToken" in row:
            #     file1.write("PhotoUriSubstitutionToken:")
            #     file1.write("\n")
            if "PhotoUriSubstitutionEnablede" in row:
                file1.write("PhotoUriSubstitutionEnablede:false")
                file1.write("\n")
            # if "LdapUserDomain" in row:
            #     file1.write("LdapUserDomain:")
            #     file1.write("\n")
            # if "LDAP_UseCredentialsFrom" in row:
            #     file1.write("LDAP_UseCredentialsFrom:")
            #     file1.write("\n")
            # if "UseLdapReferral" in row:
            #     file1.write("UseLdapReferral:0")
            #     file1.write("\n")
            # if "SipUri" in row:
            #     file1.write("SipUri:")
            #     file1.write("\n")
            # if "UriPrefix" in row:
            #     file1.write("BUriPrefix:")
            #     file1.write("\n")
            # if "UseSipUriToResolveContacts" in row:
            #     file1.write("UseSipUriToResolveContacts:")
            #     file1.write("\n")
            # if "GroupSearchBase1" in row:
            #     file1.write("GroupSearchBase1:")
            #     file1.write("\n")
            # if "MinimumCharacterQuery" in row:
            #     file1.write("MinimumCharacterQuery:")
            #     file1.write("\n")
