import os.path
import jsonpickle
import getopt
import sys
from model.Contact import Contact
from test.different_methods import random_string, random_email, random_phone


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage(0)
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


test_data = [Contact(name="", sec_name="", last_name="", nickname="", company="", phone="",
                     mobile="", work_phone="", secondary_phone="", email="")] + [
             Contact(name=random_string('', 10), sec_name=random_string('', 10), last_name=random_string('', 20),
                     nickname=random_string('', 15), company=random_string('', 25), address=random_string('', 100),
                     phone=random_phone(), mobile=random_phone(), work_phone=random_phone(),
                     secondary_phone=random_phone(), email=random_email(),
                     email2=random_email(), email3=random_email())
             for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(test_data))
