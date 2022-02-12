# Lucas Ramos
# Redes, Port Scanner.

import socket
import sys

# Recebendo host para escanear 
print ("\n--------------------Welcome-to-Port-Scanner-----------------------")
entrada = input("-     Escreva o host para buscar: ex: ufmt.br ou 200.17.60.5     -\n")
busca = socket.gethostbyname(entrada)

print ("------------------------------------------------------------------")
print ("-        Escaneando host informado...              " + busca+"   -")
print ("------------------------------------------------------------------")

# Para realizar o scanner de portas devemos entender que existe tres intervalos para realizar as buscas
# Porém, como já notorio se informar todas as portas possiveis a execução iria levar horas se não dia;
# O range de portas conhecidas vai de 0-1023 e são nessas que vamos buscar, as portas registradas vai de 1024 ate 49151
# Por fim, as portas privadas ou dinamicas vão de 49152 ate 65535, 
# ou seja, para buscar todas seria de 0 ate 65535...

try:
    for porta in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = sock.connect_ex((busca, porta))
        if resultado == 0:
            stateHost = socket.getservbyport(porta)
            print ("-        Porta {}: Aberta; Serviço: ".format(porta) + stateHost + ".")
        sock.close()
    print ("------------------------------------------------------------------")
except socket.error:
    print ("Host informado nao pode ser buscado, por favor informe outro host...")
    sys.exit()