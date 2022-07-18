import time

print("Loading ...")

for i in range(101):
    print("[",i*"*", (100-i)*" ", "]", i, "% complete")
    time.sleep(0.01)