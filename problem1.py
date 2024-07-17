#Problem 1
input_string = input("Enter the passcodes in a horizontal format: ")
b=list(map(str,input_string.split()))
# Solution 1
b = sorted(b, key=lambda x: x[0])
flag=True
i=0
j=1
ll=[]
j1=len(b[0])
while(flag):
    str=""
    for k in b:
        str=str+k[j]
    ll.append(str)
    j=j+1
    if(j==j1):
        flag=False
print("Output : ")
for ii in ll:
      print(ii)

# solution 2
b = sorted(b, key=lambda x: int(x[0]))
print(b)
c = [j1[1:] for j1 in b]
print(c)
p = [''.join(i) for i in zip(*c)]
print(p)
for ii in p:
    print(ii)