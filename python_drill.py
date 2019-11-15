
import os

import sys

path = 'C:\\Users\\Camille\\python_drill'
dirs = os.listdir(path)
# print(dirs)

for file in dirs:
    
    if file.endswith(".txt"):
        m = os.path.getmtime(os.path.join(path,file))
        print(file,' ',m)

##result = os.path.join('C:\\Users\\Camille\\python_drill','desktop.ini')
##
##
##result = os.path.join('C:\\Users\\Camille\\python_drill','JayO.txt')
##print(result)
##m = os.path.getmtime(os.path.join('C:\\Users\\Camille\\python_drill','JayO.txt'))
##print(m)
##
##result = os.path.join('C:\\Users\\Camille\\python_drill','practice.html')
##result = os.path.join('C:\\Users\\Camille\\python_drill','Practice1.html')
##result = os.path.join('C:\\Users\\Camille\\python_drill','practice2.html')
##result = os.path.join('C:\\Users\\Camille\\python_drill','practice2.html')
##
##
##result = os.path.join('C:\\Users\\Camille\\python_drill','sql_essay.txt')
##print(result)
##m = os.path.getmtime(os.path.join('C:\\Users\\Camille\\python_drill','sql_essay.txt'))
##print(m)
##
##result = os.path.join('C:\\Users\\Camille\\python_drill','test.txt')
##print(result)
##m = os.path.getmtime(os.path.join('C:\\Users\\Camille\\python_drill','test.txt'))
##print(m)
##
##result = os.path.join('C:\\Users\\Camille\\python_drill','testCode3.py')
##result = os.path.join('C:\\Users\\Camille\\python_drill','testCode4.py')
##result = os.path.join('C:\\Users\\Camille\\python_drill','testCode5.py')











