import streamlit as st

st.title("Student Mark Analyzer")

st.write("Enter student details")


st.title("Student Details Form")

st.header("Enter Student Information")

name = st.text_input("Student Name")
age = st.number_input("Age", min_value=1, max_value=100)
gender = st.radio("Gender", ["Male", "Female", "Other"])
course = st.selectbox("Course", ["B.Sc", "B.Com", "B.A", "BCA", "B.Tech","B.E"])
address = st.text_area("Address")
phone = st.text_input("Phone Number")

if st.button("Submit"):
    st.subheader("Student Details")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Course:", course)
    st.write("Address:", address)
    st.write("Phone:", phone)
    st.success("Details Submitted Successfully!")

name = st.text_input("Enter Student Name")
m1 = st.number_input("Enter Mark 1", min_value=0, max_value=100)
m2 = st.number_input("Enter Mark 2", min_value=0, max_value=100)
m3 = st.number_input("Enter Mark 3", min_value=0, max_value=100)

if st.button("Calculate Result"):
    total = m1 + m2 + m3
    average = total / 3

    st.subheader("Result")
    st.write("Name:", name)
    st.write("Total Marks:", total)
    st.write("Average:", average)

    if average >= 40:
        st.success("Result: PASS")
    else:
        st.error("Result: FAIL")

