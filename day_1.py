def partOne():
    with open('day1_input.txt') as f:
        lines = f.readlines()
        counter=0
        prev=0
        for line in lines:
            depth=int(line)
            if prev==0:
                prev=depth
            else:
                if depth>prev:
                    counter+=1
            prev=depth
        print(counter)
    f.close()
def partTwo():
    with open('day1_input.txt') as f:
        lines = f.readlines()
        print(lines)
        counter = 0
        prev = 0
        for index in range(len(lines)-2):
            if prev == 0:
                summation=0
                for i in range(3):
                    depth = lines[index+i].strip('\n')
                    depth = int(depth)
                    print(summation,"summmmaaa")
                    summation+=depth
                prev = summation

            else:
                summation = 0
                for i in range(3):
                    depth = lines[index+i].strip('\n')
                    depth = int(depth)
                    summation += depth
                    print(summation,"secondd")
                if summation > prev:
                    counter += 1
                prev = summation

        print(counter)

    f.close()
partTwo()


