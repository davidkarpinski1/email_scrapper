#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup

from urllib.parse import urlparse


def make_request(url: str) -> str:
    try:
        r = requests.get(url)
        return r.text
    except requests.exceptions.RequestException as e:
        print('Error: %s' % e)
        return
    except KeyboardInterrupt:
        return


def parse_data(data: str) -> list[str]:
    try:
        soup = BeautifulSoup(data, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href.startswith('mailto:'):
                print(href.split(':')[1])
    except Exception as e:
        print('Error: %s' % e)
        return
    
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u', '--url', 
        type=str, 
        required=True, 
        help='Target URL (must start with http or https)'
    )
    args = parser.parse_args()
    
    parsed : str = urlparse(args.url)
    if not (parsed.scheme in ("http", "https") and parsed.netloc):
        print('Invalid URL: %s' % args.url)
        return
    
    data = make_request(args.url)
    parsed_data = parse_data(data)


if __name__ == '__main__':
    main()
