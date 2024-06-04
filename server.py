#Servidor
import socket
host = "localhost"  # 'localhost' en minúsculas es la convención usual
port = 5656
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("Servidor en espera de conexiones")

active, addr = server.accept()
print(f"Conexión establecida con {addr}")

try:
    while True:
        recibido = active.recv(1024)
        if not recibido:
            print("Conexión cerrada por el cliente")
            break
        print("Cliente: ", recibido.decode(encoding="ascii", errors="ignore"))
        enviar = input("Server: ")
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
finally:
    active.close()
    print("Conexión cerrada")