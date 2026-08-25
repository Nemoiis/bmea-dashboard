import streamlit as st
import pandas as pd

def getDelta(a,b):
    if a > b:
        return a - b

    else:
        return b - a

#DataFrames being referenced
reach_df = pd.DataFrame({
    "2024": [130, 297, 74],
    "2025": [275, 432, 117]
}, index=["Students", "Applications", "Schools"])

staffing_df = pd.DataFrame({
    "2024": [14, 6, 48],
    "2025": [35, 14, 61]
}, index=["HS Mentors", "Teacheres", "Zip Codes"])

st.title(":blue[BMEA] :yellow[Summer] 2024-25 Data")
dfOne = pd.read_excel("BmeaData.xlsx", sheet_name="SummerData")

stu_2024 = dfOne.loc[dfOne["Year"] == 2024, "Students"].values[0]
stu_2025 = dfOne.loc[dfOne["Year"] == 2025, "Students"].values[0]

HsM_2024 = dfOne.loc[dfOne["Year"] == 2024, "HS Mentors"].values[0]
HsM_2025 = dfOne.loc[dfOne["Year"] == 2025, "HS Mentors"].values[0]

Apps_2024 = dfOne.loc[dfOne["Year"] == 2024, "Applications"].values[0]
Apps_2025 = dfOne.loc[dfOne["Year"] == 2025, "Applications"].values[0]

Schools_2024 = dfOne.loc[dfOne["Year"] == 2024, "School Rep"].values[0]
Schools_2025 = dfOne.loc[dfOne["Year"] == 2025, "School Rep"].values[0]


col1, col2, col3, col4 = st.columns(4)
col1.metric("Students", stu_2025, delta=getDelta(stu_2024, stu_2025))
col2.metric("High School Mentors", HsM_2025, delta=getDelta(HsM_2024, HsM_2025))
col3.metric("Applications Recieved", Apps_2025, delta=getDelta(Apps_2024, Apps_2025))
col4.metric("Schools", Schools_2025, delta=getDelta(Schools_2024, Schools_2025))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Program Reach")
    st.bar_chart(reach_df)
    st.line_chart(reach_df)

with col2:
    st.subheader("Program Staffing")
    st.bar_chart(staffing_df)
    st.line_chart(staffing_df)


































dfThree = pd.read_excel("BmeaData.xlsx", sheet_name="BMEADATA")


