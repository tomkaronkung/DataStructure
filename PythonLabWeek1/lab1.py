print("*** Rabbit & Turtle ***")
x,y,z,a=input("Enter Input : ").split()
s = (int(z)*int(x))/(int(z)-int(y))
f = s/int(z)
result =f*int(a)
print('{:.2f}'.format(result))
