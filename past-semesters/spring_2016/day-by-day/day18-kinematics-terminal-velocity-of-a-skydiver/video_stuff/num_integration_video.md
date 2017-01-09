# Numerical integration

"Numerical integration" - term for a family of algorithms that are used to calculate the numerical value of a definite integral.  Also referred to as "numerical quadrature" for historical reasons.

Basic problem is to compute an approximate solution to the integral

\int_a^b f(x) dx 

to some level of accuracy.  Assuming f(x) is a smooth function over x, this is relatively straightforward to do.

Numerical integration used for many reasons

* f(x) may only be known at some points due to sampling (from an experiment, for example)
* A formula for f(x) may be known, but its integral is very hard to calculate analytically.
* It's possible to find an antiderivative analytically, but it's easier to compute the numerical approximation.

Two simplest methods:

1. Rectangle rule 
2. Trapezoidal rule

And then there are much more complex ones.  SciPy has a whole integration library, scipy.integrate, that has a bunch of different integration routines.


## Useful links

* [Wikipedia article on numerical integration](https://en.wikipedia.org/wiki/Numerical_integration)
* [numerical analysis text on numerical integration](http://www.ece.mcmaster.ca/~xwu/part6.pdf)
* [second set of lecture notes](http://pages.cs.wisc.edu/~amos/412/lecture-notes/lecture18.pdf)
* [scipy.integrate docs](http://docs.scipy.org/doc/scipy-0.14.0/reference/tutorial/integrate.html)
* [scipy quad integration](http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html)
* [Gaussian quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature)
