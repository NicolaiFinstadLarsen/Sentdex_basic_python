#if statement

#used to "if" something is the case

#often used with assignment operator (< > = etc...)

x = 5
y = 8

if x > y:
    print("x is greater then y")

    x = 5
y = 8

if x < y:
    print("x is not greater then y")

x = 5
y = 8
z = 5

if z < y > x:
    print("y is greater than z and greater than x")

x = 5
y = 8
z = 5
a = 3

if z < y > x > a:
    print("y is greater than z and greater than x and a")
    
x = 5
y = 8
z = 5
a = 3

if z <= x:
    print("z is equal to x")

x = 5
y = 8
z = 5
a = 3

if z == x:
    print("yes, z and x are the same value")

x = 5
y = 8
z = 6
a = 3

if z != x:
    print("z is not equal to x")
#alle disse sier seg selv, ikke sant? Hvis variabel er større, mindre, like eller ikke lik, gjør dette...
    
#en liten ekstra test 
x = 2+1
z = 500

if x == 2 or z == 500:
    print("Alex er EN år")
