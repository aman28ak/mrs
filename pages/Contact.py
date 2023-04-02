import streamlit as st
from PIL import Image

image = Image.open("aman.jpg")
st.image(image, caption="Aman kumar", width=200)

def contact():
    st.header("Contact Us")
    st.write("If you have any questions, comments, or feedback about our app, please reach out to us using the information below.")
    st.subheader("Email")
    st.write("Send us an email at [happy28vk@gmail.com](mailto:example@gmail.com).")
    st.subheader("Phone")
    st.write("Call us at 8955358254")
    st.subheader("Address")
    st.write("Vivekananda institute of professional studies")
    st.write("Delhi 110088 ")

if __name__ == "__main__":
    contact()