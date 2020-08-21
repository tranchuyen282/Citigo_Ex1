import re
import sys
from datetime import datetime
import glob
import csv
import time
start_time_line = time.time()

list_file = glob.glob("/home/chuyentd/workspace/log_mykiot/log/*")
for file_name in list_file:
    log_file_name = file_name
    csv_file_name = "/home/chuyentd/workspace/log_mykiot/acesslog.log"
    
    file = open(log_file_name)
    f = open(csv_file_name, 'w')
    index = 0
    for line in file:
        f.write(line)
        if index == 10000: break
        index += 1
    f.close()
    file.close()
        

end_time_line = time.time()
print('End convert: {} ms'.format(((end_time_line-start_time_line)*1000)))
