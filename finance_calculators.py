import math

# Capstone project - Variables and Control Structures

"""
The below is an example of a program that I have created for my first 
Capstone project.

The program allows the user to access two different financial calculators:
An investment calculator and a home loan repayment calculator.

It takes into account the type of interest e.g simple or compound that the user
will be paying. Or the interest earned on an investment.

"""

# Simple interest calculated once per year, then added to principal amount

# Compound interest - calculated on the current total known as the accumulated amount

print(
    "\n"
    "Please choose from the following two options: \n"
    "1. investment - to calculate the amount of interest you'll earn "
    "on your investment\n"
    "2. bond - to calculate the amount you'll have to pay on your home loan\n"
    "\n"
)

user_choice = input(
    "Enter either 'investment' or 'bond' from the above menu: "
)

# adding lower case to allow for valid entries that may be capitalised
if user_choice.lower() == "investment":
    P = int(
        input(
            "\nPlease enter the amount of money you are depositing in GBP,"
            " e.g 1000: "
        )
    )
    # interest rate entered by the user
    r_100 = int(
        input("Please enter the interest rate (number only no '%') e.g. 8: ")
    )
    # interest rate divided by 100 to account for percentage
    r = float((r_100 / 100))

    t = int(
        input("Enter the number of years you plan on investing, e.g. 20: ")
    )

    user_interest = input(
        "Please select whether you would like; "
        "'simple' or 'compound' interest: "
    )
    # For the simple and compound formulas below:
    #'r' is the interest rate entered by user divided by 100
    #'P' is the amount the user deposits
    #'t' is the number of years the money is being invested for

    simple_interest = P * (1 + r * t)

    # added formatting for output to be 2 decimal and written as currency convention
    if user_interest.lower() == "simple":
        print(
            f"The amount of interest you will earn is £{simple_interest:,.2f}."
        )
    elif user_interest.lower() == "compound":
        compound_interest = P * math.pow((1 + r), t)
        print(
            "The amount of interest you will earn is "
            f"£{compound_interest:,.2f}."
        )

    # adding error message to account for user typing in an invalid entry
    else:
        print(
            f"You entered '{user_choice}', this is an invalid choice.\n"
            "Please enter 'simple' or 'compound' next time.\n"
            "The programme will now exit."
        )

elif user_choice.lower() == "bond":
    P = int(input("Please enter present value of your house e.g. 100000: "))
    user_i = int(input("Please enter the interest rate e.g. 7: "))

    # monthly interest rate so need to divide by 100 and then by 12
    i = float((user_i / 100) / 12)

    n = int(
        input(
            "Please enter the number of months you plan to take"
            " to repay the bond: "
        )
    )

    # For the repayment formula below:
    #'P' is the amount the present value of the house
    #'i' is the monthly interest rate
    #'n' is the number of months over which the bond will be repaid

    repayment = (i * P) / (1 - (1 + i) ** (-n))
    repayment = round(repayment, 2)

    print(
        f"The amount of money you will repay each month is £{repayment:,.2f}."
    )
else:
    print(
        f"You entered '{user_choice}', this is an invalid choice.\n"
        "Please enter 'investment' or 'bond' next time.\n"
        "The programme will now exit."
    )
