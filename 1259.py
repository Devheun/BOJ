list1=[]
list2=[]

while True:
    number=input()
    if number=="0":break
    length1=len(number)
    length2=int(length1/2)
    for i in range(length2):
        list1.append(number[i])
    for j in range(length1,length1-length2,-1):
        list2.append(number[j-1])
    if list1==list2:print("yes")
    else:print("no")
    list1,list2=[],[]
    