
print("hello world")
print("please input filepath:")
filepath = input()
print("please input filename:")
filename = input()

with open(filepath + filename, 'r') as file:
    lines = file.readlines()