#!/usr/bin/python

def calculate_loan_payment(loan, interest_rate, total_payments):
    rate = interest_rate / 100
    return round(rate * loan / (1 - (1 + rate)**(-total_payments)), 2)

def calculate_amortized_schedule(original_loan, interest_rate, payment_number, total_payments=360):
    """
    Calculates the amoritization schedule for the first [payment_number] payments (0-indexed).

    Determines the amount to pay on [payment_number] (0-indexed) payment for a fixed rate loan of [original_loan] at [interest_rate] (percentage, 4.75% rate is inputted as 4.75) with [total_payments].
    Interest rate should be the percentage per period.
    """

    if total_payments <= 0:
        raise Exception("Must have positive total_payments")

    payment_amount = calculate_loan_payment(original_loan, interest_rate, total_payments)

    n = 0
    rate_decimal = interest_rate / 100
    balance = original_loan

    schedule = []
    while True:
        # There is rounding error but it shouldn't be a substantial amount of money.
        interest = round(balance * rate_decimal, 2)
        principal = round(payment_amount - interest, 2)

        schedule.append((payment_amount, interest, principal))
        balance -= principal

        if n >= payment_number:
            break
        n += 1
    return schedule

def calculate_overview(loan, interest_rate, total_payments=360):
    payment = calculate_loan_payment(loan, interest_rate, total_payments)
    schedule = calculate_amortized_schedule(loan, interest_rate, total_payments, total_payments)

    total_interest = round(sum([line[1] for line in schedule]), 2)

    return {
        "payment": payment,
        "total_interest": total_interest,
        "interest_percentage": round(total_interest / loan, 2)
    }

