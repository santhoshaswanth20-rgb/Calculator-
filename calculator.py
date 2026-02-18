import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Advanced Analytics Engine", layout="wide")
st.title("🔬 Advanced Scientific Computing Hub")

# Sidebar navigation
mode = st.sidebar.radio("Select Engine", ["Graphing & Calculus", "Matrix Algebra", "Physics & Constants", "Unit Converter"])

if mode == "Graphing & Calculus":
    st.header("📈 Interactive Function Plotter")
    equation = st.text_input("Enter a function of x (e.g., np.sin(x) * x**2)", "np.sin(x)")
    
    x_range = st.slider("Select X Range", -100, 100, (-10, 10))
    x = np.linspace(x_range[0], x_range[1], 500)
    
    try:
        y = eval(equation)
        df = pd.DataFrame({'x': x, 'y': y})
        fig = px.line(df, x='x', y='y', title=f"Plot of f(x) = {equation}")
        st.plotly_chart(fig, use_container_width=True)
        
        # Derivative (Quick approximation)
        dy = np.gradient(y, x)
        st.subheader("Calculus Analysis")
        st.write(f"**Mean Slope (Derivative):** {np.mean(dy):.4f}")
        st.write(f"**Area Under Curve (Integral):** {np.trapezoid(y, x):.4f}")
    except Exception as e:
        st.error(f"Invalid Equation: {e}")

elif mode == "Matrix Algebra":
    st.header("🔲 Matrix Operations")
    size = st.number_input("Matrix Size (N x N)", 2, 5, 2)
    st.write("Enter values for Matrix A:")
    
    # Create a dynamic input grid
    matrix_a = []
    for i in range(size):
        cols = st.columns(size)
        row = [cols[j].number_input(f"A[{i},{j}]", value=float(i+j)) for j in range(size)]
        matrix_a.append(row)
    
    if st.button("Analyze Matrix"):
        mat = np.array(matrix_a)
        st.write("**Determinant:**", np.linalg.det(mat))
        st.write("**Eigenvalues:**", np.linalg.eigvals(mat))
        st.write("**Inverse:**")
        st.write(np.linalg.inv(mat) if np.linalg.det(mat) != 0 else "Non-invertible")

elif mode == "Physics & Constants":
    st.header("⚛️ Fundamental Constants")
    col1, col2 = st.columns(2)
    col1.metric("Speed of Light (c)", "299,792,458 m/s")
    col2.metric("Planck Constant (h)", "6.626 x 10^-34 J·s")
    col1.metric("Gravitational Const (G)", "6.674 x 10^-11")
    col2.metric("Avogadro Number (Na)", "6.022 x 10^23")

elif mode == "Unit Converter":
    st.header("⚖️ Precision Converter")
    cat = st.selectbox("Category", ["Length", "Mass", "Energy"])
    val = st.number_input("Value", value=1.0)
    if cat == "Length":
        st.write(f"{val} Meters = {val * 3.28084:.4f} Feet")
        st.write(f"{val} Kilometers = {val * 0.621371:.4f} Miles")
elif mode == "Unit Converter":
    st.header("⚖️ Precision & Currency Converter")
    
    # Sub-tabs for Units vs Currency
    conv_type = st.radio("Conversion Type", ["International Currency", "Physical Units"], horizontal=True)
    
    if conv_type == "International Currency":
        st.subheader("💱 Real-Time Exchange")
        
        # Input amount
        amount = st.number_input("Enter Amount:", min_value=0.0, value=3.0)
        
        col1, col2 = st.columns(2)
        with col1:
            from_curr = st.selectbox("From", ["USD", "EUR", "GBP", "JPY"])
        with col2:
            to_curr = st.selectbox("To", ["INR", "USD", "EUR", "GBP", "CAD"])
            
        # Simplified conversion rates (For a 2026 feel)
        # In a real app, we'd use an API, but here are the current estimates:
        rates = {
            "USD_to_INR": 83.50,
            "EUR_to_INR": 90.20,
            "GBP_to_INR": 105.10,
            "USD_to_EUR": 0.92
        }
        
        pair = f"{from_curr}_to_{to_curr}"
        
        if st.button("Convert Currency"):
            if from_curr == to_curr:
                st.write(f"Result: {amount} {to_curr}")
            elif pair in rates:
                result = amount * rates[pair]
                st.success(f"💰 {amount} {from_curr} = {result:,.2f} {to_curr}")
            else:
                # Fallback if pair isn't in our hardcoded list
                st.warning("Rate for this specific pair is updating. Try USD to INR!")

    else:
        # Your previous Physical Units code goes here...
        st.write("Physical units like Length and Mass.")
