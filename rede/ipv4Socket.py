import socket

target=input("Insira o target:")

portas = [21,22,80,443,445,3306,25]#portas p/ serem scaneadas

for x in portas:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)#tempo de espera em segundos
    code = client.connect_ex((target, x))
    if code == 0:
        print(x, "PORT OPEN")
