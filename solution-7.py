# Solution to problem 7

rootof =float(input(" Please enter a positive floating point number : ")) 
# Input a positive floating point number

estimate = (rootof / 2) - 2
# make an estimate of the value of square root of the number that we`re trying
# to find the square root of

while abs((estimate * estimate)-rootof) > 0.1:
    estimate -= ((estimate * estimate)-rootof) / (2 * estimate)

# while loop that checks is the squared estimate whitin 0.1 of the actual number, if it is
# it sets the new value of estimate determined by Newton`s square root approximation 

print(f"The square root of {rootof} is approx.{estimate}.")
 #Prints the number that we`re looking the square root of, and the estimate of the
 # square root.


