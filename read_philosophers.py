#this program reads and sisplays the contents of the philosophers.txt file
def main():
    #open a file named philosophers.txt
    infile = open('philosophers.txt','r')
    #read the file's contents
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')
    print(line1)
    print(line2)
    print(line3)

    #print data from your code
    infile.close
main()