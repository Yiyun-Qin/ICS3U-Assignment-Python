#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, with proper style

import math
from fractions import Fraction


def main():
    # This function calculates the surface area and volume of a cone

    # input
    radius = int(input("Enter the radius of the cone you want to calculate: ")
    height = int(input("Enter the height of the cone you want to calculate: ")

    # process
    surface_area = math.pi * radius * (radius + pow((pow(height, 2) + pow(radius, 2), Fraction(1, 2))))
    volumn = math.pi * pow(radius, 2) * height * Fraction(1, 3)

    # output
    print("")
    print("The surface area of the cone is {} cm.".format(surface_area))

    print("\nDone.")


if __name__ == "__main__":
    main()
