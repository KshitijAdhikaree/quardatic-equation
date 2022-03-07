import cmath

print('enter the equation in the form ax^2+bx+c:')

a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))

x1=(-b+cmath.sqrt(b**2-4*a*c))/2*a
x2=(-b-cmath.sqrt(b**2-4*a*c))/2*a

print('the roots are:',x1,'and',x2)
