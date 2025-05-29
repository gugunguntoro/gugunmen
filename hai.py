import streamlit as st

st.title("Aplikasi Gugun Men")

nama = st.text_input("Masukkan nama kamu :)")

if st.button("Cek"):
    if not nama:
        st.warning("Masukkan nama kamu dulu dong")
    else:
        st.success(f"Hai {nama}, aku Gugun Men, aku siap membantu kamu untuk membasmi penjahat dimuka bumi ini. Tapi aku makan dulu, ya... Kamu juga makan, karena melawan penjahat itu butuh energi.")
    

