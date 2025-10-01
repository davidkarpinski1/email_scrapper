#!/usr/bin/env python3

import argparse

from urllib.parse import urlparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u', '--url', 
        type=str, 
        required=True, 
        help='Target URL (must start with http or https)'
    )
    args = parser.parse_args()
    
    parsed = urlparse(args.url)
    if not (parsed.scheme in ("http", "https") and parsed.netloc):
        print('Invalid URL: %s' % args.url)
        return
    
    print(args.url)


if __name__ == '__main__':
    main()
