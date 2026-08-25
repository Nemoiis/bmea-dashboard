import streamlit as st
import pandas as pd

elaBandA = pd.DataFrame({
    "Before": [2.8],
    "After": [58.3]
}, index=["Grade 3 ELA"])

def getDelta(a,b):
    if a > b:
        return a - b

    else:
        return b - a


st.title(":blue[BMEA] 2024-25 Academic Outcomes")
dfTwo = pd.read_excel("BmeaData.xlsx", sheet_name="AcademicOutcomes")

st.subheader("YLDP")
col1, col2, col3 = st.columns(3)
col1.metric("Growth Benchmark Met", "75%")
col2.metric("Avg Math Growth", "157%")
col3.metric("Above National Rate", "+57 pts")

st.subheader("Summer Discovery")
col4, col5, col6 = st.columns(3)
col4.metric("Grade 1 Math Proficient", "68.8%")
col5.metric("Grade 2 Below Basic Eliminated", "100%")
col6.metric("Students Moved Up 1+ Band", "70%")

st.bar_chart(elaBandA, height=200, horizontal= True)
st.caption("Grade 3 ELA proficiency rose 20x in five weeks")