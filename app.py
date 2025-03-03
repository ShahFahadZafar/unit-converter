import streamlit as st
import requests

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

def get_currency_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("rates", {})
    return {}

def main():
    st.title("Unit Converter")
    
    category = st.selectbox("Select Category", ["Length", "Weight", "Temperature", "Volume", "Speed", "Area", "Energy", "Time", "Pressure", "Power", "Currency"])
    value = st.number_input("Enter Value", min_value=0.0, format="%f")
    
    if category == "Length":
        units = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Millimeters": 0.001, "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048, "Inches": 0.0254, "Nautical Miles": 1852}
    elif category == "Weight":
        units = {"Kilograms": 1, "Grams": 0.001, "Milligrams": 0.000001, "Pounds": 0.453592, "Ounces": 0.0283495, "Tonnes": 1000, "Stones": 6.35029}
    elif category == "Volume":
        units = {"Liters": 1, "Milliliters": 0.001, "Cubic Meters": 1000, "Cubic Centimeters": 0.001, "Cubic Inches": 0.0163871, "Cubic Feet": 28.3168, "Gallons (US)": 3.78541, "Gallons (UK)": 4.54609}
    elif category == "Speed":
        units = {"Meters per second": 1, "Kilometers per hour": 0.277778, "Miles per hour": 0.44704, "Knots": 0.514444, "Feet per second": 0.3048}
    elif category == "Area":
        units = {"Square Meters": 1, "Square Kilometers": 1e6, "Square Centimeters": 0.0001, "Square Millimeters": 0.000001, "Square Miles": 2.59e6, "Acres": 4046.86, "Hectares": 10000}
    elif category == "Energy":
        units = {"Joules": 1, "Kilojoules": 1000, "Calories": 4.184, "Kilocalories": 4184, "Watt-hours": 3600, "Kilowatt-hours": 3.6e6}
    elif category == "Time":
        units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800, "Months": 2.628e6, "Years": 3.154e7}
    elif category == "Pressure":
        units = {"Pascals": 1, "Kilopascals": 1000, "Bars": 100000, "Atmospheres": 101325, "PSI": 6894.76}
    elif category == "Power":
        units = {"Watts": 1, "Kilowatts": 1000, "Horsepower": 745.7, "Megawatts": 1e6}
    elif category == "Currency":
        rates = get_currency_rates()
        from_unit = st.selectbox("From Currency", list(rates.keys()))
        to_unit = st.selectbox("To Currency", list(rates.keys()))
        if st.button("Convert"):
            if from_unit in rates and to_unit in rates:
                converted_value = value * (rates[to_unit] / rates[from_unit])
                st.success(f"Converted Value: {converted_value:.2f} {to_unit}")
            else:
                st.error("Currency conversion not available")
        return
    else:  # Temperature
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        
        if st.button("Convert"):
            if from_unit == to_unit:
                st.success(f"Converted Value: {value:.2f} {to_unit}")
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                st.success(f"Converted Value: {(value * 9/5) + 32:.2f} {to_unit}")
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                st.success(f"Converted Value: {value + 273.15:.2f} {to_unit}")
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                st.success(f"Converted Value: {(value - 32) * 5/9:.2f} {to_unit}")
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                st.success(f"Converted Value: {((value - 32) * 5/9) + 273.15:.2f} {to_unit}")
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                st.success(f"Converted Value: {value - 273.15:.2f} {to_unit}")
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                st.success(f"Converted Value: {((value - 273.15) * 9/5) + 32:.2f} {to_unit}")
        return
    
    from_unit = st.selectbox("From Unit", list(units.keys()))
    to_unit = st.selectbox("To Unit", list(units.keys()))
    
    if st.button("Convert"):
        converted_value = convert_units(value, from_unit, to_unit, units)
        if converted_value is not None:
            st.success(f"Converted Value: {converted_value:.2f} {to_unit}")
        else:
            st.error("Invalid conversion")

if __name__ == "__main__":
    main()
