'''
Multi-dimensional List
'''

'''
man kan ha lister i lister i lister i lister
'''
def example1():
    x = [
        [1],[2,1],
        [2,4]
        ]
    # 2 dimmensjons liste
    
    print(x)
    
    print(x[2])
    #vi printer listen i listen med index nr 2, burde da være 2 og 4 
    
    print(x[2][0])
    '''
    Vi printer listen i listen med index nr to, men vi printer bare 
    tallet med index 0 i den listen, burde være 2
    '''
example1()

def example2():
    x = [
        [[5,7],[6,6]],
        [[6,6],[7,8]],
        [7,2],[2,5]
        ]
    
    '''
    vi sorterer listen i brakets, dette gjør det litt lettere å se hvor vi er i listen. 
    her vil vi printe ut fra listen, subliste index 1 som er 6,6 og 7,8
    vi vil også bare ha subliste del index 0, som er 6,6 
    og til slutt bare subliste del index 0, som er 6
    '''
    
    print(x[1][0][0])
    
example2()