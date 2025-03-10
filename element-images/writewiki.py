import csv

f=open("elements.csv",'r')
g=open('wiki.txt','w')

reader=csv.reader(f)


for i in reader:
    name=i[1]

    link= 'https://en.wikipedia.org/wiki/'+name+'\n'

    g.writelines(link)


print("link written successfully")

g.close()
f.close()
