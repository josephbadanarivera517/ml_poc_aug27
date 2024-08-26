import streamlit as st

# Apply custom CSS for tab spacing
st.markdown(
    """
    <style>
    /* Increase the space between tabs */
    div[data-baseweb="tab-list"] button {
        margin-right: 60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Sentiment Analysis")
st.markdown("<br>", unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3 = st.tabs(["About our Product", "Business Value", "Test our Product"])

# Content for the "About our Product" tab
with tab1:
    st.header("About our Product")
    st.write("Here you can provide detailed information about your product...")

# Content for the "Business Value" tab
with tab2:
    st.header("Business Value")
    st.write("Here you can explain the business value of your product...")

# Content for the "Test our Product" tab
with tab3:
    st.header("Test our Product")
    st.write("Here users can interact with and test your product...")