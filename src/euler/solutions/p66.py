# Diophantine equations
# Generate the D possibilities from 2 to 1000 if it is NOT square

from euler import continued_expansion, is_square

# The equation in question is a special form of Diophantine equation, called a Pell equation.
# The equation is of the form:
#     x^2 - Dy^2 = 1
# ...and this special form can be solved by finding the continued fraction of the square root of D
# See https://mathworld.wolfram.com/PellEquation.html


def solve_pell_equation(D):
    alphas = continued_expansion(D)

    # We can repeat the alphas from [1:] - but need remember how many we added. This allows us to access 2r + 1
    alphas_extended = alphas[1:]
    alphas.extend(alphas_extended)

    a0 = alphas[0]
    p = [a0, a0 * alphas[1] + 1]
    q = [1, alphas[1]]
    for i in range(2, len(alphas)):
        p.append(alphas[i] * p[-1] + p[-2])
        q.append(alphas[i] * q[-1] + q[-2])

    r = len(alphas) - len(alphas_extended) - 2
    assert alphas[r + 1] == 2 * alphas[0]

    if r % 2 == 1:
        x = p[r]
        y = q[r]
    else:
        x = p[2 * r + 1]
        y = q[2 * r + 1]

    return x, y


def solution() -> int:
    D_max = 1000
    D_poss = [n for n in range(2, D_max + 1) if not is_square(n)]

    # Find the D with the largest X
    all_x = {}
    for D in D_poss:
        x, _ = solve_pell_equation(D)
        all_x[D] = x
    print(all_x)

    return max(all_x, key=lambda k: all_x[k])


if __name__ == "__main__":
    print(solution())
