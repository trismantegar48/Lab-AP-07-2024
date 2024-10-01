import random

def deal_card():
    """Mengambil kartu acak dari dek kartu."""
    cards = [1,11] #[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(hand):
    """Menghitung total nilai dari tangan pemain atau dealer."""
    return sum(hand)

def blackjack():
    player_hand = [deal_card()]
    dealer_hand = [deal_card()]

    print("Welcome to Blackjack!")

    while True:
        print(f"Kartu anda sekarang adalah: {calculate_score(player_hand)}")
        print("Apakah masih akan mengambil kartu? (y/n)")
        response = input().lower()

        if response == "y":
            player_hand.append(deal_card())
            if calculate_score(player_hand) > 21:
                print(f"Anda kalah! Total skor kartu anda adalah {calculate_score(player_hand)}")
                return
        elif response == "n":
            break

    print(f"Kartu dealer adalah: {calculate_score(dealer_hand)}")

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        print(f"Kartu dealer sekarang adalah: {calculate_score(dealer_hand)}")

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21:
        print("Anda menang, dealer melebihi 21.")
    elif player_score > 21:
        print("Anda kalah, kartu anda melebihi 21.")
    elif player_score > dealer_score:
        print("Anda menang!")
    elif player_score < dealer_score:
        print("Dealer menang!")
    else:
        print("Seri!")

blackjack()