#연습1의 해쉬 테이블에 linear probling 기법으로 충돌해결 코드 추가해보기
#해시 함수 : key % 8
#해시 키 생성 : hash(data)

hash_table = [None for i in range(8)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    key = get_key(data)
    hash_code = hash_function(key)
    if hash_table[hash_code] != None:
        for i in range(hash_code, len(hash_table)):
            if hash_table[i] == None:
                hash_table[i] = [key, value]
                return
            elif hash_table[i][0] == key:
                hash_table[i][1] = value
                return
    else:
        hash_table[hash_code] = [key, value]

def get_data(data):
    key = get_key(data)
    hash_code = hash_function(key)

    if hash_table[hash_code] != None:
        for i in range(hash_code, len(hash_table)):
            if hash_table[i]==None:
                return None
            elif hash_table[i][0] == key:
                return hash_table[i][1]
    else:
        return None 

save_data('LEG', '650316')
save_data('JHJ', '610123')

print(hash_table)

print(get_data('JSW'))
save_data('JSW', '990123')

print(hash_table)

print(get_data('JSW'))
save_data('JSW', '981203')
print(get_data('JSW'))
