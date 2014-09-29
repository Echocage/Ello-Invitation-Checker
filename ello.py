import os
from threading import Thread
import re
import requests
import sys

def send_request(item):
    req = requests.get('https://ello.co/api/v1/availability/invitation_code?value=' + item)
    if req.json()['available']:
        print 'Key:', item, ' is valid'


if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        print 'Usage: python ello.py filename\n' \
              'Example: python ello.py keys.txt\n'
        exit()
    if not os.path.isfile(args[0]):
        print "Can't find file, quitting"
        exit()

    raw_text = open(args[1], 'r').read()

    for line in re.findall('[a-z]+-[a-z]+-[a-z]+', raw_text):
        print line
        Thread(target=send_request, args=(line,)).start()
