"""https://www.hackerrank.com/challenges/30-review-loop/problem"""2
# solution




T =int(input().strip())
#print(T)
len_str=[]

for i in range(T):
    a=input().strip()
    len_str.append(a)
#print(len_str)
def evnstr_oddstr(len_str):
    for i in len_str:
        even_str=[]
        odd_str=[]
        str =list(i)
        for j in range(len(str)):
            if j % 2 == 0 :
                even_str.append(str[j])
            else:
                odd_str.append(str[j])
        print(''.join(even_str),  ''.join(odd_str))            
evnstr_oddstr(len_str)