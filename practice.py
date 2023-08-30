def numcomplement(num):
    num=format(num,"b")
    print(num)
    complement=""
    com=str(num)
    for alpha in com:
        if alpha=="0":
            complement+="1"
        else:
            complement+="0"
    print(complement)
    print(int(complement,2))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2):


def addnum(l1,l2):
    print(l1)
    add=1
    sum1=0
    sum2=0
    for elem in l1:
        sum1+=elem*add
        add=add*10
    add=1
    for elem in l2:
        sum2+=elem*add
        add=add*10
    print(sum1)
    print(sum2)
    print(sum1+sum2)

def longestpaln(word):
    start=0
    end=0
    palindrome=""
    check=""
    for i in range(len(word)):
        check+=word[i]
        if isPalin(check):
            if len(check)>len(palindrome):
                palindrome=check

def isPalin(word):
    end=-1
    for i in range(len(word)):
        print(word[i], word[end])
        if i>=len(word)//2:
            return True
        if word[i]!=word[end]:
            print(word[i],word[end])
            return False
        end-=-1





if __name__ == '__main__':
    # numcomplement(5)
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    # addnum(l1,l2)
    longestpaln("babad")
