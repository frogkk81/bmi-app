import streamlit as st

st.title("BMI 測試")

sex = st.radio("你是男的女的:", ('M', 'F'))
weight = st.number_input("請輸入體重 (kg)", min_value=1.0)
height = st.number_input("請輸入身高 (cm)", min_value=1.0)

st.write("你選擇的性別是:", sex)
st.write("你的體重是:", weight)
st.write("你的身高是:", height)

if st.button("計算 BMI"):
    bmi = weight / (height / 100) ** 2
    st.write(f"你的 BMI 是: {bmi:.2f}")

    if sex == 'M':
        if bmi > 25:
            st.write("結果：死肥宅")
        elif bmi < 21:
            st.write("結果：竹竿人")
        else:
            st.write("結果：帥哥")
    else:
        if bmi > 22:
            st.write("結果：死胖子")
        elif bmi < 19:
            st.write("結果：人乾")
        else:
            st.write("結果：辣妹")
