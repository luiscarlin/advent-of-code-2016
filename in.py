import requests
import os, sys
from dotenv import load_dotenv

load_dotenv()
year = os.getenv('YEAR')
cookie = os.getenv('COOKIE')

if not year or not cookie:
  print('Need YEAR and COOKIE in .env file')
  sys.exit(1)

day = sys.argv[1] if len(sys.argv) > 1 else ''

if not day:
  print('Need day number as input')
  sys.exit(1)

response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={ 'session': cookie })

if response.status_code is not 200:
  print('Something went wrong with the request!')
  print(response.status_code)
  print(response.text)
  sys.exit(1)

print(response.text)