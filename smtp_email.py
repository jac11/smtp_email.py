#/usr/bin/env python 


import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart    
from email.mime.base import MIMEBase
from email import encoders
import imghdr 
import time 
import os 

class Sand_Mail():
      
      import atexit
      import os
      import readline
      import rlcompleter
           
      historyPath = os.path.expanduser("~/.EMAIL_HISTORY")
      def save_history(historyPath=historyPath):
             import readline
             readline.write_history_file(historyPath)
      if os.path.exists(historyPath):
             readline.read_history_file(historyPath)
      atexit.register(save_history)
      del os, atexit, readline, rlcompleter, save_history, historyPath

      def __init__(self): 
            self.banner()
            self.INFORMATIONS()
            self.Messags_heder()
            self.attached_file()
            self.Send_email()
            
      def INFORMATIONS(self):
          try: 
              self.sendder = str(raw_input("\n[#]Enter the Email Sender [FROM]:"))
              time.sleep(2)
              self.Receive =  str(raw_input("\n[#]Enter the Email Receiver [TO] :"))
              time.sleep(2)
              self.smtp_machine =  str(raw_input("\n[#]Enter the SMTP Server Name or Ip address :"))
              time.sleep(2)
              self.user_SMTP = str(raw_input("\n[#]Enter SMTP User Name or Email account :"))
              time.sleep(2)
              self.auth = str(raw_input("\n[#]Enter Password or APIkey :"))
              time.sleep(2)
              self.subject = str(raw_input("\n[#]Email Subject :"))
              time.sleep(2)
              self.body= str(raw_input("\n[#]Email Message :"))
              time.sleep(2)
          except KeyboardInterrupt:
                  self.banner()
                  exit()                 
      def Messags_heder(self) :
           self.mes = MIMEMultipart()
           self.mes["From"]= self.sendder
           self.mes["To"]= self.Receive
           self.mes["subject"] = self.subject
          
      def attached_file(self):
           try:
              try:
                 value_1='Y'
                 value_2='N'
                 print "\n[\]if you want attach fille pleae enter 'y ' or not enter 'n'[/]\n".upper()
                 time.sleep(2)
                 self.input = str(raw_input("\n[@]Enter your choese 'y' or 'n': ".upper()))
                 time.sleep(2)
                 if self.input == value_1 :
                    for i in self.input:
                        print "\n[@]to attach file Change Current Working Directory than Enter the attach File Name[@]"
                        time.sleep(2)
                        path =str(raw_input("\n[#]Enter Current Working Directory :"))
                        time.sleep(2)
                        os.chdir(path)
                        print "\n[O]The Current Working Directory is :",os.getcwd()
                        time.sleep(2)
                        file_name = str(raw_input("\n[#]Enter the file name :"))
                        time.sleep(2)
                        file_atta = open(file_name,'rb')    
                        get = MIMEBase("application","octet-stream")
                        get.set_payload((file_atta).read())
                        encoders.encode_base64(get)
                        get.add_header("content-Disposition","file_atta ;filename ="+file_name)
                        self.mes.attach(get)
                        self.message= self.mes.as_string()
                        break   
                 elif self.input == "N":
                     pass 
                       
                 else:   
                     print"\n[+]Check the input[+]"
                     time.sleep(2)
                     self.attached_file()   
              except Exception: 
                  print "\n(@)SomeThing is wrong try again[]"
                  self.attached_file()
           except KeyboardInterrupt:
                  self.banner()
                  exit() 
                                
      def Send_email(self):
           try:
               try:
                 print "\n[&]selcet your encryption 'SSL' in port '465'or 'TLS' in port '587' use uppercase[@]"
                 time.sleep(2)  
                 option_1 = "TLS".upper()
                 option_2 = "SSL".upper()
                 encryption = str(raw_input('[#]\nplease enter you encryption for email "SSL" or "TLS" : '))
                 time.sleep(2)
                 if encryption ==option_1:
                      print"\n[#]the email encryption is :",encryption
                      time.sleep(2)
                      server = smtplib.SMTP(self.smtp_machine,587)
                      server.starttls()
                      server.login(self.user_SMTP,self.auth)
                 elif encryption ==option_2:
                      print"\n[#]the email encryption is :",encryption
                      time.sleep(2)
                      server = smtplib.SMTP_SSL(self.smtp_machine,465)
                      server.login(self.user_SMTP,self.auth)
                 else:
                      time.sleep(2)
                      print"\n(@)SomeThing is wrong try again[]"
                      time.sleep(2)
                      print"[%]\nencryption  is SSL or TLS",encryption ,"not found"
                      time.sleep(2)
                      return self.Send_email()
                 if self.input =='Y':
                    server.sendmail(self.sendder, self.Receive ,self.message)
                    server.quit()
                    print "\n[%]!!Congratulation the Email  is Delivered !![%]"
                    self.banner()
                    exit() 
                 if self.input =='N':
                    self.mes.attach(MIMEText(self.body,"plain"))
                    self.mes=self.mes.as_string()
                    server.sendmail(self.sendder, self.Receive,self.mes)
                    server.quit()  
                    print "\n[%]!!Congratulation the Email  is Delivered !![%]" 
                    self.banner()
                    exit()
               except Exception:
                   time.sleep(2)
                   print "\n[E]Email Not Delivered [E]"
                   time.sleep(2)
                   print "\n[E]Check you input informations and try again[E]"
                   time.sleep(2)
                   self.INFORMATIONS()
                   self.Messags_heder()
                   self.attached_file()
                   self.Send_email()
           except KeyboardInterrupt:
                  self.banner()
                  exit()              
      
      def banner(self):
      
            banner ="""  
 ____  __  __ _____ ____   ____       __  __       _ _     
/ ___||  \/  |_   _|  _ \ / __ \  ___|  \/  | __ _(_) |    
\___ \| |\/| | | | | |_) / / _` |/ _ \ |\/| |/ _` | | |    
 ___) | |  | | | | |  __/ | (_| |  __/ |  | | (_| | | |___ 
|____/|_|  |_| |_| |_|   \ \__,_|\___|_|  |_|\__,_|_|_____|
                          \____/                           """

                                        
            print banner                                    
                                 
                                              
if __name__=='__main__':
     Sand_Mail()
