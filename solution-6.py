welcome = input (" Enter a string : ")
words = welcome.split()
new_list = words[::2]


words = " ".join(new_list)
print(words)