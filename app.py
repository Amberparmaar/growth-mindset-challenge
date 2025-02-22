import streamlit as st

st.set_page_config(page_title= "Growth mindset project", page_icon="⭐" )

#title & description
st.title("🌱 Growth mindset challenge By Amber Parmaar")
st.header("Welcome to your Growth Mindset Project")
st.write("Embrace the challange, learn from your mistakes, and grow from them. This is a project to help you develop a growth mindset.")

st.markdown("---")

#quote section
st.header("🌑 Today's wisdom on personal growth")
st.write("'Neither success nor failure defines you; your determination to move forward does.'- Unknown")

st.markdown("---")

st.header("💪 How are you challenging yourself today?")
user_input = st.text_area("Share your goals and progress below.")

#condition

if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward toward your goals! 🚀")
else:
    st.warning("Tell us about your challenge to get started! 🌟")

   
st.markdown("---")

#reflection section
st.header("Reflect on your progress")
st.write("Take a moment to reflect on your progress and what you've learned from your experiences.")
reflection = st.text_area("What have you learned from your challenges today?")

if reflection:
    st.success(f"Great insight! You've learned: {reflection} 🌟")
else:
        st.info("Share your reflection to continue growing! 🌱")

st.markdown("---")

#achievements section
st.header("🏆 Celebrate your achievements")
achievement = st.text_area("What have you accomplished today?")
if achievement:
    st.success(f"Congratulations on your achievement: {achievement} 🎉")
else:
    st.info("Share your achievements to celebrate your growth! 🌟")

st.markdown("---")
#footer
st.write("----")
st.write("Keep up the great work! 🌟")
st.write("**Created with ❤️ by Amber Parmaar**")
st.write("Find me on [LinkedIn](https://www.linkedin.com/in/amber-shoukat-19724a293/)")



