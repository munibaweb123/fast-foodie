import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "cart" not in st.session_state:
    st.session_state.cart = {}

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

    menu_items = [
        {"name": "Fries", "price": 2.49, "image": "images/french-fries.jpg"},
        {"name": "Burger", "price": 5.99, "image": "images/beef-burger.jpg"},
        {"name": "Juice", "price": 1.99, "image": "images/fresh-juice.jpg"},
        {"name": "Soda", "price": 1.49, "image": "images/soda.jpg"},
        {"name": "Frappuccino", "price": 3.99, "image": "images/chocolate-frappuccino-table.jpg"},
        {"name": "Milkshake", "price": 2.99, "image": "images/milkshake-set-table.jpg"},
        {"name": "Shawarma", "price": 4.99, "image": "images/shwarma.jpg"},
        {"name": "Pizza", "price": 6.99, "image": "images/pepperoni-pizza-slice.jpg"},
        {"name": "Mojito", "price": 3.49, "image": "images/strawberry-mojito.jpg"},
    ]

    for item in menu_items:
        st.image(item["image"], width=250, caption=item["name"])
        st.write(f"**{item['name']}** - ${item['price']:.2f}")
        if st.button(f"Add {item['name']} to cart", key=f"{item['name']}_button"):
            if item["name"] in st.session_state.cart:
                st.session_state.cart[item["name"]]["quantity"] += 1
            else:
                st.session_state.cart[item["name"]] = {"price": item["price"], "quantity": 1}
            st.success(f"{item['name']} added to cart!")

# ---------------- ORDER PAGE ----------------
elif st.session_state.page == "Order":
    st.title("🛒 Your Cart")

    if st.session_state.cart:
        total = 0
        for item, details in st.session_state.cart.items():
            st.write(f"{item} - ${details['price']:.2f} x {details['quantity']}")
            total += details["price"] * details["quantity"]
        st.write(f"**Total: ${total:.2f}**")
        st.markdown("---")
        st.write("Fill in your order details below:")

        with st.form("order_form"):
            name = st.text_input("Name")
            submit = st.form_submit_button("Place Order")

            if submit:
                st.success(f"Thank you {name}, your order has been placed!")
                st.session_state.cart = {}  # Clear the cart after order
    else:
        st.write("Your cart is empty. Go to the Menu to add items.")

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