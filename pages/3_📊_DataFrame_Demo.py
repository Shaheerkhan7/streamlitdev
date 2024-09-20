import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Customer Reviews", page_icon="💬")

# Title for the page
st.markdown("# Customer Testimonials & Reviews ⭐")
st.sidebar.header("Daig.com Customer Reviews")

# Section for customer testimonials
st.write(
    """
    Welcome to Daig.com's Customer Review section! We're proud to share what our customers are saying
    about our famous Pulao, Biryani, and other delicious dishes. Your feedback means everything to us.
    Here's what some of our happy customers have to say:
    """
)

# Example customer reviews (can be expanded with real data)
st.write("### Customer Testimonials:")
st.write("- **Sarah from Lahore**: *\"The best Biryani I've ever had! It reminded me of home.\"*")
st.write("- **Ahmed from Karachi**: *\"Daig.com's Pulao is out of this world. Highly recommended!\"*")
st.write("- **Fatima from Islamabad**: *\"Great food, excellent service. I can't get enough of their Biryani!\"*")

# Data visualization section header
st.markdown("## Customer Ratings Data Visualization 📊")
# st.write(
#     """Below is an example of how we can visualize customer ratings and feedback data using `st.write`
#     with Pandas DataFrames. This demo also highlights our ability to analyze large amounts of feedback to improve our services.
#     (Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
#     """
# )

# Function to get the UN dataset
@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

# Try loading the data and creating the visualizations
try:
    df = get_UN_data()

    # Multiselect for choosing specific regions/countries (can simulate customer regions)
    countries = st.multiselect(
        "Choose countries/regions", list(df.index), ["United States of America"]
    )
    if not countries:
        st.error("Please select at least one region.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Customer happy hour with Us", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Happy Consumer"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Happy Consumer:Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """ % e.reason
    )
