#classes

'''
understanding what classes are. not to write classes. incase a group, could 
be used instad of modules. Class->module->function
grouping things together. 

lage en kalkulator.
'''

class calculator:
    
    def addition(x,y):
        added = x + y
        print(added)
        
    def subtraction(x,y):
        sub = x - y
        print(sub)
        
    def multiplication(x,y):
        mult = x * y
        print(mult)
        
    def division(x,y):
        div = x / y
        print(div)
    def powerto(x,y):
        powr = x ** y
        print(powr)
        
calculator.powerto(10,5)
