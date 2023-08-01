import pandas as pd
import datetime

import streamlit as st

st.markdown("### Product configuration")
st.sidebar.markdown("# Load product")

with st.sidebar.expander("Existing Product"):
    products_sel = st.multiselect(
        'Load an existing product',
        ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'],
        max_selections=1,
        placeholder="Load an existing product",
        label_visibility="collapsed"
        )

st.sidebar.text("Or")
cap_button = st.sidebar.button("Configure new product", use_container_width=True)
