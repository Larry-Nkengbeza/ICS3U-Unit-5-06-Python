# usr/env/bin Python
# This program was created by Larry Nkengbeza
# THis program was created on January 2021
# This prgram turns decimals to whole numbers.


def main():

    # input
    user_input = int(float(input("Enter a decimal number: ")))
    oth_user_in = int(input("Enter how many decimal places to round to: "))
    rounded = user_input + 0.5 * (oth_user_in)
    # process and output
    print("This number rounded up is: {0}".format(rounded))


if __name__ == "__main__":
    main()
