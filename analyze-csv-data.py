import csv
data = open('data.csv','r')
context = csv.reader(data)
for item in context:
    info = []
    name = item[0]
    for j in item[1:]:
        info.append(float(j))
        #... mean-min-max
        
