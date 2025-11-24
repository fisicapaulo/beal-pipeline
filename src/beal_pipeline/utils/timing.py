import time
from contextlib import contextmanager

@contextmanager
def timed():
    t0 = time.time()
    yield lambda: time.time() - t0
