import streamlit as st

st.title("Chai Maker App")
#widgets
add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("masala added to your chai")

tea_type = st.radio("Pick your chai base:", ["Milk","water","honey"])

st.write(f"Selected base {tea_type}")    
flavour = st.selectbox("choose flavour:",["Ginger", "honey","kesar","tulsi", "elaichi"])
st.write(f"Selected Flavour {flavour}")

sugar = st.slider("sugar level (spoon)", 0, 5, 2)
st.write(f"Selected sugar spoons {sugar}")

cups = st.number_input("How many cups", min_value = 1, max_value = 10, step = 1)
st.write(f"Selected no of cups {cups}")

name = st.text_input("Enter your name")
if name:
    st.write("Welcome, {name} ! your chai is on the way")
dob = st.date_input("Select your dob")
if st.button("Make Chai"):
    st.success("Your chai is being brewed")