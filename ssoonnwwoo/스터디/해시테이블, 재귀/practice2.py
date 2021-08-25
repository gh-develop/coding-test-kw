#연습1의 해쉬 테이블에 chaining 기법으로 충돌해결 코드 추가해보기
#해시 함수 : key % 8
#해시 키 생성 : hash(data)

hash_table =[None for i in range(8)]
print(hash_table)

def get_key(data):
    return hash(data)

def hash_fucntion(key):
    return key % 8

def save_data(data, value):
    key = get_key(data)
    hash_code = hash_fucntion(key)
    if hash_table[hash_code] != None:
        for i in range(len(hash_table[hash_code])):
            if hash_table[hash_code][i][0] == key:#키가 같은 경우, 덮어 씀 
                hash_table[hash_code][i][1] = value
                return
        hash_table[hash_code].append([key, value])
    else:
        hash_table[hash_code] = [[key, value]]

def get_data(data):
    key = get_key(data)
    hash_code = hash_fucntion(key)
    if hash_table[hash_code] != None:
        for i in range(len(hash_table[hash_code])):
            if hash_table[hash_code][i][0]==key:
                return hash_table[hash_code][i][1]
        return None
    else: return None

save_data('Dave','01075536880')
print(hash_table)
save_data('Dave','01046906883')
print(hash_table)
print(get_data('Dave'))

