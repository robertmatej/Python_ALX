import datetime

now = datetime.datetime.today()
print(now)
print(now.day)
print(now.weekday)

x = datetime.datetime.strptime('2018/01/31', '%Y/%m/%d')
print (x)

my_birthday = datetime.datetime(1987, 1 ,31)
dzien_tygodnia = my_birthday.weekday()
print(f'Dzień mojego urodzenia: {dzien_tygodnia}')

delta = now - my_birthday

print (f'Ilośc dni od mojego urodzenia: {delta}')

for i in range(20):
    print (now+ datetime.timedelta(hours=i))


