import streamlit as st
import numpy as np

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")
st.title("🧮 Advanced Calculator")

# Operation selection
operation = st.selectbox("Choose an operation:", [
    "Addition", "Subtraction", "Multiplication", "Division",
    "Power", "Modulus", "Square Root", "Logarithm",
    "Sine", "Cosine", "Tangent"
])

result = None

# Input fields and operation logic
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Modulus"]:
    num1 = st.number_input("Enter first number:", format="%.4f")
    num2 = st.number_input("Enter second number:", format="%.4f")
    
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero.")
        elif operation == "Power":
            result = np.power(num1, num2)
        elif operation == "Modulus":
            result = num1 % num2

elif operation in ["Square Root", "Logarithm", "Sine", "Cosine", "Tangent"]:
    num = st.number_input("Enter the number:", format="%.4f")
    
    if st.button("Calculate"):
        if operation == "Square Root":
            if num >= 0:
                result = np.sqrt(num)
            else:
                st.error("Cannot take square root of a negative number.")
        elif operation == "Logarithm":
            if num > 0:
                result = np.log10(num)
            else:
                st.error("Logarithm undefined for non-positive numbers.")
        elif operation == "Sine":
            result = np.sin(np.radians(num))
        elif operation == "Cosine":
            result = np.cos(np.radians(num))
        elif operation == "Tangent":
            result = np.tan(np.radians(num))

# Display result
if result is not None:
    st.success(f"Result: {result:.4f}")
