a_factaral=f=lambda x:(x>1 and x*f(x-1)-1)+1
print(f(0),f(1),f(2),f(3),f(8),f(10))