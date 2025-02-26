import streamlit as st

conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
    },
    "Mass": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274,
    },
    "Area": {
        "Square Meter": 1,
        "Square Kilometer": 0.000001,
        "Square Centimeter": 10000,
        "Square Millimeter": 1000000,
        "Hectare": 0.0001,
        "Acre": 0.000247105,
        "Square Mile": 3.861e-7,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639,
        "Square Inch": 1550,
    },
    "Volume": {
        "Cubic Meter": 1,
        "Liter": 1000,
        "Milliliter": 1000000,
        "Cubic Centimeter": 1000000,
        "Cubic Millimeter": 1000000000,
        "Cubic Inch": 61023.7,
        "Cubic Foot": 35.3147,
        "Cubic Yard": 1.30795,
        "Gallon": 264.172,
        "Quart": 1056.69,
        "Pint": 2113.38,
        "Cup": 4226.75,
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15,
    },
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
    else:
        base_value = value / conversion_factors[category][from_unit]
        return base_value * conversion_factors[category][to_unit]

st.title("Unit Converter Made By Sumaira Malik")

category = st.selectbox("Select Category", list(conversion_factors.keys()))
from_unit = st.selectbox("From Unit", list(conversion_factors[category].keys()) if category else [])
to_unit = st.selectbox("To Unit", list(conversion_factors[category].keys()) if category else [])
value = st.number_input("Enter Value", min_value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result} {to_unit}")
