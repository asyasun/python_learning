import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*4
    if prefix == '':
        prefix = random.choice(string.ascii_letters)
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + random.choice(string.ascii_letters)


def random_phone():
    return random.choice(['', ''.join([random.choice(string.digits) for i in range(10)])])


def random_email():
    symbols = string.ascii_letters + string.digits
    return random.choice(['', ' ', ''.join([random.choice(symbols) for i in range(random.randrange(15))]) + '@' +
                          ''.join([random.choice(symbols) for i in range(random.randrange(15))]) + '.ru'])
