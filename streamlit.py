import streamlit as st


st.title('铭源的小屋')

st.write('')


st.write('铭源的小屋里面有很多东西，有他的衣服，有他的电脑，还有他的情感')


things = st.text_input('请输入你想要放进去的东西：')

article = st.selectbox(
    "或者说我来帮你选：",
    [
        '金条',
        '钻石',
        '美刀',
        '或者说我去厨房给你取点美刀'
    ]
)
st.write(f"你自愿放入：{article}")


res = st.radio(
    '你喜欢铭源的小屋吗？',
    ['喜欢','非常喜欢','超级无敌喜欢'])
height = st.slider("或者说你能忍受多少力量的击打",value = 6000,min_value = 3000, max_value = 10000, step = 1)
st.write(f"击打力量：{height}(单位/N)")
st.image('1.jpg')