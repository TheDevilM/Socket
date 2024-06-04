#Cliente
import socket
host = "localhost"  # 'localhost' en minúsculas es la convención usual
port = 5656
objsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((host, port))
print("Iniciamos Cliente")

try:
    while True:
        enviar = input("Cliente: ")
        if enviar.lower() == 'exit':
            print("Cerrando conexión...")
            break
        objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))
        recibido = objsocket.recv(1024)
        if not recibido:
            print("Conexión cerrada por el servidor")
            break
        print("Servidor: ", recibido.decode(encoding="ascii", errors="ignore"))
finally:
    objsocket.close()
    print("Conexión cerrada")