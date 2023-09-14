import csv
infile = open('customers.csv','r')
outfile = open('customer_country.csv','w')
csvfile = csv.reader(infile,delimiter=',')

outfile.write('Fullname, Country' + '\n')
#fullname(fname+lname),country(country)#just need the header for all these
#outfile.write()
next(csvfile)
counter =+ 1
for record in csvfile:
    fname = record[1]
    #print("full name:"),
    lname = record[2]
    country = record[4]

    outfile.write(fname+' ' +lname+','+country +'\n')
    counter =+ 1
    
    #outfile.write = (record[1],' ' record [2],','record[4])
outfile.close()
infile.close()
