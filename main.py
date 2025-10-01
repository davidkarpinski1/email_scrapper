#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, required=True)
    args = parser.parse_args()
    
    print(args.url)

if __name__ == '__main__':
    main()
