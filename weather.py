import requests

api_url = "http://api.weatherapi.com/v1/current.json?"
api_key = "cc1c8c16dc414858a9e90359250303"

st.title("Weather App")
city = st.text_input('enter a city name')
if city:
    url = api_url+"key="+api_key +"&q="+city
    res = requests.get(url)
    if res.status_code ==200:
        data = res.json()
        st.write(f"the current temperature in {city} is : {data["current"]["temp_c"]}degr c")
        st.write(data['current'])
        
    else:
        st.write("city not found")mport streamlit as st
import r
de_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

