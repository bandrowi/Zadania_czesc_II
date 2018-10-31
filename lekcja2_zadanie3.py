#Proszę o napisanie funkcji, która przyjmuje nieokreśloną ilość argumentów
#typu string i jeden argument glue=':'.
#Połączyć wszystkie słowa większe niż 3 litery za pomocą argumentu glue.

def my_function(*args, glue=':'):
    string=''
    for i in args:
        if len(i)>=3:
            string=string+i+glue
    string = string[:-1]
    print(string)

my_function('Adusia','i','chce','mieć','kota','ta','te')
