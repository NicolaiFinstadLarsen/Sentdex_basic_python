'''
Reading from a CSV spreadsheet
csv = comma separated value
'''
def example1():
    
    import csv
    with open("example.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        
        for row in readCSV:
            print(row)
            print(row[3])
            print(row[0], row[1])
example1()
            


def example2():
    
    import csv
    with open("example.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        
        dates = []
        colors = []
        
        for row in readCSV:
            date = row[0]
            color = row[3]
            
            dates.append(date)
            colors.append(color)
            
        print(dates)
        print(colors)
        
        whatColor = input("What color whould you like to know the date of?")
        colDex = colors.index(whatColor)
        
        theDate= dates[colDex]
        
        print("The date of",whatColor,"is:",theDate)
         
    
    
example2()

'''
dette skjønte jeg ikke så mye av. Han gikk gjennom veldig fort. 
Example 2 er jeg ikke veldig med på i det hele tatt. 
Jeg regner med at vi lager en variabel som går verdi av inputten vi spør om. 
Vi lager en variabel med indexen til fargen vi svarte. 
Vi lager en variabel hvor vi bruker samme indexen til å finne datoen som samsvarer med denne indexen.
Vi printer både variabelen med fargen vi svarte og variabelen med datoen for samme index. 
'''
