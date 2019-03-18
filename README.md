# pands-problem-set
# Solution to problem 1 
 Entering a positive integer

 Setting the beggining value from which Python will start to add numbers in the range from 0 up to x+1, to zero 
 (x + 1) - because the "range" function does not include the last number

 sum is set to zero, the range is from 0 to x+1 which means the sum value will change every time the "for" statement loops, 
i.e. sum = sum(0)+x(in the range from 0 to (x+1))
 now the new value of sum = 1, then 2, then 3 and so on up to x+1

 prints the final value of sum


# Solution to problem 2 

 First we need to import date and time with import datetime function so that Python knows how to calculate it

 "if" function works if we set a condition. In this case the condition is days that begin with a letter T.

 Python calculates the number of days in the week by starting with 0 as Monday, and ending with a 6 as Sunday. So, we need 1 and 3 in order to print " Yes today begins with a T"

 If the days are not 1 or 3 a.k.a Tuesday and Thursday Python will then print " No today does not begin with a T"



# Solution to problem 3

Using for loop and range function. For loop will check all the numbersin the range from 1000 to 10000.  10000+1 - because "range" function does not include the last number and we need range from 1000 to 10000

 If number is divisible by 12, and we check that by checking the remainder of the division of that number and number 2, continue looping, don`t print anything, using the continue function

if number is divisible by 6, print the number


# Solution to problem 4

Asking a user to input a positive integer

Printing the entered value

As long as the entered value of n is not equal to 1 (n!=1), function continues to loop. Using a while loop

If the number is divisible by 2, if its an even number, divide the number by 2 ( double forward slash because if we use only one, we will get floating point number) and continue, and if its not divisible by 2, then multiply that number by 3 and add 1

Print number


# Solution to problem 5

Entering a positive number

Using an if statement check that the number is bigger than 1 because we wnat to find out the prime numbers

For loop loops in the range from 2 till whatever number has the user typed in and with an if statement checks if the typed in number is divisible by the number from the range 2 till n.

If it is it prints out that number with a statement that its not a prime number, and breaks the if statement with a break function

using the "else" function, it is determined which number is a prime and is printed on the screen


