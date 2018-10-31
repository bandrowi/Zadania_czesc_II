#Proszę o napisanie funkcji, która ma 2 argumenty:
#str i flagę (jako typ bool), która domyślnie jest ustawiona na True.
#Jeżeli flaga jest prawdziwa - to proszę wyprowadzić string do konsoli
#duzymi literami,jak nie -małymi.

def my_function(string,arg=True):
    if arg==True:
        return string.upper()
    else:
        return string.lower()
print(my_function("tekst"))

