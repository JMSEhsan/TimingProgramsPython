# Bell, Ana, "Get Programming Learn to Code with Python", Manning, 2018
import time
start = time.process_time()

count = 0
for i in range(1000000):
    count += 1
end = time.process_time()
print(end-start)