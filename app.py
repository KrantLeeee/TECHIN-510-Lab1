import streamlit as st

st.title("Hi, I'm Krant, a product designer 🌟")

col1, col2 = st.columns(2)

with col1:
    # About me
    st.header('About Me')
    st.write("I'm equipped with a heart of a dreamer and the mind of a realist.\n"
             "I am passionate about pioneering in the realm of AI 🤖, specifically in crafting natural language interaction interfaces that seamlessly connect human intuition with AI 🧠.")

    # Education
    st.header('Education')
    if st.button('M.S. graduate student at UW'):
        st.markdown("https://gix.uw.edu/program/msti/", unsafe_allow_html=True)
    if st.button('B.A. in Art History at Sichuan University'):
        st.markdown("https://jwc.scu.edu.cn/", unsafe_allow_html=True)
    if st.button('Contact me via LinkedIn'):
        st.markdown("http://www.linkedin.com/in/krant-lee1", unsafe_allow_html=True)

    # Hobbies
    st.header('Fun Facts About Me!')
    st.write("I was an artist 👨🏻‍🎨")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("I am a skilled badminton player 🏸")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("I am a value investor 💵")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("I am addicted to music 🎸, travel 🚗, detective novel 🕵🏻‍♂️ and philosophy 🧐")

# Add img & video
with col2:
    st.image('my avatar1.jpg', caption='My Recent Photo', use_column_width=True)

    st.image('My Painting.jpg', caption='My Painting', use_column_width=True)

    st.video('walking.mov')
