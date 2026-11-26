#Price per pound calculator 
#The goal of this script is to either find the price per pound of one item, or compare the price per pound for 2 items and then print which item is the better buy

def get_weight_in_lbs(prompt):
    #this section asks for weight. for weight, user should input x lbs or x oz. and program will understand which is which and convert to lbs for final calculation
    while True:
        user_input = input(prompt).strip().lower()  # e.g. "5 lbs" or "8 oz"
        parts = user_input.split()

        if len(parts) != 2:
            print("Please enter in the format: <number> <lbs/oz>, e.g. '5 lbs'")
            continue

        amount_str, unit = parts

        try:
            amount = float(amount_str)
        except ValueError:
            print("That doesn't look like a valid number.")
            continue

        #def lbs
        if unit in ("lb", "lbs", "pound", "pounds"):
            return amount
        #def oz
        #if oz, convert to lbs (16 oz = 1 lbs)
        elif unit in ("oz", "ounce", "ounces"):
            return amount / 16
        else:
            print("Unit not recognized. Please use lbs or oz.")


def get_price(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            price = float(user_input.replace("$", ""))
            return price
        except ValueError:
            print("Please enter a valid number, e.g. 3.99")


def price_per_pound(price, weight_lbs):
    return price / weight_lbs


def main():
    #note that final prices per pound will be in lbs
    #How many Items are we looking at? (enter 1 or 2)
    while True:
        choice = input("How many items are we looking at? (enter 1 or 2): ").strip()
        if choice in ("1", "2"):
            break
        print("Please enter 1 or 2.")

    #if user inputs 1, then find the price per item for one.
    if choice == "1":
        #print "what is the weight of item a"
        #user input x lbs or x oz
        weight_a = get_weight_in_lbs("What is the weight of item A? (e.g. 5 lbs or 8 oz): ")
        #print "what is the price of item a"
        price_a = get_price("What is the price of item A? (e.g. 3.99): ")

        ppp_a = price_per_pound(price_a, weight_a)
        print(f"\nItem A: ${ppp_a:.2f} per pound")

    #elif user inputs 2, then compare the prices of both items
    elif choice == "2":
        #print "what is the weight of item a"
        weight_a = get_weight_in_lbs("What is the weight of item A? (e.g. 5 lbs or 8 oz): ")
        #print "what is the price of item a"
        price_a = get_price("What is the price of item A? (e.g. 3.99): ")

        #print "what is the weight of item b"
        weight_b = get_weight_in_lbs("What is the weight of item B? (e.g. 5 lbs or 8 oz): ")
        #print "what is the price of item b"
        price_b = get_price("What is the price of item B? (e.g. 3.99): ")

        ppp_a = price_per_pound(price_a, weight_a)
        ppp_b = price_per_pound(price_b, weight_b)

        print(f"\nItem A: ${ppp_a:.2f} per pound")
        print(f"Item B: ${ppp_b:.2f} per pound")

        #If option 2 selected,
        #If price per pound is higher for item b, than say "item a is the better buy" and vice-versa
        if ppp_a < ppp_b:
            print("Item A is the better buy.")
        elif ppp_b < ppp_a:
            print("Item B is the better buy.")
        else:
            print("Both items have the same price per pound.")

        #Calculate how many months of buying the pricier item it takes for the
        #cumulative extra cost to reach a target dollar amount
        premium_per_lb = abs(ppp_a - ppp_b)
        pricier_weight = weight_b if ppp_b > ppp_a else weight_a
        extra_per_month = premium_per_lb * pricier_weight

        if extra_per_month > 0:
            target = float(input("\nEnter a target dollar amount to compare against: "))
            months = target / extra_per_month
            print(f"Extra cost per month from buying the pricier item: ${extra_per_month:.2f}")
            print(f"Months until cumulative difference reaches ${target:.2f}: {months:.2f}")
        
if __name__ == "__main__":
    main()

