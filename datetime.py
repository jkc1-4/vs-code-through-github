date=input('Enter a date(mm/dd/yyy)')
replace=date.replace('/',' ')
convert=replace.split()
day=convert[1:2]
year=convert[2:4]
for ch in convert:
    if ch[:2]=='01':
        print('January ',day,year )
