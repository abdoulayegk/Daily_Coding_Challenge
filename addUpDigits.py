"""Give a non-negative integer numb, repeteadly add all its digits until the
result has only one digit.for example :39=3+9=12 output:3"""


def addDigits(num):
    sum = 0
    while num > 0:
        r = num % 10
        sum = sum + r
        num = int(num / 10)
    result = sum
    if sum > 9:
        result = addDigits(sum)
    return result


if __name__ == "__main__":
    print("Sum of digits of the numbers is :", addDigits(159))
