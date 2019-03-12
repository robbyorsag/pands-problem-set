# "Solution to problem 5"

num = int(input(" Please enter a positive integer :"))

if num > 1:
   
   for i in range(2,num):
       if num % i == 0:
           print(num,"is not a prime number")
           break
           
           
   else:
       print("That is a prime number")
       
