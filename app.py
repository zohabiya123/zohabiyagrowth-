#streamlit
import streamlit as st 

st.set_page_config(page_title= "growth mindset projects", project_icon="★")
st.title("Growth Mindset challenge: Web App with Streamlit ")

st.header("🚀 welcome to your Growth Journey!")🌟
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

#quote section
st.header("💡 Today's Growth Mindset quote")
st.write("Embrace the struggle, it's shaping your strength")

st.header("what's your challenge Today?")
user_inpur = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
st.succes(f" you re facing: {user_input}. keep pushing forwards towards your goals and wishes!")
else:
st.warning("Tell us about your challenge to get started!")

#reflexing
if reflection:
st.header(" Rflect on your learning")
reflectionst.text area("write your reflections here:")

if reflection:
st.succes(f"Great Insight! your reflection: {reflection}")
else:
st.info("Reflect not just on what you did, but who you’re becoming.")

#acheivements
st.header("Honor your progress!")
achievements = st.text_input("What’s a little victory you’ve had recently?")

if achievment:
st.success(f"💫So proud of you for reaching that!: {acheivment}")
else:
st.info("Progress is progress, no matter the size! Share one now! 😍")

#footer
st.writer("- - -")
st.write("Trust yourself—you're growing every step of the way! ✨")
st.write("created by zohabiya naeem" ⭑⭑)