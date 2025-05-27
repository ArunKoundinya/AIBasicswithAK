def show_menu(pizza_menu):
  counter=1
  print("\n --------- PIZZA ORDERING SYSTEM --------- \n")
  for pizza, price in pizza_menu.items():
    print(f"{counter} - {pizza} : ${price}")
    counter = counter + 1


def take_order():
  selected_pizza = input("What pizza would you like to order; Enter ther serial number? ")
  return selected_pizza


def pizza_ordering_system():
   pizza_menu = {
    "margherita" : 8.99,
    "pepperoni" : 10.99,
    "vegetarian" : 12.99,
    "hawaiian" : 11.00,
    "bbq_chicken": 11.54,
    "panner_tikka" : 13.99
    }
   
   show_menu(pizza_menu)
   
   customer_pizza = take_order()
   
   print("\n----- Your Final Bill Amount in $ ----\n")

   print(list(pizza_menu.values())[int(customer_pizza)-1])

if __name__ == "__main__":
  pizza_ordering_system()