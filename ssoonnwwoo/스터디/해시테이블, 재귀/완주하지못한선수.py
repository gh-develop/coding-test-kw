
hash_table = [[] for _ in range(100000)]#해시 테이블 

def get_key(data):
    return hash(data)

def hash_function(key):#해시함수 ==> 100000으로 나누기
    return key % 100000

def save_data(parti):#(key, value) 형태로 만들어줌
    for i in parti:
        key = get_key(i)
        hash_code = hash_function(key)
        hash_table[hash_code].append([key, i])#chaining으로 충돌 방지

def del_data(compl):#hashtable에서 completion에있는 놈들을 지움
    for i in compl:
        key = get_key(i)
        hash_code = hash_function(key)
        for i in hash_table[hash_code]:
            if i[0] == key:
                hash_table[hash_code].remove(i)
                break

def check_loser():#누가누가 못들어왔나
    for i in hash_table:
        if i :
            return i[0][1]

def solution(participant, completion):
    save_data(participant)
    del_data(completion)
    answer = check_loser()
    return answer

# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))