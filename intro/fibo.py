def fibo(n):
    x, y = 1, 1
    for _ in range(n-2): # anonymous var _
        x, y = y + x, x
    
    return x

n = 20
for i in range(n):
	print(fibo(i))