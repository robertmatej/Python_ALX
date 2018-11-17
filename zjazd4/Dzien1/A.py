import B       #jeszcze działa OK
#from B import bar       # probmel z importowaniem  o ile jest imp0oirt w drugiej funkcji do tej
print ('jestem w module A')

def foo():
    return "foo z modułu A"

print (foo())


# rzeczy z biblioteki standardowej
import sys
import OS
import CSV


# rzeczy biblikoteki zewnetrznej

import pip


# moduły z naszej aplikacji
import B

