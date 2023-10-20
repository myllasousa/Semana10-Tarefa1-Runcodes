par = 0
impar = 0
for i in range(100):
    num = int(input(""))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1


print(par)
print(impar)
