#global and local variable 

x = 6
#dette er ikke en global variabel
def example():
    global x 
    #lager x global variabel
    z = 5 
    print(x+5)
    x+=6
    print(x+5)
#example()

x = 6
#dette er ikke en global variabel
def example2():
    globx = x  
    print(globx)
    globx+=6
    print(globx)
    
    return globx

x = example2()

print(x)
'''vi har endret variablen x til å globx gitt den en ny verdi og satt example 2
til å være x. Når vi printer x etter function får vi altså den nye x'''
