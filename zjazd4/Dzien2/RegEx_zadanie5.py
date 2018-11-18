'''
w liku wyszukuje all wystpąpienia
kodó pocztowych
adresow e-mail
dat

'''

import re

post_code_pattern = re.compile("^\d{2}-\d{3} | \d{2}-\d{3} | \d{2}-\d{3}$")   #  daszek ^ oznacza początek siągu znaków
e_mail_pattern = re.compile('[\w\.-]+@[\w\.]+')
date_pattern = re.compile("\d{2} \w{3} \d{4}")
with open ('c:/users/kurs/pycharmprojects/bootcamp/zjazd4/Dzien2/input.txt') as f:
    data = f.read()
    print("kody pocztowe"+", ".join(post_code_pattern.findall(data)))
    print("e-maile"+", ".join(e_mail_pattern.findall(data)))
    print("daty"+", ".join(date_pattern.findall(data)))




