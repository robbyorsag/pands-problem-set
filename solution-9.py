# Solution to problem 9



# Open the file moby-dick.txt for reading and mark as "f"
with open('moby-dick.txt', 'r') as f:
    count = 0 # set counter to zero
    for line in f: # for every line in the file
        count+=1 # count +1
        if count % 2 == 0: # if the remainder is 0
            print(line) # print line where the remainder is 0