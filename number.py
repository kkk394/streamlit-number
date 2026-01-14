import streamlit as st
st.title("電卓")
num1=st.number_input(input("1つ目の数字を入力してください"))
num2=st.number_input(input("2つ目の数字を入力してください"))
operation=st.selectbox("計算方法を選んでください",("足し算","引き算","掛け算","割り算"))
if st.button("計算する"):
    if operation=="足し算":
         st.write("結果:",num1+num2)
    elif operation=="引き算":
         st.write("結果:",num1-num2)
    elif operation=="掛け算":
         st.write("結果:",num1*num2)
    elif operation=="割り算":
        if num2 !=0:
            st.write("結果:",num1/num2)
        else:
            st.write("エラー:0で割ることはできません")