from datetime import date, timedelta


def solution() -> int:
    start = date(1901, 1, 1)
    end = date(2000, 12, 31)
    i = start
    count = 0
    while True:
        if i.weekday() == 6 and i.day == 1:
            count += 1
        i += timedelta(days=1)
        if i == end:
            break
    return count


if __name__ == "__main__":
    print(solution())
