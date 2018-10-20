
# program liczący samogłoski (a e i o u y) w napisie podanym przez usera

print('Wprowadź napis, policzymy samogłoski')

end = 'a'
while end != 'q':
    napis = str(input('Wprowadź tekst: '))
    test = 0
    licz = 0
    i = 1
    for test in napis:

        if test == 'a' or test == 'e' or test == 'i' or test == 'o' or test == 'u' or test == 'y':
            licz += 1
        i += 1
        if i > len(napis):
            break

    print(f'Liczba samogłosek w napisie wynosi:  {licz}')
    end = input('Czy zakończyć program? Wciśnij "q" aby zakończyć: ')