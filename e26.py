'''
vi lager en modul som består av:
    
    
def examplemod.ex(data)
print(data)

denne ligger lagret lokalt nå. 
vi kan da importere denne modulen hvis vi ønsker å bruke den. 
'''

import examplemod
examplemod.ex("test")

'''
vi kan også her bruke de samme import modul triksene
'''


from examplemod import ex as a
a("test2")