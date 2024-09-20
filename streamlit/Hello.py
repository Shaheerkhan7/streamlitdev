import streamlit as st
import random


def get_response(user_input):
    responses = {
        "hello": "Hello! Please select an item below and if there are issues a live agent will reach out to you! Have a daigy experience. ",
        "how are you": "I'm an AI, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Feel free to come back anytime."
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

with st.sidebar:
    # Create a container for the messages
    messages = st.container()

    # Get user input from the chat input field
    if prompt := st.chat_input("Any Query? (type: hello)"):
        # Display user input
        with messages:
            messages.chat_message("user").write(prompt)
            
            # Generate and display assistant response
            response = get_response(prompt)
            messages.chat_message("assistant").write(response)

    # List of selectable items for the user
    items = ["Biryani", "Pulao", "Kebab", "Salad", "Dessert"]
    selected_item = st.selectbox("Select an item to order:", items)

    if st.button("Order"):
        messages.chat_message("user").write(f"Ordered: {selected_item}")
        messages.chat_message("assistant").write(f"Thank you for your order of {selected_item}! We are getting back to you.")



st.write("# Welcome to Daig.com! 🍛")

# Add some styling or custom messages on the sidebar
st.sidebar.success("Discover the best Pulao & Biryani recipes!")

# Random welcome messages or taglines for Daig.com
welcome_messages = [
    "Welcome to Daig.com – Your ultimate destination for the most flavorful Pulao and Biryani recipes!",
    "Satisfy your cravings with authentic Chawal dishes, only at Daig.com.",
    "Discover the rich flavors of traditional Pulao and Biryani – because life is too short for bland rice!",
    "Spice up your mealtime with Daig.com’s curated collection of mouthwatering rice dishes!"
]

# Random featured dishes to showcase popular recipes
featured_dishes = [
    "Today's Highlight: Mughlai Biryani – Tender pieces of chicken cooked with aromatic spices and saffron-infused basmati rice.",
    "Chef's Choice: Hyderabadi Dum Biryani – Layers of fragrant rice and spicy marinated chicken, slow-cooked to perfection.",
    "Featured Recipe: Mutton Pulao – Succulent mutton pieces simmered with basmati rice, seasoned with whole spices.",
    "Must Try: Vegetable Pulao – A healthy yet flavorful mix of basmati rice, fresh vegetables, and subtle spices."
]

# Choose a random welcome message and featured dish
random_welcome = random.choice(welcome_messages)
random_dish = random.choice(featured_dishes)

# Display the random welcome message
st.markdown(f"### {random_welcome}")

# Display the random featured dish
st.markdown(f"**{random_dish}**")

# Additional information about Daig.com
st.markdown(
    """
    ### Explore Our Signature Dishes:
    - **Biryani**: A timeless classic with variations from Hyderabadi to Mughlai, each bursting with flavor.
    - **Pulao**: A subtle yet aromatic dish, from Chicken Pulao to Vegetable Pulao, perfect for any occasion.
    - **Specialty Rice**: Discover a variety of rice dishes beyond Pulao and Biryani – try our fried rice, coconut rice, and more.

    ### About Daig.com:
    Daig.com is a culinary treasure trove dedicated to bringing you the best rice-based dishes. Whether you’re a fan of the rich, aromatic Biryani or prefer the subtle elegance of Pulao, we’ve got recipes and tips to satisfy every palate. Our goal is to celebrate the art of cooking rice dishes that connect people to heritage and tradition.

    ### Visit Us:
    - Address: 456 Flavors Street, Spice City
    - Hours: Mon-Sun: 10 AM - 9 PM
    - Phone: (555) 987-6543
    """
)

# Optional: You can add a button for newsletter subscription or ordering a recipe book
if st.button("Subscribe to our Recipe Newsletter"):
    st.success("Thank you for subscribing! Get ready to receive the best Pulao and Biryani recipes.")
