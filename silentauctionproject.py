import os
def find_winner(bidder_details):
    highest_bid=0
    for keys in dict:
        bidding_price=bidder_details[keys]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=keys
    print(f"The winner is {winner} with a bit price of {highest_bid}")
dict={ }
auction_end=False
while not auction_end:
    names=input("what is your name?:")
    price=int(input("what is your bid?:"))
    dict[names]=price
    any_bidders=input("Are there any other bidders?(Yes/No):\n").lower()
    if any_bidders=="no":
        auction_end=True
        find_winner(dict)
    elif any_bidders=="yes":
        os.system("cls")
