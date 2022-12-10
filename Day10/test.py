#!/usr/bin/env python

import sys


def main() -> None:
    data = open("input.txt", mode="r").read().splitlines()

    circle_values = []
    current_value = 1

    for row in data:
        if len(row.split()) != 2:
            circle_values.append(current_value)
        else:
            _, value = row.split(" ")

            circle_values.append(current_value)
            circle_values.append(current_value)
            current_value = current_value + int(value)

    print(
        "first part solution",
        circle_values[20 - 1] * 20
        + circle_values[60 - 1] * 60
        + circle_values[100 - 1] * 100
        + circle_values[140 - 1] * 140
        + circle_values[180 - 1] * 180
        + circle_values[220 - 1] * 220,
    )

    for i in range(0, 6):
        for j in range(0, 40):

            if j in [
                circle_values[i * 40 + j],
                circle_values[i * 40 + j] + 1,
                circle_values[i * 40 + j] - 1,
            ]:
                print("#", end="")
            else:
                print(".", end="")
        print("")


if __name__ == "__main__":
    sys.exit(main())