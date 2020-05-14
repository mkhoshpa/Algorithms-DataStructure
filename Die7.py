'''You have a function rand5() that generates a random integer from 1 to 5.
 Use it to write a function rand7() that generates a random integer from 1 to 7.'''
from random import randrange


def die5():
    return 1+randrange(5)


def die7():
    out=0
    for i in range(7):
        out += die5()
    return out % 7


def main():
    output_dict = {}
    for i in range(70000):
        roll = die7()
        if roll in output_dict:
            output_dict[roll]+=1
        else:
            output_dict[roll] = 1
    print(output_dict)

if __name__ == '__main__':
    main()
