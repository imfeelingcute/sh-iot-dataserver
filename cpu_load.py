import random

try:
    import psutil
except ImportError:
    psutil = None


def get_random_cpu_load():
    """This function returns a random CPU load which can be used if no
    actual CPU load can be determined.

    :return: A random CPU load value between 0% and 100%
    """
    load = random.gauss(55, 10)
    if load < 0:
        return 0.0
    elif load > 100:
        return 100.0
    else:
        return round(load, 1)


def get_maximum_cpu_load():
    """This function returns the maximum CPU load across all CPU cores
    or a random value if the actual CPU load can't be determined.

    :return: Actual CPU load if available, else a random CPU load
    """
    if psutil is not None:
        return max(psutil.cpu_percent(percpu=True))
    else:
        return get_random_cpu_load()
