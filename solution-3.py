# Solution to problem number 3:

for num in range (1000,(10000+1)):
    # 10000+1 - because "range" function
    # does not include the last number and
    # we need range from 1000 to 10000
    if num % 12 == 0:
        continue
    # If number is divisible by 12, continue
    # looping, don`t print anything

    if num % 6 == 0:
        print (num)
    
    # if number is divisible by 6, print 
    # the number
