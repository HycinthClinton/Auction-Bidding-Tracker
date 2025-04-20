# Initialize variables to track the highest bidder
highest_bidder_name = ""
highest_bidder_amount = 0

while True:
    try:
        # Get bid details from the user
        bidder_name = input("What is your name?: ")
        bid_amount = int(input("What is your bid?: $"))
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

        # Check if the current bid is the highest
        if bid_amount > highest_bidder_amount:
            highest_bidder_amount = bid_amount
            highest_bidder_name = bidder_name

        # If no more bidders, print the result and exit
        if more_bidders == "no":
            print(f"The highest bidder is {highest_bidder_name} with a bid of ${highest_bidder_amount}.")
            break

    except ValueError:
        print("Invalid bid amount. Please enter a valid number.")


