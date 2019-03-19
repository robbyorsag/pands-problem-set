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


# Solution to problem 6

First the user inputs a string
Then, the string is split up and made a list using a .split() function.
After that a new list is created and every second word is being indexed [::2] ( :: - means from the begginig till the end and 2 means every second word from the list)
Creating a new string using a "".join() function which joins the list into a string
Print the string

# Solution to problem 7

Input a positive floating point number

make an estimate of the value of square root of the number that we`re trying
to find the square root of

while loop that checks is the squared estimate whitin 0.1 of the actual number, if it is it sets the new value of estimate determined by Newton`s square root approximation 

Prints the number using a formated string format

# Solution to problem 8
import time and datetime modules

set todays date as d_date, using a .datetime.now() function

Using a .strftime() function, convert datetime object into a string
%A -full name of the day in a wekk
%B - full name of the month
%d - day in a month as a number
%Y -year as a number
%I -hour ( 12 hour time)
%M - minutes
%p - PM or AM

# Solution to problem 9

Open the file moby-dick.txt for reading and mark as "f"
with open('moby-dick.txt', 'r') as f

set counter to zero

for line in f: -using a for lopp, loop through every line in the file and count +1 using a count +=1
        if count % 2 == 0: 
if the remainder of the division between count and 2 is 0 ( every other word)

            print(line) 
print line where the remainder is 0


# Solution to problem 10

 Importing matplotlib and numpy libraries

 linspace function in numpy allows us to
pick as many points we want in a certain range in this case that is a 100 points in a range from 0 to 4

plotting the x, x^2 and 2^x and giving 
them labels on the graph using a .plot() function in matplotlib

using a .legend() function in matplotlib that displays the legend on the graph

.show() in matplotlib shows (prints) the graph








