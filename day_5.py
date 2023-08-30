def hydrothermal():
    map={}
    with open('day5_example.txt') as file:
        file=file.readlines()
        for line in file:

            line=line.strip('\n')
            line=line.split(" -> ")
            # line=line.replace(" -> ",",")

            print(line)
        print("")
    # for index in range(0,len(line),2):
    #     print("first:",line[index])
    #     print("second",line[index+1])
    #     print("dddddd")

def check():
    matrix=[]
    for i in range(10):
        matrix.append([0,0,0,0,0,0,0,0,0,0])
    matrix[9][0]=9
    matrix[1][2]=1
    matrix[2][2]=1
    for l in matrix:
        print(l)


if __name__ == '__main__':
    hydrothermal()
    check()
