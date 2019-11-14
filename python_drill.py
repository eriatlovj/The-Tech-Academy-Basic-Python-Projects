
import os
import sys

path = 'C:\\Users\\Camille\\python_drill'
dirs = os.listdir(path)

for file in dirs:
    print(file)

result = os.path.join('C:\\Users\\Camille\\python_drill','desktop.ini')
print(result)

result = os.path.join('C:\\Users\\Camille\\python_drill','JayO.txt')
print(result)
m = os.path.getmtime(os.path.join('C:\\Users\\Camille\\python_drill','JayO.txt'))
print(m)

result = os.path.join('C:\\Users\\Camille\\python_drill','practice.html')
print(result)

result = os.path.join('C:\\Users\\Camille\\python_drill','Practice1.html')
print(result)

result = os.path.join('C:\\Users\\Camille\\python_drill','practice2.html')
print(result)

result = os.path.join('C:\\Users\\Camille\\python_drill','practice2.html')
print(result)

result = os.path.join('C:\\Users\\Camille\\python_drill','sql_essay.txt')
print(result)
m = os.path.getmtime(os.path.join('C:\\Users\\Camille\\python_drill','sql_essay.txt'))
print(m)

result = os.path.join('C:\\Users\\Camille\\python_drill','test.txt')
print(result)
m = os.path.getmtime(os.path.join('C:\\Users\\Camille\\python_drill','test.txt'))
print(m)

result = os.path.join('C:\\Users\\Camille\\python_drill','testCode3.py')
print(result)

result = os.path.join('C:\\Users\\Camille\\python_drill','testCode4.py')
print(result)

result = os.path.join('C:\\Users\\Camille\\python_drill','testCode5.py')
print(result)










