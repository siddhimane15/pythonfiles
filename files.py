import os
import datetime
from datetime import datetime
import calendar


print(os)
print(os.path)

if os.path.exists('demo.txt'):
    print("files exist")
    
else:
    print("files not exit")

print(datetime.now()) 

print(calendar.calendar(2025))