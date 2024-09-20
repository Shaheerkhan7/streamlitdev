# import streamlit as st
# # st.balloons()
# st.snow()
# st.write("# Streamlit App")

# # x = st.text_input("How May I Be Of Service")

# # st.write("Hello, *World!* :sunglasses:")

# # Function to generate responses based on user input
# # def get_response(user_input):
# #     responses = {
# #         "hello": "Hello! How can I assist you today?",
# #         "how are you": "I'm an AI, so I don't have feelings, but thanks for asking!",
# #         "bye": "Goodbye! Feel free to come back anytime.",
# #     }
# #     return responses.get(user_input.lower(), "Sorry, I don't understand that.")


# # with st.sidebar:
# #     # Create a container for the messages
# #     messages = st.container(height=200)

# #     # Get user input from the chat input field
# #     if prompt := st.chat_input("Say something"):
# #         # Display user input
# #         with messages:
# #             messages.chat_message("user").write(prompt)

# #             # Generate and display assistant response
# #             response = get_response(prompt)
# #             messages.chat_message("assistant").write(response)


# # Initialize session state to manage chat window visibility
# if 'chat_open' not in st.session_state:
#     st.session_state['chat_open'] = False

# # Toggle chat window visibility when the button is clicked
# if st.button("Toggle Chat"):
#     st.session_state['chat_open'] = not st.session_state['chat_open']

# # Function to generate responses based on user input
# def get_response(user_input):
#     responses = {
#         "hello": "Hello! How can I assist you today?",
#         "how are you": "I'm an AI, so I don't have feelings, but thanks for asking!",
#         "bye": "Goodbye! Feel free to come back anytime."
#     }
#     return responses.get(user_input.lower(), "Sorry, I don't understand that.")

# # Display chat window if it's open
# if st.session_state['chat_open']:
#     st.markdown("### Chat Window")
#     # Create a container for the chat messages
#     chat_container = st.container()

#     # Get user input from the chat input field
#     if prompt := st.chat_input("Say something"):
#         with chat_container:
#             # Display user input
#             chat_container.chat_message("user").write(prompt)
            
#             # Generate and display assistant response
#             response = get_response(prompt)
#             chat_container.chat_message("assistant").write(response)
# st.divider()
# st.write("# Streamlit App")
# # with st.sidebar:
# #     messages = st.container(height=500)
# #     if prompt := st.chat_input("Say something"):
# #         messages.chat_message("user").write(prompt)
# #         messages.chat_message("assistant").write(f"Echo: {prompt}")

# # st.html()

# # import pandas as pd
# # data = pd.read_csv("data.csv")
# # st.write(data)
