def numeric_integral(f, start: int, end: int, steps: int):
    area = 0
    step_size = (end - start) / steps
    x = start

    for _ in range(steps):
        area += step_size * (f(x) + f(x + step_size)) / 2
        x += step_size

    return area


def f(x):
    return 4+x**2


print(numeric_integral(f, 0, 1, 3))
