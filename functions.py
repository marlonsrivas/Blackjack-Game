import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def UserDealing():
    user_cardss = []  # Initialize the list for the user
    ucard = 0
    while ucard < 2:
        user_cardss.append(random.choice(cards))
        ucard = ucard + 1
        # print("user:", user_cardss)
    user_sum = sum(user_cardss)
    # print(f"Your Cards are {user_cardss[0]} and {user_cardss[1]} Current Score: {user_sum}")
    return user_cardss
def Dealer_Dealing():
    dealer_cardss = []  # initialize the list for the dealer
    # start of game - Both user and dealer start with 0 cards
    dcard = 0
    # Dealer and User both get two cards - 1 is shown and the other one is hidden.
    while dcard < 2:
        dealer_cardss.append(random.choice(cards))
        dcard = dcard + 1
    dealer_sum = sum(dealer_cardss)
    return dealer_cardss

    # print("dealer:",dealer_cardss)
def CheckForAce(mylist):
    if (max(mylist) == 11):
        return 1
    else:
        return 0
def ReplaceAce(mylist):
    n = len(mylist)
    if ((max(mylist) == 11) and sum(mylist) > 21):
        for i in range(n):
            if mylist[i] == 11:
                mylist[i] = 1
                return mylist
def BlackJack():
    UserLose = 0
    DealerLose = 0
    UserAce = 0
    DealerAce = 0
    utotal = 0
    dtotal = 0
    cont = True

    # User Initial Cards
    user_cardss = UserDealing()
    user_sum = sum(user_cardss)
    ucard = len(user_cardss)

    # Dealer Initial Cards
    dealer_cardss = Dealer_Dealing()
    dealer_sum = sum(dealer_cardss)
    dcard = len(dealer_cardss)

    print(f"Your Cards are {user_cardss[0]} and {user_cardss[1]} Current Score: {user_sum}")
    print(f"dealer's card is {dealer_cardss[0]}, the sum is {dealer_sum}")

    # User playing
    while cont:
        if user_sum > 21:
            UserAce = CheckForAce(user_cardss)
            if UserAce == 1:
                user_cardss = ReplaceAce(user_cardss)
                cont = True
               # print(f"User list is {user_cardss}")
            else:
                cont = False
                UserLose = 1
            break
        user_input = input(f"Your sum is {user_sum} do you want to grab another card or hold?\n").lower()
        if user_input == "grab":
            user_cardss.append(random.choice(cards))
            #print(user_cardss)
            user_sum = user_sum + user_cardss[ucard]
            ucard = ucard + 1
        elif user_input == "hold":
            print(f"Your Total Sum is {user_sum}")
            print(f"Dealer Sum is {dealer_sum}")
            cont = False
    # User stops grabbing cards

    # Case if dealer needs to draw a new card because draw is less than 16
    if dealer_sum <= 16:
        while dealer_sum <= 16:
            dealer_cardss.append(random.choice(cards))
            #print(dealer_cardss)
            dealer_sum = dealer_sum + dealer_cardss[dcard]
            dcard = dcard + 1
            print(f"the new dealer sum is {dealer_sum}")
            DealerAce = CheckForAce(dealer_cardss)
            if DealerAce == 1 and dealer_sum > 21:
                dealer_cardss = ReplaceAce(dealer_cardss)
        # Case in case dealer or user gets an Ace
        #print(f"The max card on dealers list is: {(max(dealer_cardss))}")
        #print(f"The max card on users list is: {(max(user_cardss))}")
    elif UserLose == 1:
        print(f"You lost your sum {user_sum}, is greater than 21.")
    # Case if User or Dealer get a 10 and 11 1st hand
    elif dealer_sum == 21 or user_sum == 21 and DealerLose == 0 or UserLose == 0:
        if dealer_sum == 21 and user_sum == 21:
            print("Draw")
        elif (dealer_sum == 21):
            print("Dealer Wins!")
            UserLose = 1
        else:
            print("User Wins")
            DealerLose = 1
    elif (user_sum < 21 and dealer_sum < 21):
        dtotal = 21 - dealer_sum
        utotal = 21 - user_sum
        if (dtotal < utotal):
            print(f"Dealer Wins!")
            DealerLose = 1

        else:
            print(f"User Wins!")
            DealerLose = 1
    elif (user_sum == dealer_sum):
        print(f"It is a Draw!")
    else:
        print(f"User Wins!")
        DealerLose = 1

