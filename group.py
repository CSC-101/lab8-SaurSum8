
#Function takes a list of integers as input
#Returns a list of lists of integers as output
#These are the same integers but divided into groups of 3, when possible
def groups_of_3(l: list[int]) -> list[list[int]]:

    x = 0
    retL = list()
    t = []

    for i in l:
        if x == 3:
            retL.append(list(t))
            t = []
            x = 0

        t.append(i)
        x += 1

    if len(t) > 0:
        retL.append(t)

    return retL