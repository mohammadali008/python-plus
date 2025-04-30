#### - I.T.N.O.G ---/// MohammadAl/// ---
import csv
from statistics import mean
#### --- Exercise-01 --- get info and write on one file
# counter = 0
# while counter <11:
#     user_info = input('Enter user_info  in firs-name,last-name-age :')
#     with open(r'D:\\project\python\learning\class\info.txt','a') as file:
#         file.write(f"{user_info}\n")
#     counter += 1
    ## --- file.close() is'nt necessary because of that we used 'with expression'
### --- Exercise-02 --- get 10 numbers from user and write mean of them in one file
# user_input = input('Enter 10 nums in num,num,... format :')
# print(mean([float(item)for item in user_input.split(',')]))
# #--- we want to writ this info on a file
# with open(r'info.txt','w') as file:
#     file.write(user_input)
#     file.write(
#         f"The average of data that you entered is{mean([float(item) for item in user_input.split(',')])}"
#     )
### ---Exercise-03 --- read a file and show just lines with 'python'
# with open(r'source.txt','r') as file:
#     for line in file.readlines():
#         if 'python' in line:
#             print(line)
### --- Exercise-04 --- read 'source.csv' and filter students by score>80 in new file.txt
# source_info = open('source.csv','r')
# #data = csv.reader(source_info)
# filtered_data = []
# for item in csv.reader(source_info):
#     for score in item[1:]:
#         if int(score) >= 80:
#             filtered_data.append(item)
# file = open(r'source.txt','a')
# for row in filtered_data:
#     file.write(','.join(row)+'\n')
# file.close()
### --- Exercise-05 - read a txt file and return count of lines
# file = open('source.txt','r')
# print(file.read().count('\n'))






        
