a = int(input("введите число a:")) 
b = 0
while a>0:
    b = b*10 + a%10
    a = a//10
print(b)