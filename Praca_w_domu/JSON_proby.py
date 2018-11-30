import json

a = ['ala', 'ma ',2 , 'koty']
a_as_json = json.dumps(a)
b = ['albo', ' i ', 6, 'sierściuchów']
print (a_as_json)
for add in b :
    a.append(add)
#    print(b)
fp=1
b_json = json.dumps(a)
c= json.loads(b_json)
print (b_json)
print (c)