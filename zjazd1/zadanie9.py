import datetime

rok= int(input("Pdaj rok swojego urodzenia"))
data = 2018
pelnoletni=data-rok
zostalo=18-pelnoletni

now=datetime.datetime.now()
print(now)
if pelnoletni >=18:
    print ("Brawo możesz wypić piwko")
else:
    print(f"Musisz jeszcze poczekać {zostalo} lat aby być pełnoletnim")