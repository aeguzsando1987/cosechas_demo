import platform
import os
import time
import uuid

def cls_pantalla():
    sist = platform.system()
    if sist == "Windows":
        os.system('cls')
    else: # Linux
        os.system('clear')
        
        
def espera(mensaje="Espere por favor...", segundos=1.5, puntos=3):
    intervalo = segundos / puntos
    for i in range(puntos):
        print(f"\r{mensaje}{'.'*(i+1)}", end='', flush=True)
        time.sleep(intervalo)
    print()
    
    
def encoder_prueba():
    return str(uuid.uuid4()).replace('-','')[:20]