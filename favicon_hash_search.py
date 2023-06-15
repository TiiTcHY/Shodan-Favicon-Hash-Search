import base64
import mmh3
import requests

SHODAN_API_KEY = 'your_shodan_api_key'

def get_favicon_hash(favicon_url):
    response = requests.get(favicon_url)
    favicon = response.content
    favicon_base64 = base64.encodebytes(favicon)
    favicon_hash = mmh3.hash(favicon_base64)
    return favicon_hash

def search_shodan(favicon_hash):
    shodan_url = f'https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query=http.favicon.hash:{favicon_hash}'
    response = requests.get(shodan_url)
    data = response.json()
    return data['matches']

def main():
    favicon_url = input('Enter the favicon URL: ')
    favicon_hash = get_favicon_hash(favicon_url)
    print(f'Favicon hash: {favicon_hash}')
    results = search_shodan(favicon_hash)
    for result in results:
        print(f'IP: {result["ip_str"]}, Port: {result["port"]}, Hostnames: {result["hostnames"]}')
    else:
        print(f'No results found for the following favivon hash: {favicon_hash}')

if __name__ == '__main__':
    main()