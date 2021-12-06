def lanternFish():
    with open('day6_input.txt') as file:
        file=file.readlines()
        line=file[0]
        line = line.split(",")
        lst = list(map(int, line))
        days=80
        count=0
        for day in range(days):
            for index in range(len(lst)):
                if lst[index] == 0:
                    lst.append(8)
                    count+=1
                    lst[index]=6
                else:
                    lst[index]-=1
            # print(lst)
        return count

def lanternFishPartTwo():
    with open('day6_input.txt') as file:
        file = file.readlines()
        line = file[0]
        line = line.split(",")
        lst = list(map(int, line))
        days =256
        masterlst=[0]*9
        for fish in lst:
            masterlst[fish]+=1
        print(masterlst)
        temp=0
        for day in range(days):
            # print(">"*20)
            for index in range(8,-1,-1):
                if index == 0:
                    masterlst[8] += masterlst[index]
                    masterlst[6] += masterlst[index]
                    masterlst[index]=0
                temp,masterlst[index]=masterlst[index],temp
        print(masterlst)
        return sum(masterlst)



if __name__ == '__main__':
    # number=lanternFish()
    # print(number)
    number=lanternFishPartTwo()
    print(number)
    # a=1
    # b=2
    # a,b=b,a
    # print("a:",a)
    # print("b:",b)