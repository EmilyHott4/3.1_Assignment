#this program writes three lines of data to a file
def main():
   outfile = open('philosophers.txt','a')
   outfile.write('Emily Hott' + "\n")

   #close file
   outfile.close
#call main function


#finish with main()
main()
