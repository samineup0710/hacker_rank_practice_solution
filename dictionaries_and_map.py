"""QUESTIONS LINK: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem """
N = int(input())
phonebook ={}
#print(N)
# enter name and number by separate space
for i in range(N):
  name, phn = input().split(  )
  phonebook.update({name:phn})
# Enter name in order to get phone number
for i in range(0, N):
    try:
        name = input()
        if name in phonebook:
            print("{}={}".format(name, phonebook[name]))
        else:
            print("Not found")
    except:
        break
