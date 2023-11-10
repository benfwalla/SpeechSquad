import streamlit as st
import pandas as pd

if 'trial_data' not in st.session_state:
    st.session_state.trial_data = pd.DataFrame(columns=['Trial', 'Student Name', 'Objective', 'Score'])

if 'trial_counter' not in st.session_state:
    st.session_state.trial_counter = 1

if 'percentage' not in st.session_state:
    st.session_state.percentage = 0

st.set_page_config(
    page_title="Speech Squad",
    page_icon=":speech_balloon:",
)

# Function to log the trial data
def log_trial(trial_number, student_name, objective, score):
    new_row = {'Trial': trial_number, 'Student Name': student_name, 'Objective': objective, 'Score': score}
    st.session_state.trial_data = pd.concat([st.session_state.trial_data, pd.DataFrame(new_row, index=[0])],
                                            ignore_index=True)

    st.session_state.trial_counter += 1


# Function to calculate and display percentage
def calculate_percentage():
    if not st.session_state.trial_data.empty:
        # Convert scores to numeric and calculate percentage
        numeric_scores = pd.to_numeric(st.session_state.trial_data['Score'], errors='coerce')
        percentage = (numeric_scores.sum() / len(numeric_scores)) * 100
        st.session_state.percentage = percentage
    else:
        st.session_state.percentage = 0

    # Update the display for percentage
    st.markdown(f"#### Percentage: {st.session_state.percentage:.2f}%")


# Function to display the app interface
def show_app():
    st.title("Speech Squad 💬💪")

    st.divider()

    # Add text input fields for student name and objective
    student_name = st.text_input("Enter Student Name")
    objective = st.text_input("Enter Objective")

    # Initialize and display the trial counter
    trial_counter = st.empty()  # Placeholder for the trial counter

    # create a container to hold the buttons
    buttons_container = st.container()

    # add buttons with different button_clicked values
    with buttons_container:
        col1, col2, col3 = st.columns(3)
        if col1.button("Full - 1"):
            log_trial(st.session_state.trial_counter, student_name, objective, "1")
        if col2.button("Half - ½"):
            log_trial(st.session_state.trial_counter, student_name, objective, ".5")
        if col3.button("None - 0"):
            log_trial(st.session_state.trial_counter, student_name, objective, "0")

    # Display the updated trial counter
    trial_counter.markdown(f"<h2 style='text-align: center'>Trial #{st.session_state.trial_counter}</h2>",
                           unsafe_allow_html=True)

    st.divider()

    # Display the trial data table and bind the calculate_percentage function to run on changes
    st.subheader("Trial Data")

    calculate_percentage()  # Initial calculation and display

    st.data_editor(st.session_state.trial_data, hide_index=True)

    # Download button for the trial data
    st.download_button("⬇️ Download as CSV", st.session_state.trial_data.to_csv(index=False),
                       file_name=f"{student_name}-{objective}-trial_data.csv")


# Run the app
show_app()
