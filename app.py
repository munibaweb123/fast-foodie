import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Page setup
st.set_page_config(page_title="FastFoodie 🍔", layout="centered")

# Sidebar Navigation
menu = ["Home", "Menu", "Order", "Contact"]
choice = st.sidebar.selectbox("Navigate", menu, index=menu.index(st.session_state.page))
st.session_state.page = choice

# ---------------- HOME PAGE ----------------
if st.session_state.page == "Home":
    st.markdown(
        """
        <style>
        .banner {
            background-color: #FFDE59;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 20px;
        }
        .banner h1 {
            font-size: 3em;
            color: #D62828;
            font-family: 'Comic Sans MS', cursive;
        }
        .banner p {
            font-size: 1.3em;
            color: #333;
        }
        .item-card {
            background-color: #fff3cd;
            color: #856404;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class='banner'>
        <h1>🍔 FastFoodie Express</h1>
        <p>Your favorite fast food, made fresh & delivered fast!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/beef-burger.jpg", caption="Classic Burger 🍔", use_container_width=True)
        st.markdown("<div class='item-card'><strong>$5.99</strong></div>", unsafe_allow_html=True)

    with col2:
        st.image("images/french-fries.jpg", caption="Crispy Fries 🍟", use_container_width=True)
        st.markdown("<div class='item-card'><strong>$2.49</strong></div>", unsafe_allow_html=True)

    with col3:
        st.image("images/soda.jpg", caption="Cold Soda 🥤", use_container_width=True)
        st.markdown("<div class='item-card'><strong>$1.99</strong></div>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🎉 Order now and get 10% off your first meal!")

    if st.button("Go to Menu"):
        st.session_state.page = "Menu"
        st.rerun()

# ---------------- MENU PAGE ----------------
elif st.session_state.page == "Menu":
    st.title("📋 Our Menu")
    st.image("images/french-fries.jpg", width=250, caption="Crispy Fries")
    st.write("**Fries** - $2.49")
    st.image("images/beef-burger.jpg", width=250, caption="Juicy Burger")
    st.write("**Burger** - $5.99")
    st.image("images/fresh-juice.jpg", width=250, caption="Fresh Juice")
    st.write("**Fresh Juice** - $1.99")
    st.image("images/soda.jpg", width=250, caption="Soda")
    st.write("**Soda** - $1.49")
    st.image("images/chocolate-frappuccino-table.jpg", width=250, caption="Chocolate Frappuccino")
    st.write("**Chocolate Frappuccino** - $3.99")
    st.image("images/milkshake-set-table.jpg", width=250, caption="Milkshake")
    st.write("**Milkshake** - $2.99")
    st.image("images/shwarma.jpg", width=250, caption="Shawarma")
    st.write("**Shawarma** - $4.99")
    st.image("images/pepperoni-pizza-slice.jpg", width=250, caption="Pepperoni Pizza")
    st.write("**Pepperoni Pizza** - $6.99")
    st.image("images/strawberry-mojito.jpg", width=250, caption="Strawberry Mojito")
    st.write("**Strawberry Mojito** - $3.49")

# ---------------- ORDER PAGE ----------------
elif st.session_state.page == "Order":
    st.title("🛒 Place Your Order")
    st.write("Fill in your order details below:")

    with st.form("order_form"):
        name = st.text_input("Name")
        food = st.selectbox("Select Item", ["Burger", "Fries", "Soda"])
        quantity = st.number_input("Quantity", 1, 10)
        submit = st.form_submit_button("Order Now")

        if submit:
            st.success(f"Thank you {name}, your order of {quantity} {food}(s) has been placed!")

# ---------------- CONTACT PAGE ----------------
elif st.session_state.page == "Contact":
    st.title("📞 Contact Us")
    st.write("We're happy to hear from you!")
    st.text_input("Your Name")
    st.text_input("Email")
    st.text_area("Message")
    if st.button("Send"):
        st.success("Thanks! We'll get back to you soon.")
# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    """
    <style>
    footer {
        text-align: center;
        padding: 20px;
        background-color: #FFDE59;
        color: #D62828;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<footer>© 2023 FastFoodie Express. All rights reserved.</footer>", unsafe_allow_html=True)