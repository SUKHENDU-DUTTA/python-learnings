from functools import lru_cache
import time

@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")

print(fx(2))
print("done for 2")

print(fx(8))
print("done for 8")

# For the code downward it doesnt takes 5 sec of time

print(fx(20))
print("done for 20")

print(fx(2))
print("done for 2")

print(fx(8))
print("done for 8")