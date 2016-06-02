import time
class bcolors:
    Morado = '\033[95m'
    Azul = '\033[94m'
    Verde = '\033[92m'
    Amarillo = '\033[93m'
    Rojo = '\033[91m'
    Negrita = '\033[1m'
    Subrayado = '\033[4m'
    normal = '\033[0m'

print bcolors.Morado + 'encontrando a luis...' +bcolors.normal
time.sleep(3)
print bcolors.Verde + 'luis encontrado' +bcolors.normal
time.sleep(1)
print bcolors.Rojo + 'partiendole las piernas a luis...' +bcolors.normal
time.sleep(3)
print bcolors.Azul + 'piernas de luis partidas' +bcolors.normal
time.sleep(1)
print bcolors.Amarillo + 'enhorabuena' +bcolors.normal