import sys

if __name__ == "__main__":
    l = sys.argv #Takes run agrument from cmd line, stores it in a list

    try:
        f = open(l[1], 'r') #Try to open file from given name 

        vals = f.readlines() #Put file data into a list, line by line

        for i in vals:
            l = i.split() #Further split string into two separate values

            try:
                f1 = float(l[0]) #Try to convert them to float
                f2 = float(l[1])
                print(f1 + f2) #Print sum if successful

            except Exception as e:
                print('err for this line :', e) #Otherwise print error if failed to convert to float
                continue

        f.close() #Close the file at the end of program

    except IOError as e:
        print('err') #Print error if there is any error in opening the file
        print(e)
        sys.exit(1)
