Escáner de IP y Sitios Web

Este es un programa en Python que te permite realizar escaneos en varios servicios en línea utilizando direcciones IP o nombres de dominio. El programa proporciona una interfaz simple en la línea de comandos para seleccionar el servicio que deseas utilizar para el análisis.

Modo de uso
Configuración de las direcciones IP o sitios web: Antes de utilizar el programa, asegúrate de agregar las direcciones IP o los nombres de dominio de los sitios web que deseas analizar en un archivo de texto llamado direcciones_ip.txt. Cada dirección debe estar en una línea separada en este archivo.

Ejecución del programa: Ejecuta el script proporcionado en un entorno de Python. El programa solicitará que selecciones el servicio de análisis deseado ingresando el número correspondiente.

Servicios de análisis disponibles:

1 - Symantec: Utiliza el servicio de Symantec para análisis de seguridad de sitios web.
2 - AbuseIP: Utiliza el servicio de AbuseIP para buscar si las direcciones IP han sido reportadas por actividades maliciosas.
3 - VirusTotal: Utiliza el servicio de VirusTotal para realizar un análisis de virus en los sitios web.
4 - Buscar IP (nombre_web.com): Proporciona la dirección IP de un sitio web ingresando su nombre de dominio.
Salida: Una vez que hayas seleccionado una opción, el programa abrirá el navegador web predeterminado con el servicio correspondiente y realizará los análisis pertinentes.

Requisitos
Python 3.x
Las siguientes bibliotecas de Python deben estar instaladas:
webbrowser
pyperclip
pyautogui
colorama

Notas adicionales
Asegúrate de tener una conexión a Internet estable para que el programa funcione correctamente.
Ten en cuenta que este programa utiliza servicios en línea externos para realizar los análisis, por lo que la disponibilidad y la precisión de los resultados pueden variar.
¡Disfruta escaneando y analizando sitios web con IPweb!

