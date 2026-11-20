import socket

def start_client(host="127.0.0.1", port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5.0)

    try:
        print(f"[*] Attempting to connect to {host}:{port}...")
        client_socket.connect((host, port))
        print("[+] Connected to server! Type 'exit' to disconnect.\n")

        while True:
            message = input("Enter message to send: ")
            if message.lower() == "exit":
                print("[*] Disconnecting from server...")
                break
            client_socket.sendall(message.encode("utf-8"))
            data = client_socket.recv(1024)
            print(f"[Server]: {data.decode('utf-8')}\n")
    except ConnectionRefusedError:
        print("[!] Connection failed: The server is not running or refused the connection.")
    except socket.timeout:
        print("[!] Connection timed out.")
    except socket.error as e:
        print(f"[!] Socket error: {e}")
    finally:
        client_socket.close()
        print("[*] Client socket closed.")

if __name__ == "__main__":
    start_client()
