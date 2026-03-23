import time

def metSL(texto): #Abreviatura de maquina de escribir de tiempo super lento
    listTexto = list(texto)
    for char in listTexto:
        print(char, end="", flush=True)
        time.sleep(0.2)
    return ""
def metL(texto): #Abreviatura de maquina de escribir de tiempo lento
    listTexto = list(texto)
    for char in listTexto:
        print(char, end="", flush=True)
        time.sleep(0.12)
    return ""
def metM(texto): #Abreviatura de maquina de escribir de tiempo medio
    listTexto = list(texto)
    for char in listTexto:
        print(char, end="", flush=True)
        time.sleep(0.07)
    return ""
def metR(texto): #Abreviatura de maquina de escribir de tiempo rapido
    listTexto = list(texto)
    for char in listTexto:
        print(char, end="", flush=True)
        time.sleep(0.03)
    return ""