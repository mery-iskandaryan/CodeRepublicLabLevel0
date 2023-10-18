def sqrt_newton(x, max_iterations=100):
    guess = 0.1
    for _ in range(max_iterations):
        next_guess = 0.5 * (guess + x / guess)
        if abs(next_guess - guess) < 0.000001:
            return next_guess

        guess = next_guess

    raise Exception("Square root calculation did not converge")

x = 2
result = sqrt_newton(x)
print(f"The square root of {x} is approximately {result}")


