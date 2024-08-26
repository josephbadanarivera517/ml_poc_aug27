import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "app_pages/about_us.py",
    title="What We Do",
    icon=":material/account_circle:",
    default=True,
)
# contact_page = st.Page(
#     "app_pages/contact_us.py",
#     title="Contact Us",
#     icon=":material/email:",
#     #default=True,
# )
project_1_page = st.Page(
    "app_pages/sentiment.py",
    title="Sentiment Analytics",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "app_pages/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

pg = st.navigation (
    {
        "About Us": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("C:/Users/Joseph Rivera/Desktop/project/AI_projects/ml_poc/assets/qbe_logo.png")
st.sidebar.markdown("Made with ❤️ by Joseph")

pg.run()
