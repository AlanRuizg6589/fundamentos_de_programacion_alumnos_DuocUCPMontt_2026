import time
from escritura import metSL #Abreviatura de maquina de escribir de tiempo super lento
from escritura import metL  #Abreviatura de maquina de escribir de tiempo lento
from escritura import metM  #Abreviatura de maquina de escribir de tiempo medio
from escritura import metR  #Abreviatura de maquina de escribir de tiempo rapido
metM("Es de noche y estas afuera de una casa abandonada\nViniste por recomendacion de tus amigos. Es un lugar poco conocido\nPara probarte a ti mismo viniste solo al lugar\n")
metL("Buena suerte\n.   .   .\n.   .   .\n")
metM("El pasto es humedo\nNo hay ninguna luz visible a la vista\nNo se escucha nada a la distancia\nFrente a ti esta la casa y una bodega a su lado\n")
time.sleep(1)
Explorar = input("A donde prefieres ir? ")
if Explorar.lower() == "bodega":
    time.sleep(1.5)
    metL("Caminas en direccion a la bodega...\n")
    time.sleep(0.5)
    metM("La puerta se encuentra barricada\nPero por lo menos existen ventanas a los lados\nEsta oscuro\n")
    Linterna1 = input("Prender la linterna? (Si/No) ")
    if Linterna1.lower() == "si":
        time.sleep(1)
        metR("*Tick*\n")
        time.sleep(1)
        metL("Revisas el interior de la bodega por la ventana\n")
        metSL("Nada\n")
        metM("Te vas de la bodega")
    elif Linterna1.lower() == "no":
        print()
    else:
        metL("? ? ?")
elif Explorar.lower() == "casa":
    print()
else:
   metL("? ? ?")