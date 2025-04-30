#- reading mode
data = open('D:\project\python\learning\class\data.txt','r') #-as read mode
print(data.read(1)) # one character
print(data.readline()) # print all lines as string
print(data.readlines()) # print all lines as list
#- writing mode
data = open('D:\project\python\learning\class\data.txt','w') #-as read mode
data.write(
    "That's new thing that I want to mention"
)
data.close()
#- Appending new things to our file
data = open('D:\project\python\learning\class\data.txt','a') #-as append mode
data.write('new item')
data.close()
#- Example 01
data = open('D:\project\python\learning\class\data.txt','r')
lines = data.readline()
print(len(lines))
#- Example02
data = open(r'D:\\project\python\learning\class\data.txt','r')
print('Count of words is :',len(data.readline().split()))
#- Example03
data = open(r'D:\\project\python\learning\class\data.txt','r')
context = data.readline().split()
for item in context:
    if len(item) == 5:
        print(item)
#- Example 04
data = open(r'D:\\project\python\learning\class\data.txt','r')
context = data.readline()
count_of_uppercase,count_of_lowercase,count_of_integer = 0
for char in context:
    if char.isupper():
        count_of_uppercase +=1
    elif char.islower():
        count_of_lowercase +=1
    elif char.isdigit():
        count_of_integer +=1

# Print and Test
print('Count of Uppercases  :',count_of_uppercase)
print('Count of Lowercases  :',count_of_lowercase)
print('Count of Integers  :',count_of_integer)
#- Example 06
#   
    

