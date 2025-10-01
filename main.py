#!/usr/bin/env python3

import requests
import argparse

from urllib.parse import urlparse


def make_request(url: str) -> str:
    try:
        r = requests.get(url)
        return r.text
    except requests.exceptions.RequestException as e:
        print('Error: %s' % e)
        return None


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
    
    print(make_request(args.url))


if __name__ == '__main__':
    main()
