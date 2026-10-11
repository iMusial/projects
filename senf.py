import requests, argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("domain", help="target domain for subdomain discovery")
parser.add_argument("-l", "--leet-mode", help="for those who are worthy", action="store_true")
args = parser.parse_args()

if args.leet_mode:
        print("test")

target = args.domain

url = "http://" + args.domain
response = requests.get(url)

print(response) #prints status code
rawHTML = response.text #saves raw HTML, pass to BeautifulSoup
