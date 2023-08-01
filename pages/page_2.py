import pandas as pd
import datetime

import streamlit as st
from st_pages import Page, show_pages, add_page_title



add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("streamlitt_examples/example_1.py", "Home", "🏠")
        Page("streamlitt_examples/pages/page_2.py", "Home2", "🏠")

    ]
)
streamlitt_examples

st.markdown("### Report run")
st.sidebar.markdown("# Settings")

with st.sidebar.expander("Date"):
    date_as_of = st.date_input(label="As of date", value=datetime.date.today(), format="MM.DD.YYYY")

with st.sidebar.expander("Profile"):
    profile_selected = st.selectbox(
    'Specific profile ot use?',
    ('No', 'Board-All', 'Board-Internal', 'Test-All', 'Board-Guernsey', 'Board-Cayman', 'Test last 15d',
    'IOC-Cockpit', 'PD Program Review', 'RE Program Review', 'OG LUX Program Review', 'Daniel Stopher Settings',
    'Infra Program Review', 'PE Program Review', 'Board - NONE', 'Board - Luxembourg'), 
    placeholder="Select...")

with st.sidebar.expander("Products"):
    products_selected = st.multiselect(
        'What products should be run?',
        ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'],
        ['Product 1'])

reports = ['Counterparty Report', 'Liquidity Report', 'Country Report', 'DebtConcentration Report', 
        'EquityConcentrationReport', 'Guidelines Report', 'FX Report', 'DART Report', 'Operational Report',
        'Performance Report', 'Benchmarking Report', 'GrossToNet Report', 'InvestmentPace Report', 
        'VintageConcentration Report', 'Contributors Report', 'ESG Report', 'TopPage Report', 
        'EvergreenLiquidity Report']

with st.sidebar.expander("Reports"):
    reports_all = st.checkbox('Run all reports', value=True)
    reports_selected = ["All"]
    if not reports_all:
        reports_selected = st.multiselect(
            'What reports should be run?',
            reports
            )

with st.sidebar.expander("Additional Settings"):
    guidelines_quarter_end = st.checkbox('Guidelines as of run date', value=True)
    guidelines_date = date_as_of
    if not guidelines_quarter_end:
        guidelines_date = st.date_input("Guidelines as of", datetime.date(2019, 7, 6), )


cap_button = st.button("Run")
st.write('Run date: {}'.format(date_as_of.strftime("%d %b, %Y")))
st.write('Profile:', profile_selected)
st.write('Products ({}x): '.format(len(products_selected)), ", ".join(products_selected))
st.write('Reports ({}x): '.format(len(reports_selected)), ", ".join(reports_selected))

st.write('Guidelines date:', guidelines_quarter_end)
st.write('Guidelines date:', guidelines_date)


def test_func(products):

    for i, prod in enumerate(products):
        print(i, prod)
        st.text("Running {}/{}: {}".format(i+1, len(products), prod))

if cap_button: # Make button a condition.
        test_func(products=products_selected)
        st.text("Execution Successful")
