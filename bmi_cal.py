import streamlit as st

# import time


page_bg_img = """
<style>
.stApp {
background-image: url("https://cdn.dribbble.com/users/4320847/screenshots/11368106/media/257b93c68aeba658d9509e1e0e3ae60c.jpg");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("BMI Calculator")

stat = st.radio("Select your Weight format: ", ("kgs", "pounds", "ounce"))

weight = st.number_input("Enter you weight (in {})".format(stat))


if stat == "pounds":
    weights = weight * 0.45359237

elif stat == "ounce":
    weights = weight * 0.028

elif stat == "kgs":
    weights = weight

status = st.radio("Select your height format: ", ("cms", "meters", "feet"))

if status == "cms":
    height = st.number_input("Centimeters")

    try:
        bmi = weights / ((height / 100) ** 2)
    except:
        st.text("Enter your height")

elif status == "meters":
    height = st.number_input("Meters")

    try:
        bmi = weights / (height**2)
    except:
        st.text("Enter your height")

else:
    height = st.number_input("Feet")

    try:
        bmi = weights / ((height / 3.28) ** 2)
    except:
        st.text("Enter your height")

if st.button("Calculate BMI"):
    st.text("Your BMI Index is {}.".format(bmi))

    st.balloons()

    # st.subheader("Progress bar")
    # st.progress(10)

    # st.subheader("Wait the execution")
    # with st.spinner("Wait for it..."):
    #     time.sleep(10)

    if bmi < 16:
        st.error("You are Extremely Underweight !!")
    elif bmi >= 16 and bmi < 18.5:
        st.warning("You are Underweight!")
    elif bmi >= 18.5 and bmi < 25:
        st.success("You are Healthy.")
    elif bmi >= 25 and bmi < 30:
        st.warning("You are Overweight!")
    elif bmi >= 30:
        st.error("You are Extremely Overweight !!!")
