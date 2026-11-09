# author: Danila "akshin_" Axyonov

from math import pi, sin, exp
from collections.abc import Callable
import numpy as np
from matplotlib import pyplot as plt

def e1(x: float) -> float:
    return 6 * (x - 1) * (x - 3) * (x - 9)
e1_str: str = '6 * (x - 1) * (x - 3) * (x - 9)'

def e2(x: float) -> float:
    return x / 6 + sin(3 * pi * x + 9)
e2_str: str = 'x / 6 + sin(3 * pi * x + 9)'

def e3(x: float) -> float:
    return 6 - exp(- ((x - 3) / 9) ** 2)
e3_str: str = '6 - exp(- ((x - 3) / 9) ^ 2)'

def build_plot(e: Callable[[float], float],
               x_min: float,
               y_min: float,
               title: str,
               fname: str,
               l: float = -10,
               r: float = 10,
               n: int = 1_000,
               color: str = 'blue') -> None:
    x = np.linspace(l, r, num=n)
    y = np.array(list(map(e, x)))
    plt.clf()
    plt.plot(x, y, color=color)
    plt.plot(x_min, y_min, marker='X', color='black', label=f'min: ({x_min:.3f}, {y_min:.3f})')
    plt.grid(True)
    plt.title(title)
    plt.legend()
    plt.savefig(fname, dpi=300, bbox_inches='tight')

def main() -> None:
    x1_min: float = 6.73
    x2_min: float = 0.210
    x3_min: float = 3

    y1_min: float = e1(x1_min)
    y2_min: float = e2(x2_min)
    y3_min: float = e3(x3_min)

    build_plot(e1, x1_min, y1_min, f'E1(x) = {e1_str}', './plots/e1.png', r=15, color='green')
    build_plot(e2, x2_min, y2_min, f'E2(x) = {e2_str}', './plots/e2.png', l=-2.5, r=2.5, color='orange')
    build_plot(e3, x3_min, y3_min, f'E3(x) = {e3_str}', './plots/e3.png', l=3 - 20, r=3 + 20, color='red')
    plt.close()

if __name__ == '__main__':
    main()
