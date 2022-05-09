from math import sqrt, pi, exp
from random import random
from uniform_generator import calculate_next, M
import matplotlib.pyplot as plt
import typing

def prob_density_function_basic(x: float):
    return abs(1-x)


def prob_density_function_adv(x: float, delta=0.2, u=0):
    aux1 = -1 * ((x-u)**2)/(2*delta**2)
    aux2 = 1/(delta * sqrt(2*pi)) * exp(aux1)
    return aux2

def draw_plot(n: list):
    import matplotlib
    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=20)
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 22}
    #plt.yscale("log")
    matplotlib.rc('font', **font)
    plt.xlabel("Rozmiar danych N [-]")
    plt.ylabel("Czas wykonywania [s]")
    nums = list(range(len(n)))
    plt.plot(nums, n, 'ro')
    plt.legend()
    plt.show()

def main():
    a = -2
    b = 2
    number_list = []
    #a = int(input("podaj a: "))
    #b = int(input("podaj b: "))
    #d = int(input("podaj d: "))
    d = 1
    u1 = 1
    next_item = u1
    for i in range(1000):
        next_item = calculate_next(next_item)#*(b-a)+a
        u1 = (next_item/M)*(b-a)+a
        u2 = random()*d
        if u2 <= prob_density_function_adv(u1):
            number_list.append(u1)

    for i in number_list:
        print(i)
    draw_plot(number_list)

if __name__ == '__main__':
    main()

