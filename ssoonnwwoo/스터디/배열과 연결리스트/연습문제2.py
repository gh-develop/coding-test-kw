'''
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
 
"Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."
'''

s = "Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."
vowel = ['a', 'e', 'i', 'o', 'u']
l1 = [char for char in s if char not in vowel]#문자열 s에서 for문을 이용해 문자단위로 char변수에 뽑아냄
print("".join(l1))                            #문자(char)가 vowel리스트 안에 없으면 l1에 char추가