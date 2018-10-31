#Proszę wprowadzić liczbę (funkcja_input), jeżeli liczba jest
#parzysta - ValueError, jeżeli liczba< 0 - TypeError,
#jeżeli liczba> 10 - IndexError. Proszę wychwycić wyjątek i
#powiedzieć użytkowniku w czym jego problem.

e=input("Podaj liczbę, od której mam liczyć: ")
e=int(e)
try:
    if e%2==0:
        raise ValueError('Ta liczba jest parzysta')
    if e<0:
        raise TypeError('Ta liczba jest mniejsza od zera')
    if e>10:
        raise IndexError('Ta liczba jest wieksza od 10')
except ValueError as a:
    print(a)
except TypeError as a:
    print(a)
except IndexError as a:
    print(a)
