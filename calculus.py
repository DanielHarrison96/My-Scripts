import math 
#math was only imported to allow ease of testing the code

#f is the function, a and b the limits of integration and N the number of strips
def integ(f, a, b, N):
    # f: function. a,b: lower and upper lims. N: number of strips
    a, b = a * 1.0, b * 1.0 #make limits floats
    h = (b - a)/N #strip width
    if N % 2 == 1:
        raise Exception('N must be even.') # ensures even number os strips
    result = f(a) + f(b)
    for i in range(1, N):
        result += f(a + h * i) * (2 * (i % 2) + 2)
    return (h/3)*result
    #this is Simpson's rule of numerical integration

#f is the function, x is the point at which the deriv will be calculated and dx is 
#the interval size
def diff(f, x, dx):
    x *= 1.0
    return (f(x+dx)-f(x-dx))/(2.0*dx)
    
    