# okres, srednia, wariancja
a = 17
c = 17
M = 43991


def main():
    a = int(input("Podaj a:"))
    c = int(input("Podaj c:"))
    M = int(input("Podaj M:"))
    number_list = [c]
    while True:
        next = calculate_next(a, number_list[-1], c, M)
        if not_looped_already(number_list, next):
            number_list.append(next)
        else:
            break
    print("Okres: {}".format(len(number_list)))
    mean = sum(number_list) / len(number_list)
    print("Średnia: {}".format(mean))
    variance = 0
    nominator = 0
    for i in number_list:
        nominator = nominator + (i-mean)**2
    denominator = len(number_list)
    variance = (nominator/denominator)**0.5
    print("Wariancja: {}".format(variance))


def calculate_next(last, a=a, c=c, M=M):
    next = (a * last + c) % M
    return next


def not_looped_already(number_list, next):
    for i in number_list:
        if i == next:
            return False
    else:
        return True


if __name__ == '__main__':
    main()
