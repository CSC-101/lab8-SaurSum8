import sys

if __name__ == "__main__":
    l = sys.argv

    try:
        f = open(l[1], 'r')

        vals = f.readlines()

        for i in vals:
            l = i.split()

            try:
                f1 = float(l[0])
                f2 = float(l[1])
                print(f1 + f2)

            except Exception as e:
                print('err for this line :', e)
                continue

        f.close()

    except IOError as e:
        print('err')
        print(e)
        sys.exit(1)
