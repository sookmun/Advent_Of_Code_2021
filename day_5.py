def hydrothermal():
    with open('day5_example.txt') as file:
        file=file.readlines()
        for line in file:

            line=line.strip('\n')
            line=line.replace(" -> ",",")
            line=line.split(",")
            print(line)


if __name__ == '__main__':
    hydrothermal()