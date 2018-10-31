#Stworzyć listę. Użytkownik może wprowadzić index listy
#który chcę zobaczyć – jeżeli taki index istnije –
#proszę wyprowadzić jego do konsoli, jeżeli nie –
#proszę zgłosić wyjątek z jego opisem.

lista=('Ada', 'Michał', 'Klarcia', 'Krzysiu', 'Janeczka')
e=input("Podaj indeks który chcesz odczytać: ")
e=int(e)

try:
    if e>len(lista)-1 or e<0:
        raise IndexError('Indeks jest poza zakresem')
    else: print(lista[e])
except IndexError as a:
    print(a)
