from euler.primes import is_prime


class NumberSpiral:
    value: int
    step: int

    diagonal_prime_count: int
    diagonal_count: int

    def __init__(self) -> None:
        self.value = 1
        self.step = 1

        self.diagonal_prime_count = 0
        self.diagonal_count = 1  # Start with the center 1

    def add_layer(self) -> None:
        self.step += 2

        # Take a step to the right
        self.value += 1

        # Walk up (1 less than step)
        self.value += self.step - 2
        if is_prime(self.value):
            self.diagonal_prime_count += 1

        # Walk left
        self.value += self.step - 1
        if is_prime(self.value):
            self.diagonal_prime_count += 1

        # Walk down
        self.value += self.step - 1
        if is_prime(self.value):
            self.diagonal_prime_count += 1

        # Walk right
        self.value += self.step - 1
        if is_prime(self.value):
            self.diagonal_prime_count += 1

        self.diagonal_count += 4

    def diagonal_prime_percentage(self) -> float:
        return self.diagonal_prime_count / self.diagonal_count


def solution() -> int:
    spiral = NumberSpiral()
    for _ in range(3):
        spiral.add_layer()

    # Add the other layers
    while spiral.diagonal_prime_percentage() >= 0.1:
        spiral.add_layer()

    return spiral.step


if __name__ == "__main__":
    print(solution())
