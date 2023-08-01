import pandas as pd

import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be

show_pages(
    [
        Page("example_1.py", "Home", "🏠"),
        Page("pages/page_3.py", "Product Configuration", "🏠"),
        Page("pages/page_2.py", "Run Standard Reports", "🏠"),
        Page("pages/page_4.py", "Closed Ended Liquidity", "🏠")
    ]
)



def func_1():

    st.write("Here's our first attempt at using data to create a table:")
    df_1 = pd.DataFrame({
                    'first column': [1, 2, 3, 4],
                    'second column': [10, 20, 30, 40]})

    st.dataframe(df_1.style.highlight_max(axis=0))
    st.table(df_1)
    st.text_input("Your name", key="name")

    st.write(st.session_state.name)

    add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
)
    st.sidebar.markdown("# Main page 🎈")

    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")

if __name__ == "__main__":
    print('hello')
    func_1()