a = 2
b = 4
c = 8

print('\nDefault Order:\t', a, '*', c, '+', b, '=', a * c + b)
print('\nForced Order:\t', a, '* (', c, '+', b, ') =', a * (c + b))
print('\nDefault Order:\t', c, '//', b, '-', a, '=', c // b - a)
print('\nForced Order:\t', c, '// (', b, '-', a, ') =', c // (b - a))
print('\nDefault Order:\t', c, '%', a, '+', b, '=', c % a + b)
print('\nForced Order:\t', c, '% (', a, '+', b, ') =', c % (a + b))
print('\nDefault Order:\t', c, '**', a, '+', b, '=', c ** a + b)
print('\nForced Order:\t', c, '** (', a, '+', b, ') =', c ** (a + b))