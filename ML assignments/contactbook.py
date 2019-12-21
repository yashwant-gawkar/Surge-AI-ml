import csv
import os

current_direct=os.path.dirname(__file__)
filename="Yashwant.csv"
field=['Name','Phone-no','Email','Address']
data=[]

with open(os.path.join(current_direct,filename),'w')as csvfile:
    csvfile1=csv.writer(csvfile)
    csvfile1.writerow(field)
    n=int(input("Enter the number of people you want to include:"))
    for i in range(n):
        data.append([])

    for i in range(n):
        for j in range(0,4):
            data[i].append(j)
            data[i][j]=0
            print("Row:",i+1," col:",j+1," in table")
            data[i][j]=input("Enter person Name,Phone-no,Email,Address:")

    csvfile1.writerows(data)

with open(os.path.join(current_direct,filename),'r')as checkcsv:
    csvread=csv.reader(checkcsv)
    search=input("Enter any person name,person phone-no,person Email,person address you want to search:")
    for a in csvread:
        for i in a:
            if i==search:
                print(a)
            
        
