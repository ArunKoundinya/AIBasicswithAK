import streamlit as st

def show_menu(pizza_menu):
    st.subheader("🍕 Pizza Menu")
    for idx, (pizza, price) in enumerate(pizza_menu.items(), start=1):
        st.write(f"{idx}. **{pizza}** - ${price:.2f}")


def take_order(pizzamenu):
  pizza_list = list(pizzamenu.keys())
  selected_pizza = st.selectbox("Select your pizza",pizza_list)
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
   
   st.title(" Pizza Ordering System")
   show_menu(pizza_menu)
   
   st.markdown("--")
   customer_pizza = take_order(pizza_menu)

   if st.button("Place Order"):
     price = pizza_menu[customer_pizza]
     st.success(f"Order placed for **{customer_pizza}** pizza.")
     st.markdown("### Final Bill")
     st.write(f"**Total Amount:** ${price}")

if __name__ == "__main__":
  pizza_ordering_system()