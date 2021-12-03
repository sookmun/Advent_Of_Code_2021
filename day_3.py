def partOne():
    with open('day3_input.txt') as file:
        file=file.readlines()
        gamma=""
        epsilon=""
        length=len(file[0])
        lst=[]
        for x in range(length-1):
            lst.append([0,0])
        # print(lst)
        for line in file:
            print(line)
            for index in range(length-1):
                if line[index]=="0":
                    lst[index][0]+=1
                elif line[index]=="1":
                    lst[index][1]+=1
                else:
                    print("wrong")
        print(lst)
        for item in lst:
            max_val=max(item)
            max_index=item.index(max_val)
            min_val = min(item)
            min_index = item.index(min_val)
            gamma+=str(max_index)
            epsilon+=str(min_index)
            print("gam",gamma)
            print("epi",epsilon)

        a=int(gamma,2)
        b=int(epsilon,2)
        print(a*b)
        print("gamme",gamma,int(gamma,2))
        print("epsolone",epsilon,int(epsilon,2))

def get_max(file,index,kind):
    one=0
    zero=0

    for line in file:
        line=line.strip('\n')

        if line[index]=="0":
            zero+=1
        elif line[index]=="1":
            one+=1
        else:
            print("wrong")
    print("zero:",zero,"one:",one)
    if zero==one:
        if kind=="02":
            return ("1","weird")
        else:
            return "0"
    elif zero>one:
        return "0"
    else:
        return "1"

def get_min(file,index):
    one=0
    zero=0

    for line in file:
        line=line.strip('\n')

        if line[index]=="0":
            zero+=1
        elif line[index]=="1":
            one+=1
        else:
            print("wrong")
    print("zero:",zero,"one:",one)
    if zero==one:
        return "0"
    elif zero>one:
        return "1"
    else:
        return "0"

def filter(lst,index,value):
    ret=[]
    for item in lst:
        if item[index]==value:
            ret.append(item.strip('\n'))

    return ret
def partTwo():
    with open('day3_input.txt') as file:
        file=file.readlines()
        print("ori",len(file))
        miniFile=file
        maxiFile=file
        for index in range(len(file)-1):
            m=get_max(maxiFile,index,"02")

            if m=="0":
                miniFile=filter(miniFile,index,"1")
                print(">>>>>",miniFile)
            else:
                miniFile = filter(miniFile, index, "0")

            maxiFile=filter(maxiFile,index,m)
            if len(miniFile)==1:
                print("lasting",miniFile)
                break
            if len(maxiFile)==1:
                print("last",maxiFile)
                break


def partTwomin():
    with open('day3_input.txt') as file:
        file = file.readlines()
        print("ori", len(file))
        miniFile = file
        for index in range(len(file) - 1):
            m = get_min(miniFile, index)
            miniFile = filter(miniFile, index, m)


            if len(miniFile) == 1:
                print("lasting", miniFile)
                break






if __name__ == '__main__':
    # partOne()
    # partTwo()
    partTwomin()
    a = int("100100010010", 2)
    b = int("011101110101", 2)
    print(a * b)

    """
    100010001010
    
    011101110101
    4568237
    """