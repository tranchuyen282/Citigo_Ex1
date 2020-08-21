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
    csv_file_name = "/home/chuyentd/workspace/log_mykiot/{}.csv".format(str(file_name)[-12:]+'_ngnix2')
    pattern = re.compile(r'(?P<host>\S+).(?P<rfc1413ident>\S+).(?P<user>\S+).\[(?P<datetime>\S+ \+[0-9]{4})]."(?P<httpverb>\S+) (?P<url>\S+) (?P<httpver>\S+)" (?P<status>[0-9]+) (?P<size>\S+) "(?P<referer>.*)" "(?P<useragent>.*)"\s*\Z')

    file = open(log_file_name)
    with open(csv_file_name, 'w',newline='') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['host', 'ident', 'user', 'time', 'verb', 'url', 'httpver', 'status', 'size', 'referer', 'useragent'])

        for line in file:
            m = pattern.match(line)
            result = m.groups()
            list_result = list(result)
            list_result[3] = datetime.strptime(list_result[3], '%d/%b/%Y:%H:%M:%S +0700')
            result = tuple(list_result)
            csv_out.writerow(result)

end_time_line = time.time()
print('End convert: {} ms'.format(((end_time_line-start_time_line)*1000)))
