"""Calculate cost of floor."""


def main():
    """Calculate it."""
    cost = float(input(u"Cost per unit²: "))
    width = float(input("meters of the width: "))
    height = float(input("meters of the height: "))
    print(u"The cost is: \u20B9"+f"{float(cost*width*height)}")


if __name__ == "__main__":
    main()
