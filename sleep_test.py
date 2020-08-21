from time import sleep,perf_counter
from motor import left
start=perf_counter()
sleep(0.3)
end=perf_counter()
print(end-start)