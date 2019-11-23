import os 
file = open('test.txt', 'r')



for i in range(1, 10):
    print(file.read())

    file.close()