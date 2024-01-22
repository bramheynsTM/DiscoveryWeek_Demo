import streamlit as st

url = "https://docs.streamlit.io/library/cheatsheet"
st.write("Check out this %s for the Streamlit CheatSheet" %url)
st.title("Project Discovery Week")
st.header("This is my very first app")
st.write("Hello World!")
st.text("this is a text")
st.markdown('_Markdown_ is also a possibility')

st.code('for i in range(8): blablabla')

st.camera_input("Take a picture")

st.toast('Warming up...')