from datetime import datetime, timedelta, date

payday = date(2023, 10, 12)
d = timedelta(weeks=2)
next = payday + d

weeks = 26
payday = date(2023, 10, 12)
for i in range(weeks):
    
    d = timedelta(weeks=2)
    payday = payday + d
    print(payday)
    
