from datetime import datetime
from time import sleep
from cpu_load import get_maximum_cpu_load
from db import Database


def main(_delay):
    db = Database('cpu_loads.db')
    db.create()
    while True:
        load = get_maximum_cpu_load()
        db.store(load)
        print(f'{datetime.now()}  CPU load = {load}')
        sleep(_delay)


if __name__ == '__main__':
    delay = 30.0
    main(delay)
