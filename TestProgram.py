_author_ = 'Sumukha Nadig'


def retfunc(dic, key):
    return dic[key] #function to return value, in order to sort according to value

def readingfile():
    d = {}
    d2 = {}
    with open('fruits.txt', 'r') as f1: #opening file to read
        f1.readlines()
        f1.seek(0) #point to first line in the file
        for line in f1:
            h = line.split(" ")
            if h[0] in d:
                g = int(d[h[0]])
                d[h[0]] = g + int(h[1].split("\n")[0]) # if item already in dictionary, add previous value and new value
            else:
                d[h[0]] = int(h[1].split("\n")[0]) #if item not in dictionary, add key to dictionary
#********************** At this point, all fruits in text are copied to dictionary with right values *************#
    for item in d:
        val = retfunc(d, item)
        key = int(val)
        d2.setdefault(key, []) #creating a dictionary to add multiple values to key
        if key in d2:
            d2[key].append(item)
        else:
            d2[key].append(item) #dictionary with respect to values
    d2 = sorted(d2.items(), reverse=True)
#********************* Second dictionary now has all sorted fruits according to value *************************#
    with open ('fruits.txt', 'w') as f2:
            for i in range(3):
                if len(d2[i][1]) > 1: #when there arre more fruits with same value, execute the following fucntion
                    for j in range(len(d2[i][1])):
                        f2.write("%s %s\n" % (d2[i][1][j], d2[i][0])) #write all fruits with same value one after the other
                else:
                    f2.write("%s %s\n" % (d2[i][1][0], d2[i][0])) #write fruits in the file
readingfile()