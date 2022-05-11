from random import randint
from time import sleep

import redis

from settings import REDIS_URL

r = redis.from_url(REDIS_URL)


def main():
    name = randint(69420, 99999)
    r.set(name, "farts")


if __name__ == "__main__":
    while True:
        main()
        sleep(1)
