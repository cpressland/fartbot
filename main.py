import os
import redis
from random import randint
from time import sleep

r = redis.from_url(os.getenv("REDIS_URL", "redis://127.0.0.1:6379"))


def main():
    name = randint(69420, 99999)
    r.set(name, "jarts")


if __name__ == "__main__":
    while True:
        main()
        sleep(1)
