import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="medium")
with col1:
    st.image("assets/man.jpg", width=230)

with col2:
    st.title("AI & Data Analytics Innovation POCs", anchor=False)

# --- ABOUT SECTION ---
st.write("\n")
st.write("\n")
st.subheader("About AI & Data Analytics Innovations")
st.write(
    """
    Welcome to DMML AI & Data Analytics Innovation POCs, where we transform complex data into actionable insights and empower businesses with cutting-edge AI-driven solutions. Our mission is to harness the power of artificial intelligence and advanced data analytics to drive innovation, efficiency, and growth for organizations across industries.

    ### Who We Are
    We are a team of passionate data scientists, AI experts, and technology enthusiasts dedicated to solving real-world challenges through intelligent solutions. With a deep understanding of the latest advancements in AI, machine learning, and data science, we provide customized solutions that meet the unique needs of each client. Our diverse team brings together expertise from various fields, ensuring a comprehensive approach to every project we undertake.

    ### Our Vision
    We envision a world where data-driven decision-making is at the heart of every organization, enabling them to achieve unprecedented levels of success. Our goal is to be the trusted partner for businesses looking to leverage AI and data analytics to gain a competitive edge, optimize operations, and unlock new opportunities.

    ### What We Do
    At AI & Data Analytics Innovations, we offer a wide range of services designed to help businesses make the most of their data:

    - **Data Analytics:** We provide in-depth data analysis services that uncover valuable insights, helping businesses understand their customers, optimize processes, and make informed decisions.

    - **AI & Machine Learning:** Our team develops custom AI and machine learning models tailored to specific business needs, from predictive analytics to natural language processing and computer vision.

    - **Business Intelligence:** We create intuitive dashboards that visualize complex data, making it easy for stakeholders to monitor key metrics and trends.

    ### Our Approach
    Our approach is rooted in collaboration and innovation. We work closely with our clients to understand their unique challenges and objectives, ensuring that our solutions are aligned with their business goals. By combining domain expertise with the latest AI and data analytics tools, we deliver solutions that are not only effective but also scalable and future-proof.

    ### Why Choose Us?
    - **Expertise:** Our team consists of industry-leading professionals with extensive experience in AI, data analytics, and technology.
    - **Customization:** We understand that every business is different, and we tailor our solutions to meet your specific needs.
    - **Innovation:** We stay at the forefront of technological advancements to bring you the most innovative solutions.
    - **Results-Oriented:** Our focus is on delivering measurable results that drive business success.

    ### Join Us on the Journey to Innovation
    We are committed to helping businesses thrive in the digital age. Whether you’re just starting on your data journey or looking to take your AI capabilities to the next level, we are here to support you every step of the way.

    Thank you for choosing AI & Data Analytics Innovations. Together, let's unlock the potential of your data and drive your business forward.
    """
)

# # --- FOOTER SECTION ---
# st.write(
#     """
#     *For more details on how we can assist your enterprise in leveraging data for strategic 
#     advantage, feel free to reach out via the contact form.*
#     """
# )

# --- CONTACT FORM ---
# def show_contact_form():
#     st.subheader("Get in Touch")
#     st.text_input("First Name", placeholder="Enter your first name")
#     st.text_input("Last Name", placeholder="Enter your last name")
#     st.text_input("Email", placeholder="Enter your email address")
#     st.text_area("Message", placeholder="Enter your message here")
#     if st.button("Submit"):
#         st.success("Your message has been sent! We will get back to you soon.")

# # Show the contact form
# show_contact_form()