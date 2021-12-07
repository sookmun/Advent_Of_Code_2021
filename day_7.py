def getFuel(position,end):
    return abs(position-end)

def getFuelTwo(position,end):
    start=min(position,end)
    end=max(position,end)
    distance=end-start
    #using Gauss formula
    #(n / 2)(first number + last number) = sum, where n is the number of integers.
    fuel=(distance/2)*(1+distance)
    return int(fuel)

def partOne():
    with open('day7_input.txt') as file:
        file=file.readlines()
        lines=file[0].split(",")
        lines = list(map(int, lines))
        print(lines)
        minimumFuel= 0
        for pos in range(max(lines)):
            totalFuel=0
            for crab in lines:
                fuel=getFuel(crab,pos)
                totalFuel+=fuel
                if type(minimumFuel)==tuple and totalFuel>minimumFuel[0]:
                    break
            if pos==0:
                minimumFuel=(totalFuel,0)
            elif totalFuel<minimumFuel[0]:

                minimumFuel=(totalFuel,pos)
        print(minimumFuel)

def partTwo():
    with open('day7_input.txt') as file:
        file = file.readlines()
        lines = file[0].split(",")
        lines = list(map(int, lines))
        print(lines)
        minimumFuel = 0
        for pos in range(max(lines)):
            totalFuel = 0
            for crab in lines:
                fuel = getFuelTwo(crab, pos)
                totalFuel += fuel
                if type(minimumFuel)==tuple and totalFuel>minimumFuel[0]:
                    break

            if pos == 0:
                minimumFuel = (totalFuel, 0)
            elif totalFuel < minimumFuel[0]:
                minimumFuel = (totalFuel, pos)
        print(minimumFuel)


if __name__ == '__main__':
    partOne()
    # partTwo()
    # print(getFuelTwo(16,5))
    # l=16-5
    # print((l/2)*(1+l))