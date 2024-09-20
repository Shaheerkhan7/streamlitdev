import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="About", page_icon="📈")

st.markdown("# Our Sales 🍛")

# Sidebar welcome message
st.sidebar.header("Welcome! We at Daig.com are a family")
st.sidebar.write(
    """
    At Daig.com, we bring generations of family recipes to your table. From our famous Pulao to the irresistible Biryani, every dish is made with love and tradition.
    """
)

# Main content text
st.write(
    """
    At Daig.com, we are proud to offer not only the finest rice dishes but also an incredible dining experience. Check out our sales data below, which illustrates our growing family of happy customers!
    """
)
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)


start_year = 2004
years = list(range(start_year, start_year + 21))  # Simulate 20 years (2020 - 2040)
current_year_index = 0

for i in range(1, 101):
    # Simulate new sales data for 5 random years at a time
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    
    # Update the status text to show the current year instead of percentage
    current_year = years[current_year_index // 5]  # Each 5 steps represents 1 year
    status_text.text(f"Year: {current_year}")
    
    # Add new data to the line chart
    chart.add_rows(new_rows)

    # Update the progress bar
    progress_bar.progress(i)
    
    # Store the last row for the next iteration
    last_rows = new_rows
    
    # Move to the next year for every 5 iterations
    current_year_index += 1
    
    # Add a short delay to simulate time progression
    time.sleep(0.05)

# Clear the progress bar once done
progress_bar.empty()

# Final message
st.write(f"Simulation complete. Reached year {years[-1]}! Thankyou, Order comfortably at home")
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")