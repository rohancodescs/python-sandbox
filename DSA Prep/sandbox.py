import re
def reverse(x):
    if x < 0:
        isNeg = True
        x = x* -1
    else:
        isNeg = False

    y = []
    while x % 10 != x:
        y.append(x % 10)
        x = x // 10
    if x != 0:
        y.append(x % 10)
    
    temp = [str(i) for i in y]
    # temp = temp[::-1]
    if isNeg:
        a = -int("".join(temp))
    else:
        a = int("".join(temp))
    if a > -2**31:
        if a < (2 ** 31) - 1:
            return a
    return 0
def main():
    print(reverse(-2**32))
    # text = "cool: false, cringe: true, based: false, corny: true"
    # pattern = r'(\w+): (\w+)'

    # matches = re.findall(pattern, text)

    # print("Cliff characteristics:\n")
    # for match in matches:
    #     name, age = match
    #     print("trait:", name)
    #     print("truth value:", age)
    #     print()


if __name__ == "__main__":
    main()