def my_function():
    '''definerer min funksjon og navnsetter denne funksjonen.I paranteser(parametere)
    alt som skrives under her er en del av denne funksjonsblokken'''
    print("basic function")
    z = 3+9-1
    print (z)
    #dette er del av denne funksjonen
 
my_function()
'''
her kaller man inn funksjonen når man kjører scriptet.
uten denne startet ikke funksjonen.
'''

def simple_addition(num1,num2):
    answer = num1 + num2
    print("num1 is", num1)
    print("num2 is", num2)
    print("Total is:",answer)

simple_addition(num2=12,num1=15 )
simple_addition(1,2)
