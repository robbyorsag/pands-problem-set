# Solution to problem 10

import numpy as numpy
import matplotlib.pyplot as pyplot

# Importing matplotlib and numpy libraries



x = numpy.linspace(0,4,100)
# linspace function in numpy allows us to
# pick as many points we want in a certain range
# in this case that is a 100 points in 
# a range from 0 to 4
pyplot.plot(x,x, label = "x")
pyplot.plot(x,x**2,label = "x^2")
pyplot.plot(x,2**x,label ="2^x")
# plotting the x, x^2 and 2^x and giving 
# them labels on the graph

pyplot.legend()
# function that displays the legend on the graph


pyplot.show()

# showing (printing) the graph