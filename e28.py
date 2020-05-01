'''
list manipulation
'''

x= [1,2,3,4,5,6,7,8,9,10,11]

x.append(2)
#vi legger til en 2 i listen. Kan ikke gjøres med tuple.

print(x)

x.insert(0,99)
#legger inn tallet 99 i index 0 i listen.

print(x)

x.remove(1)
#fjerne det første tallet av den verdien vi legger inn.

print(x)

x.remove(x[2])
#fjerner tallet i liste x med index 2.

print(x)

print(x[5:8])
#lager en slice av listen. Printer ut tallet fra og med index 5 til og med index 7.

print(x[-1])
#printer ut det siste tallet i listen.


print (x)
print(x.index(5))
#printer ut hvilken index i listen tallet 5 har.


print(x)
print(x.count(99))
#printer ut hvor mange ganger tallet 99 finnes i listen.

y =["Janet", "James", "Alice", "Bob", "Connor"]
x.sort()
y.sort()

print(x)
print(y)
#sorterer listen i stigende rekkefølge eller alfabetisk.

