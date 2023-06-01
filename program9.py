def find(n,char):
    count=0
    for i in n:
        if i in char:
            count+=1
    print(str(char),count)
n=input("enter word : ")
char=input("enter char to count : ")
find(n,char)


s=input("enter word : ")
all_freq={}
for i in s:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
print(str(all_freq))