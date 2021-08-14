s = input()

data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in data:
    if i in s:  #if문 필요 없을듯 
       s = s.replace(i,'a')
print(len(s)) 