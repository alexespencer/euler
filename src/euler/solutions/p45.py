from euler import hexagon_n, pentagon_n, triangle_n


class ShapeTracker:
    n3: int
    n5: int
    n6: int

    def __init__(self):
        self.n3 = 285
        self.n5 = 0
        self.n6 = 0
        self.update_shape_numbers()
        assert self.n5 == 165
        assert self.n6 == 143

    def current_triangle(self) -> int:
        return triangle_n(self.n3)

    def update_shape_numbers(self):
        # Ensure that pentagon/hexagon numbers are >= the triangle number
        current_triangle = self.current_triangle()
        while pentagon_n(self.n5) < current_triangle:
            self.n5 += 1
        while hexagon_n(self.n6) < current_triangle:
            self.n6 += 1

    def solution(self) -> int:
        """Returns the next triangle number that is also pentagonal and hexagonal"""
        while True:
            self.n3 += 1
            self.update_shape_numbers()
            current_triangle = self.current_triangle()
            if (
                pentagon_n(self.n5) == current_triangle
                and hexagon_n(self.n6) == current_triangle
            ):
                return current_triangle


def solution() -> int:
    tracker = ShapeTracker()
    return tracker.solution()


if __name__ == "__main__":
    print(solution())
