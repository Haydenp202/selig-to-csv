
from warnings import catch_warnings
from numpy._core.defchararray import strip
import pandas as pd

print("please input filepath:")
filepath = input()
print("please input filename:")
filename = input()
lst = []
csvout = filename.split(".")[0] + "clean.csv"

try:
    with open(filepath + filename, 'r') as file, open(csvout, "w") as csv:

        lines = pd.read_csv(filepath + filename,
                            sep=" ",
                            header=None,
                            skiprows=1)  #reads the file
        x = 0
        for line in file.readlines():
            x = x + 1
        i = 0
        while i < x - 1:
            lst.append('0')
            i = i + 1
      
        lines['3'] = lst
        csv.write(lines.to_csv(index=False, header=False, sep=','))  #writes the file

except FileNotFoundError:
    print("File not found. Please check the file path and try again.") #breaks if file does not exist
    exit()

except Exception as e:
    print(f"An error occurred: {e}")#unknown error
    exit()
