import sympy as sym
from sympy import sin, cos, tan, log, exp, pi

x = sym.symbols('x')
y = sym.symbols('y')

#定積分計算
hoge = cos(sin(x))
eq = sym.Eq(sym.Integral(hoge, (x, 0, pi/2)))
print(eq)
#>>>False つまり１

X = lambda x: cos(sin(x))

from scipy import integrate
print(integrate.quad(X, 0, pi/2))
#(1.2019697153172066, 1.3344544528473075e-14)
#1.2019697153172066 が答え