elif mode == "Classic Calculator":
    st.header("🔢 Classic Math Engine")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_a = st.number_input("Enter Number A", value=10.0)
    with col2:
        num_b = st.number_input("Enter Number B", value=5.0)

    st.divider()
    
    # Grid for Operations
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row2_col1, row2_col2, row2_col3 = st.columns(3)

    if row1_col1.button("➕ Add", use_container_width=True):
        st.success(f"Result: {num_a + num_b}")
        
    if row1_col2.button("➖ Subtract", use_container_width=True):
        st.success(f"Result: {num_a - num_b}")
        
    if row1_col3.button("✖️ Multiply", use_container_width=True):
        st.success(f"Result: {num_a * num_b}")

    if row2_col1.button("➗ Divide", use_container_width=True):
        if num_b != 0:
            st.success(f"Result: {num_a / num_b}")
        else:
            st.error("Cannot divide by zero!")

    if row2_col2.button("² Square A", use_container_width=True):
        st.success(f"Result: {num_a ** 2}")

    if row2_col3.button("³ Cube A", use_container_width=True):
        st.success(f"Result: {num_a ** 3}")

    st.divider()
    if st.button("🏗️ Whole Square: (A + B)²", use_container_width=True):
        # Formula: (a+b)^2 = a^2 + 2ab + b^2
        result = (num_a + num_b) ** 2
        st.info(f"Formula: ({num_a} + {num_b})² = {result}")
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Ultimate Advanced Hub", layout="wide")

# 📺 THIS IS YOUR "REMOTE CONTROL" - Add the new modes here!
mode = st.sidebar.radio(
    "Select Calculator Mode", 
    ["Classic Calculator", "Currency Converter", "Graphing & Calculus", "Matrix Algebra", "Physics & Constants"]
)

# --- 1. CLASSIC MODE ---
if mode == "Classic Calculator":
    st.header("🔢 Classic Math Engine")
    col1, col2 = st.columns(2)
    with col1:
        num_a = st.number_input("Enter Number A", value=10.0)
    with col2:
        num_b = st.number_input("Enter Number B", value=5.0)

    st.divider()
    c1, c2, c3 = st.columns(3)
    if c1.button("➕ Add", use_container_width=True): st.success(f"Result: {num_a + num_b}")
    if c2.button("➖ Subtract", use_container_width=True): st.success(f"Result: {num_a - num_b}")
    if c3.button("✖️ Multiply", use_container_width=True): st.success(f"Result: {num_a * num_b}")
    
    c4, c5, c6 = st.columns(3)
    if c4.button("➗ Divide", use_container_width=True): 
        st.success(f"Result: {num_a / num_b}") if num_b != 0 else st.error("Zero Error!")
    if c5.button("² Square A", use_container_width=True): st.success(f"Result: {num_a ** 2}")
    if c6.button("³ Cube A", use_container_width=True): st.success(f"Result: {num_a ** 3}")
    
    if st.button("🏗️ Whole Square: (A + B)²", use_container_width=True):
        st.info(f"Result: {(num_a + num_b) ** 2}")

# --- 2. CURRENCY MODE ---
elif mode == "Currency Converter":
    st.header("💱 Global Currency Exchange")
    amount = st.number_input("Enter Amount in USD ($)", min_value=0.0, value=1.0)
    
    # 2026 Estimated Rate: 1 USD = 83.50 INR
    inr_val = amount * 83.50
    st.metric("Indian Rupees (₹)", f"₹{inr_val:,.2f}")
    st.write(f"Calculation: ${amount} x 83.50")

# --- OTHER MODES ---
elif mode == "Graphing & Calculus":
    st.write("Graphing code here...")
# (Keep your other 'elif' sections for Matrix and Physics below this)