def main():
    infile = open('clients.txt','r')
    #count = 1
    #for line in infile:
        #name = line.rstrip('\n')
        #print(str(count) + '.' + name)
        #count = int(count) + 1
    counter = 1
    for line in infile: #(reads each line 1 at a time)
        print(counter, '.', line.rstrip('\n'),sep='')
        counter +=1
    infile.close()


main()