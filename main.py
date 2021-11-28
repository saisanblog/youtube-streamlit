
import streamlit as st

import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
  latest_iteration.text(f"Interation{i+1}")
  bar.progress(i+1)
  time.sleep(0.1)

"Done!!!"

left_column,right_column=st.beta_columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
  right_column.write("ここは右カラムです")


""" if st.checkbox("Show Image"):#checkbocxにチェックが入ると表示
  img=Image.open("D:\いらすとや/cat02_moyou_white.png")
  st.image(img,caption="mayou",use_column_width=True) """


expander=st.beta_expander("問い合わせ")
expander.write("問い合わせを描く")