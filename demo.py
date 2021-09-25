import psutil,datetime,time,schedule,openpyxl
pid=int(input("Enter the PID:"))
count=0
def warning():
    cpuusage=psutil.cpu_percent(interval=1)
    if cpuusage>0:
        print("CPU usage is greater than 0%",cpuusage)
    memusage=psutil.virtual_memory().percent
    if memusage>0:
        print("Memory Utillisation is greater than 0%",memusage)

def monitor():
    time=datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    p=psutil.Process(pid)
    cpu=p.cpu_percent(interval=1)/psutil.cpu_count()
    memory=p.memory_percent()

    print("CPU utilisation percent:",cpu)
    print("Memory utilisation percent:", memory)


schedule.every(1).second.do(warning)
schedule.every(3).seconds.do(monitor)

while count<12:
    count+=1
    schedule.run_pending()
    time.sleep(1)
