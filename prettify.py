#!/usr/bin/env python3

# prettify.py
# Usage: prettify <URL>

import sys
import urllib.request
from bs4 import BeautifulSoup


class Downloader:
    def __init__(self, url):
        self.url = url

    def download(self):
        response = urllib.request.urlopen(self.url)
        text = response.read()
        soup = BeautifulSoup(text, "html.parser")
        return soup.prettify()


def main():
    if len(sys.argv) == 1:
        print("HTML Downloader v0.1")
        print("Usage: %s <URL>" % sys.argv[0])
    else:
        downloader = Downloader(sys.argv[1])
        print(downloader.download())


if __name__ == "__main__":
    main()
