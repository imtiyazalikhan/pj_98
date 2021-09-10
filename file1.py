a=5
b=6
file2 = ("you are in file 2")
data_a= ("you are in file 1")
temp = a
a=b 
b = temp
with open(file2,"w") as a :
    data_a = a.read()
    print(file2)
