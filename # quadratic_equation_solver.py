# quadratic_equation_solver.py

import math

def quadratic_equation_solver(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        x = (-b) / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

# Example usage
print(quadratic_equation_solver(1, -5, 6)) # Output: (3.0, 2.0)
