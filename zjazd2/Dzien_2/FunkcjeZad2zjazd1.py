def pole_trapezu(a, b, h):
    '''

    :param a: - numeric
    :param b: - numeric
    :param h: - numeric
    :return:
    '''


    pole=(a+b)/2*h
    return pole
    #print(f"pole trapezu o podstawach {a} {b} i wysokości {h} wynosi: {pole}")
    # print(f"pole trapezu o podstawach {} {} i wysokości {} wynosi: {}".format(a,b,h, pole))
    # pin=input("podaj pIN: ")
    # print(pin, type(pin))


def test_pole_trapezu ():
    assert pole_trapezu(3, 9, 6.5) == 39.0