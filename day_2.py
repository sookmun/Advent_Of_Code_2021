class SubmarinePartOne():
    def __init__(self):
        self.horizontal=0
        self.depth=0

    def forward(self,num):
        self.horizontal+=num
    def down(self,num):
        self.depth+=num
    def up(self,num):
        self.depth -= num
    def ret(self):
        return (self.horizontal,self.depth)

class SubmarinePartTwo():
    def __init__(self):
        self.horizontal=0
        self.depth=0
        self.aim=0

    def forward(self,num):
        self.horizontal+=num
        self.depth+= self.aim*num
    def down(self,num):

        self.aim+=num
    def up(self,num):

        self.aim-=num
    def showme(self):
        print(self.horizontal)
        print(self.depth)
        print(self.aim)
    def ret(self):
        return self.horizontal*self.depth

def partOne():
    sub = SubmarinePartOne()
    with open('day2_input.txt') as f:
        file = f.readlines()
        count = 0
        for line in file:
            line = line.strip('\n')
            line = line.split(" ")
            if line[0] == 'forward':
                sub.forward(int(line[1]))
            elif line[0] == 'down':
                sub.down(int(line[1]))
            else:
                sub.up(int(line[1]))
    print(sub.ret())
    l = sub.ret()
    print(l[0] * l[1])


def partTwo():
    sub = SubmarinePartTwo()
    with open('day2_input.txt') as f:
        file = f.readlines()
        for line in file:
            line = line.strip('\n')
            line = line.split(" ")
            if line[0] == 'forward':
                sub.forward(int(line[1]))
            elif line[0] == 'down':
                sub.down(int(line[1]))
            else:
                sub.up(int(line[1]))
        print(sub.ret())



if __name__ == '__main__':
    # partOne()
    partTwo()
