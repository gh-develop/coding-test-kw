s = input().upper()
dic = {}
cnt = 0

for i in set(s):           
    dic[i] = s.count(i)
val = list(dic.values()) 

max_val = max(val)         

cnt = val.count(max_val)                          
                           
if cnt>1:                               
    print('?')
else:
    for key, value in dic.items():
        if value == max_val: 
            print(key)
