#get ignore function: takes away files that shouldn't be in your repository(not in gethub)
import csv

infile = open('customers.csv','r')
csvfile = csv.reader(infile,delimiter=',')#how you tell python how to seperate the commas based on the delimiter

next(csvfile) #this skips the first line
for record in csvfile:
    print('student ID:',record[0])
    print('Firstname:',record[1])
    print('Lastname:',record[2])
    print('City:', record[3])
    print('Country:',record[4])
    print('Phone:',record[5])

    input()

    #print(record)#record is a list, you know because of the square bracket
    #need the list index that starts at 0 
    