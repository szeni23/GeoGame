import streamlit as st
from page1 import page1
from page2 import page2

st.set_page_config(
    page_title="GeoGame",
    layout="wide"
)

tabs = {
    "GeoGame": page1,
    "Analyze counties": page2,
}

def main():
    selection = st.sidebar.radio(" ", list(tabs.keys()))

    page = tabs[selection]
    with st.spinner(f"Load {selection}..."):
        page()


if __name__ == "__main__":
    main()
