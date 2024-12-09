import streamlit as st
import time

# Streamlit app setup
st.title("Large Number Timer")

# Timer settings
hours = st.number_input("Hours:", min_value=0, value=0, step=1)
minutes = st.number_input("Minutes:", min_value=0, max_value=59, value=0, step=1)
seconds = st.number_input("Seconds:", min_value=0, max_value=59, value=0, step=1)

total_seconds = int(hours * 3600 + minutes * 60 + seconds)

if st.button("Start Timer"):
    placeholder = st.empty()

    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        hrs, mins = divmod(mins, 60)
        timer_display = f"{hrs:02}:{mins:02}:{secs:02}"

        # Display timer in large font
        placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 72px;'>{timer_display}</h1>",
            unsafe_allow_html=True,
        )

        time.sleep(1)

    placeholder.markdown(
        "<h1 style='text-align: center; font-size: 72px;'>Time's up!</h1>",
        unsafe_allow_html=True,
    )
