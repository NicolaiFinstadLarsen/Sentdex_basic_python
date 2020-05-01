'''
FAQ episode
'''



#!/usr/bi/python
'''
er en shebang linje? brukes ikke i windows, men trenger det i linux. Derfor kan 
det stå på flere scrips. 
'''




    
def epic():
    print("wow this is great")
    
if __name__== "__main__":
    
    print("such good module")
    
#eksempel blokk  
'''  
def epic():
    print("wow this is great")
    
print("such good module")
'''    




'''
Når vi importerer denne modulen fra til et annet script, vil linjen 
if __name__ == "_main__":
sjekke om du kjører denne modulen fra denne(orginale) modulen eller ikke. 
Hvis man ikke kjører fra orginal modul vil dette argumentet blir "False"
og derfor ikke printe begge print argumentene. 
Hvis man ikke bruker denne og flytter print over til en ny blokk, som sett
vil scriptet som importerer printe begge print argumentene.
'''
 


