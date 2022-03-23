#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, with proper style

import constants


def main():
    # This function calculates the cost of a pizza

    # input
    diameter = int(input("Enter the diameter of the pizza you would like (inch): "))

    # process
    untaxed_price = (
        constants.LABOR + constants.RENT + constants.MATERIAL_PER_INCH * diameter
    )
    HST = untaxed_price * 0.13
    total_cost = untaxed_price + HST

    # output
    print("")
    print("The cost of a {0} inch pizza is ${1:,.2f}.".format(diameter, total_cost))

    print("\nDone.")


if __name__ == "__main__":
    main()
