import streamlit as st

st.title("Hi, I'm Krant, a product designer 🌟")

col1, col2 = st.columns(2)

with col1:
    # About me
    st.header('About Me')
    st.write("I'm equipped with a heart of a dreamer and the mind of a realist. "
             "I am passionate about pioneering in the realm of AI 🤖, specifically in crafting natural language interaction interfaces that seamlessly connect human intuition with AI 🧠."
)

    # Education
    st.header('Education')
    st.write("I'm currently a M.S. graduate student at UW ↗"
"I have a B.A. in Art History at Sichuan University ↗"
"Contact me via LinkedIn ↗")

    # Hobbies
    st.header('Fun Facts About Me!')
    st.write("I was an artist 👨🏻‍🎨"
             "I am a skilled badminton player 🏸"
             "I am a value investor 💵"
             "I am addicted to music 🎸, detective novel 🕵🏻‍♂️ and philosophy 🧐")


# 在右列添加图片和视频
with col2:
    # 个人资料图片
    st.image('my avatar1.jpg', caption='My Recent Photo', use_column_width=True)
    
    # 添加一段视频
    st.video('walking.mov')