import csv

infile = open('steps.csv','r')
csvfile = csv.reader(infile,delimiter=',')
outfile.write('Month,Steps\n')

#next(csvfile)
MonthNames = ['','Janurary','February','March','April', 'May','June','July','August','September','October','November','December']



totalSteps = 0
dayCount = 0
month = 1

nect(csvfile)

for rec in csvfile:
    if int(rec[0]) == month:
        totalSteps += int(rec[1])
        dayCount += 1
        
        
        
    else:
        avgSteps = (totalSteps/dayCount, 2)
        outfile.write(monthNames[month] + ',' + str(avgSteps) + '\n')
        totalSteps = int(rec[1])
        dayCount = 1
        month += 1

avgSteps = (totalSteps/dayCount, 2)
 outfile.write(monthNames[month] + ',' + str(avgSteps) + '\n')


        


outfile.close()
