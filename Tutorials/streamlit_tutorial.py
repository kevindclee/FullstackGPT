import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime as dt

today = dt.today().strftime("%H:%M:%S")
st.title(today)

st.title("Hello world!")

# swiss knife of streamlit.
# streamlit tries to make UI of anything you throw in inside write()
# list, dict, class, numpy, etc.
st.write()

model = st.selectbox(
    "Choose your model",
    (
        "GPT-3",
        "GPT-4"
    )
)
st.write(model)

if model == "GPT-3":
    st.write("cheap")
else:
    st.write("not cheap")

name = st.text_input("What is your name?")
st.write(name)

st.subheader("Welcome to Streamlit!")

st.markdown("""
    #### I love it!
""")

p = PromptTemplate.from_template("hi")
st.write(p)


# In streamlit, every thing in the page from top to bottom is re-run, 
# when something gets updated in the page.
value = st.slider("temperature", min_value=0.1, max_value=1.0)
st.write(value)


# Sidebars
# Option 1
st.sidebar.title("sidebar title")
st.sidebar.text_input("xxx")

# Option 2
with st.sidebar:
    st.title("sidebar title")
    st.text_input("xxx")

# Tabs
tab1, tab2, tab3 = st.tabs(["A", "B", "C"])
with tab1:
    st.write('a')

with tab2:
    st.write('b')

with tab3:
    st.write('c')