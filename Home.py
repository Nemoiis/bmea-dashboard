import streamlit as st
import pandas as pd

st.title(":blue[BMEA] Impact Dashboard")
st.caption("Boldly Moving Education Ahead — 2024-25 program results")

col1, col2, col3 = st.columns(3)
col1.metric("Students Served", "275")
col2.metric("Grade 3 ELA Proficient", "58.3%")
col3.metric("Educator Retention", "100%")

st.divider()
st.write("Explore a section:")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("**Summer Discovery**")
        st.caption("Year over year growth in reach and staffing.")
        st.page_link("pages/1_SummerData.py", label="View")

with col2:
    with st.container(border=True):
        st.markdown("**Academic Outcomes**")
        st.caption("Proficiency and growth across YLDP and summer.")
        st.page_link("pages/2_AcademicOutcomes.py", label="View")
