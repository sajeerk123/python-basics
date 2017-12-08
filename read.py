#Final learning https://www.codecademy.com/en/tracks/python
#https://gist.github.com/tombrad/4697060
#https://github.com/paulcarroty/Python-Snippets/blob/master/Coursera%20Programming%20for%20Everybody%20(Python)/8.5%20Lists.py


fh = open("romeo.txt", "r")
count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")