# Numerical differentiation

Numerical differentiation - algorithms for estimating the derivative of a mathematical function using values of that function

As with numerical integration, there are a variety of reasons that you might want to calculate a numerical derivative

* f(x) is only known at specific points
* f(x) is complicated and not very easy to calculate the derivative of (i.e., algebraically it's a mess)
* it's faster to estimate f(x) numerically than to calculate it analytically

Derivative of f(x) at point x can be estimated using two points and calculating the slop of the secant line that connects those points.

can use f'(x) = (f(x+h)-f(x))/h

or f'(x) = (f(x)-f(x-h))/h

but most accurate is 

f'(x) = (f(x+h)-f(x-h))/2h

Note: Slope computed at x but in this case it doesn't use the value at point x

## Useful links

* [Scipy numerical differentiation](http://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.misc.derivative.html)
* [Lecture notes on numerical differentiation](http://www.ece.mcmaster.ca/~xwu/part6.pdf)
* [Wikipedia numerical differentiation](https://en.wikipedia.org/wiki/Numerical_differentiation)
* [Finite difference coefficiencts](https://en.wikipedia.org/wiki/Finite_difference_coefficient)
* []()
