import webbrowser
import pyperclip
import pyautogui
import time
from colorama import Fore,Style


documento = open('direcciones_ip.txt','r')
documento = documento.read().split('\n')
contador = 0


while contador == 0:
    eleccion = input(Fore.GREEN + "!! Escriba el (Numero correspondiente) a la herramienta que desea utilizar para analizar IPweb !!\n \n1 -Symantec \n2 -AbuseIP \n3 -Virustotal \n4 -Busca IP (nombre_web.com) \n0 -Salir.\n\n"+ Style.RESET_ALL + "Cual es tu eleccion?"+Fore.GREEN +"-->")

    if eleccion == "1":
        for ip in documento:
            webbrowser.open_new("https://sitereview.bluecoat.com/#/")
            time.sleep(3)
            pyperclip.copy(ip)
            pyautogui.hotkey('ctrl','v',interval= 0.15)
            pyautogui.press("enter")
    
    
    elif eleccion == "2":
        for ip in documento:
           webbrowser.open_new("https://www.abuseipdb.com/")
           time.sleep(3)
           for i in range(15):
               pyautogui.press("tab")
           pyperclip.copy(ip)
           pyautogui.hotkey('ctrl','v',interval= 0.15)
           pyautogui.press("enter")
        
    elif eleccion == "3":
       for ip in documento:
          webbrowser.open_new("https://www.virustotal.com")
          time.sleep(3)
          for i in range(4):
              pyautogui.press("tab")
          pyperclip.copy(ip)
          pyautogui.hotkey('ctrl','v',interval= 0.15)
          pyautogui.press("enter")

    elif eleccion == "4":
        nombre = input("Escriba el nombre de la web que desea saber su IP.\n\n-->")
        webbrowser.open_new("https://www.mon-ip.com/es/mi-ip/direccion-ip-sitio.php ")
        time.sleep(3)
        pyperclip.copy(nombre)
        pyautogui.hotkey('ctrl','v',interval= 0.15)
        pyautogui.press("enter")  
    
    elif contador == 0:
        print(Fore.GREEN +"Gracias saludos!!")
        break    
             
    else:
        print("ERROR!!! Hay que insertar un numero del 1 al 3.")        