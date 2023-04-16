from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def start ():
    another_bidder = True
    bidders ={}
    bids = []
    bidder_name = ""
    bidder_bid = 0
    max_bid = 0

    

    while another_bidder == True:
        clear()
        print(logo)
        print("\nWelcome, Anonymous bidder, to the silent auction. Shhhhhh!\n")
        bidder_name = input("What is your name?\n --: ").lower()
        bidder_bid = int(input("\nWhat is your bid?\n --: $"))

        bidders[bidder_name] = bidder_bid

        answer = input("\n Is there another one interested? type 'yes' or 'no'\n --: ").lower()

        if answer == 'yes':
            another_bidder = True
        else: 
            another_bidder = False

    for bidder in bidders:
        bids.append(bidders[bidder])

    key_list = list(dict.keys(bidders))
    val_list = list(dict.values(bidders))

    max_bid = max(bids)

    index = val_list.index(max_bid)
    name_of_winner = key_list[index]

    print(f"\nThe winner is {name_of_winner} with a bid of ${max_bid}!\n\n")


start()


