import sys

if len(sys.argv)>1:
    file_name= sys.argv[1]
else:
    file_name = '../dane/logs.txt'  # kropki cofają do do katalogu wyżej a pozniej wchodzę do własciwego folderu

user_last_login = {}
user_total_time = {}

with open(file_name) as f:
    for line in f:
        login, action, time = line.split(';')
        time = int(time)
        if action == "LOGIUN":
            user_last_login [login]=time
        if action == "LOGOUT":
            user_total_time[login]= user_total_time.get(login, 0) + time-user_last_login[login]

def sort_key(x):
    return x[1]

    print ('Czas przebywania w syustemie: ')
    for login in sorted(user_total_time):
        print(f'- {login}: {user_total_time}')    #nie skonczone