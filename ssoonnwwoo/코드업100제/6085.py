w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)
result = w*h*b/8/(2**10)/(2**10)
print("%.2f MB"%result)