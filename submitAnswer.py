import requests
import argparse
import subprocess
import sys
# import requests
from decouple import config 
from datetime import datetime

try:
    SESSION = config('SESSION')  #import from env
except:
    SESSION ='<FILL_ME_IN>'

useragent = 'https://github.com/MuhammadSaadSiddique/AdventOfCode/blob/main/get_input.py by muhammadsaad2387@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
time =datetime.now()
print(time.year,time.day)
parser.add_argument('--year', type=int, default=time.year)
parser.add_argument('--day', type=int, default=time.day)
parser.add_argument('--level', type=int, default=1)
parser.add_argument('--answer', type=int, default=0)
args = parser.parse_args()

url=f"https://adventofcode.com/{args.year}/day/{args.day}/answer"

payload = {
    "level": f"{args.level}",
    "answer": f"{args.answer}",
}


# Set up cookies
cookies = {
    "session": f"{SESSION}"  # Replace {SESSION} with your actual session value
}
print(url,payload,cookies)
# Make the POST request
response = requests.post(url, data=payload, cookies=cookies)

print(response.text)