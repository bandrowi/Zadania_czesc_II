#Proszę o napisanie funkcji, która otrzymuję jakąkolwiek
#ilość agrumentów,znajduje max i min i wyprowadza do konsoli.

def my_function(*args):
    print("Najmniejsza wartość z zakresu to: ", min(args))
    print("Najwieksza wartość z zakresu to: ", max(args))

my_function(1,2,3,55,67,1,4,6,7)
