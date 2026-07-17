import streamlit as st
st.title("Chai taste poll")
col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote masala chai")
with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/28836251/pexels-photo-28836251.jpeg",width = 100)
    vote2 = st.button("Vote adrak chai")

if vote1:
    st.success("Thanks for voting masala chai")
elif vote2:
    st.success("Thanks for voting adrak chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["masala", "adrak","kesar"])
st.write(f"welcome {name} and your {tea} chai is getting ready")

with st.expander("show chai making instructions"):
    st.write("""
             1. boil water with tea leaves
             2. add milk and spices
""")

st.markdown('# welcome to chai App')
st.markdown('> Blockquote') 