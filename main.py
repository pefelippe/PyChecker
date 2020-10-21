import psutil
import time
from datetime import datetime

def convertBytes(B):
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)


##### IMPORTANT: PASS THE PID OF THE PROCESS
PID = 3684

chrome = psutil.Process(PID) 

date = time.strftime('%m-%d-%Y_%H_%M_%S_%Z')

arquive = '{}'.format(date)

log = open(arquive, 'a+')
log.write(date)
log.write('\n')

while True:
    log = open(arquive, 'a+')
    
    cpu = chrome.cpu_percent()
    cpu = cpu/ psutil.cpu_count() # dividir pela quantidade de nucleos da cpu
    ram = chrome.memory_full_info().rss # byte
    ram = convertBytes(ram)
    
    print("CPU: {} %".format(cpu))
    print("RAM: {}".format(ram))
    
    log.write("CPU: {} %".format(cpu))
    log.write('\n')
    log.write("RAM: {}".format(ram))
    log.write('\n')
    
    time.sleep(1)

log.close()