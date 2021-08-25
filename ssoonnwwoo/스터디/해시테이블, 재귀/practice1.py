#리스트 변수를 활용해 해시테이블 구현해보기
#해시 함수 : key % 8
#해시 키 생성 : hash(data)

hash_table = [None for i in range(8)]
print (hash_table) 
#[None, None, None, None, None, None, None, None]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    key = get_key(data)
    hash_code = hash_function(key)
    hash_table[hash_code] = value

def get_value(data):
    key = get_key(data)
    hash_code = hash_function(key)
    return hash_table[hash_code]

save_data("pizza", '20.0$')
save_data("pasta", '10.0$')

print(get_value('pizza'))#20.0$
print(get_value('pasta'))#10.0$
