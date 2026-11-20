import socket

def start_server(host="127.0.0.1", port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[*] Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"[+] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[-] Client disconnected.")
                    break
                message = data.decode("utf-8")
                print(f"[Client]: {message}")
                response = f"Server received: '{message}'"
                conn.sendall(response.encode("utf-8"))
    except KeyboardInterrupt:
        print("\n[!] Server shutting down manually.")
    except socket.error as e:
        print(f"[!] Socket error: {e}")
    finally:
        server_socket.close()
        print("[*] Server socket closed.")

if __name__ == "__main__":
    start_server()
