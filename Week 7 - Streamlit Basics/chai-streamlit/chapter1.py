import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")
chai = st.selectbox("Your fav chai:", ["Masala Chai","Lemon Tea",
        "Ginger Tea", "Kesar chai"])
st.write(f"You choose {chai}. Excellent choice")
st.success("Your Chai has been brewed")
