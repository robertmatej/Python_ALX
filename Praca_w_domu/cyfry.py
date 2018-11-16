import sys

wejscie = list()
for wej in sys.argv:
    wejscie.append(wej)

lacznik=''
wejscie_zlacz = lacznik.join(wejscie)

print(wejscie_zlacz)

jeden = '''
   *
  **
 * *
   *
   *
   *
  ***
'''

dwa = '''
   * *
  *   *
      *
     * 
   *
  *   
  *****
'''

trzy = '''
   * *
  *   *
      *
     * 
      * 
  *   *
   * *
'''

cztery = '''   
     *
    * 
   *
  *  *
 ******
     *
     *

'''

piec = '''
  ******
  *   
  * *
      * 
       * 
  *   *
   * *
'''

szesc = '''
   * *
  *   
  *    
  ****
  *   * 
  *   *
   * *
'''
siedem = '''
  * * * *
       *     
      *
     *  
    *
   *   
  *
'''
osiem= '''
   * *
  *   *
  *   *
   * * 
  *   * 
  *   *
   * *
'''
dziewiec = '''
   * *
  *   *
  *   *
   ****
      * 
  *   *
   * *
'''
zero= '''
   * *
  *   *
  *   *
  *   *
  *   * 
  *   *
   * *
'''

wyjscie = list()

test = [jeden, dwa, trzy]

for wyj in wejscie_zlacz:
    if wyj == '1':
        wyjscie.append(jeden)

    elif wyj == '2':
        wyjscie.append(dwa)

    elif wyj == '3':
        wyjscie.append(trzy)

    elif wyj == '4':
        wyjscie.append(cztery)

    elif wyj == '5':
        wyjscie.append(piec)

    elif wyj == '6':
        wyjscie.append(szesc)

    elif wyj == '7':
        wyjscie.append(siedem)

    elif wyj == '8':
        wyjscie.append(osiem)

    elif wyj == '9':
        wyjscie.append(dziewiec)

    elif wyj == '0':
        wyjscie.append(zero)


for rys in wyjscie:
    print (rys, end=''),
#    print(f"test{test}")