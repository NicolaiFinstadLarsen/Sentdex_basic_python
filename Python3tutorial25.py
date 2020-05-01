'''
e25
snakker om hvordan man kan forkorte importerte moduler.
'''

example_list = [1,2,3,4,5,6,7,8,9,0]


class episode25:
    def part1():
        global example_list
    
        import statistics as s
        
        x = s.mean(example_list)
        
        print("1 The mean is: ", x)
        
        y = s.stdev(example_list)
        print("1 standard div si: ", y)
        
        z = s.variance(example_list)
        print("1 Variance is: ", z)
    part1()

    '''
    over her importerer vi statistikk modulen og forkorter "the call" til "s"
    '''

    def part2():
        from statistics import mean 
        
        x = mean(example_list)
        
        print("2 The mean is: ", x)
    part2()

    '''
    over her importerer vi FRA modulen statistikk BARE mean og da trenger vi 
    referere til moduel, vi kan call bare mean.
    '''

    def part3():
        
        from statistics import mean as m 
        
        
        x = m(example_list)
        
        print("3 The mean is: ", x)
    part3()

    '''
    over her slår vi begge sammen og alt vi trenger å "calle" er "m".
    Veldig kjapt, men kan bli forvirrende?
    '''

    def part4():
            
        from statistics import mean, stdev, variance 
        
        x = mean(example_list)
        
        print("4 The mean is: ", x)
        
        y = stdev(example_list)
        print("4 standard div si: ", y)
        
        z = variance(example_list)
        print("4 Variance is: ", z)
    part4()
    
    '''
    ved bruk av komma, kan vi mportere akkurat de delene av modulen vi vil 
    bruke
    '''

    def part5():
        from statistics import mean as m, stdev as s, variance as v
        
        x = m(example_list)
        
        print("5 The mean is: ", x)
        
        y = s(example_list)
        print("5 standard div si: ", y)
        
        z = v(example_list)
        print("5 Variance is: ", z)
    part5()
    
'''
her forkorterer vi igjen alle delene vi har valgt å importerer fra modulen,
man bruker "as" for hver importerte opperator.
'''

from statistics import *

example_list = [1,2,3,4,5,6,7,8,9,0]

x = mean(example_list)

print("6 The mean is: ", x)

y = stdev(example_list)
print("6 standard div si: ", y)

z = variance(example_list)
print("6 Variance is: ", z) 


'''
Har bruker man * for å importerer alle deler av modulen statistics. Denne 
muligheten kan man bare bruke i moduler. Derfor gikk det ikke når jeg 
hadde den satt i en class. Tror jeg?
Man kan da bruke mean, stdev, variance og slipper å skrive 
statisticks.stdev().
'''

    