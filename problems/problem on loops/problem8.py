# Exponential backoff double the wait time for 5 tries and after taht it stops
import time
wait_time=1
max_retries=5
attempts=0
while(attempts<max_retries):
    print("Attempts",attempts+1,"-waittime,wai",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1 
    