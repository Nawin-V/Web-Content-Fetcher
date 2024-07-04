import requests
import argparse
import validators

def is_valid_url(url):
    return validators.url(url)

parser = argparse.ArgumentParser(description="Script to fetch content from URL")
parser.add_argument("-u", "--url",nargs='+', help="Enter the target URL")
parser.add_argument("-o", "--output", help="Output filename to save the result")
args = parser.parse_args()
output=""
for url in args.url:
 try:
  r = requests.get(url,timeout=5)
  content= "url"
  print(content)
  print("\n" + "="*120 + "\n") 
  print(r.text)
  output += r.text + "\n" + '=' * 120 + "\n"

 except requests.exceptions.Timeout:
    print("Timeout error for fetching the result from {url}")
 except requests.exceptions.RequestException as e:
    print("error",e)

if args.output:
    with open(args.output, 'w') as file:
        file.write(output)
