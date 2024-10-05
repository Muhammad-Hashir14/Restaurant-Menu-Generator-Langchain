import streamlit as st
import os
from langchain_helper import generate_name_and_menu, clean_menu_items
# from dotenv import load_dotenv


# load_dotenv()
# api_key = os.getenv("API_KEY")
api_key = st.secrets["api_keys"]["API_KEY"]
os.environ["GOOGLE_API_KEY"] = api_key

st.set_page_config(layout = "wide")

st.header("🍽️ Restaurant Name and Menu Generater 🥂")
st.write("------------------------------------------------------------------------------------")

cuisine = st.sidebar.selectbox("Select a Cuisine", ("Pakistani", "Indian", "Chinese", "Mexican", "Italian", "Japnese",
                                          "Korean", "Thai","Vietnamese","Spanish", "Turkish", "Russian", 
                                          "German", "American", "Canadian","Moroccan","Nigerian"))

number = st.sidebar.slider("Select Number of Menu Items", 0, 20, 5, step = 4)

button = st.sidebar.button("submit")


if button:
    cusine = generate_name_and_menu(cuisine,number)    
    name = cusine["restaurant_name"].replace('"','')
    items = cusine['menu_items']
    st.write("   *Suggested Restaurant Name*")
    st.write(f"## {name}")
    st.write("--------------------------------------------------------------------------------")
    st.write(f"   *Suggested Menu Items for {name}*")
    items = clean_menu_items(items)
    for item in items:
      if item.strip() != "":
        st.write(f"- {item}")
     