from datetime import datetime
import socket
import time

def scan_ports(target, start_port, end_port, delay=0.05):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Error: Unable to resolve hostname '{target}'.")
        return

    print("-" * 55)
    print(f"Scanning Target: {target} ({target_ip})")
    print(f"Port Range:      {start_port} - {end_port}")
    print(f"Time Started:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 55)

    start_time = time.time()
    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port:<5} : OPEN")
                open_ports.append(port)
            else:
                print(f"[-] Port {port:<5} : Closed")
            sock.close()
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
    except socket.error as e:
        print(f"\n[!] Network error occurred: {e}")

    elapsed_time = time.time() - start_time
    print("-" * 55)
    print(f"Scan completed in {elapsed_time:.2f} seconds.")
    print(f"Open ports found: {open_ports if open_ports else 'None'}")
    print("-" * 55)

def main():
    print("=== Basic Ethical Port Scanner ===")
    target = input("Enter target host (ONLY 127.0.0.1 or scanme.nmap.org): ").strip()

    allowed_targets = ["127.0.0.1", "localhost", "scanme.nmap.org"]
    if target not in allowed_targets:
        print("[!] Unauthorized target. Only localhost (127.0.0.1) or scanme.nmap.org is permitted.")
        return

    try:
        start_port = int(input("Enter start port (1-65535): "))
        end_port = int(input("Enter end port (1-65535): "))

        if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
            print("[!] Error: Port numbers must be between 1 and 65535.")
            return
        if start_port > end_port:
            print("[!] Error: Start port must be less than or equal to end port.")
            return
    except ValueError:
        print("[!] Error: Invalid input. Please enter numeric values for ports.")
        return

    scan_ports(target, start_port, end_port)

if __name__ == "__main__":
    main()
