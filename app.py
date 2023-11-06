import streamlit as st
import pandas as pd

if 'trial_data' not in st.session_state:
    st.session_state.trial_data = pd.DataFrame(columns=['Trial', 'Student Name', 'Objective', 'Button Clicked'])

if 'trial_counter' not in st.session_state:
    st.session_state.trial_counter = 1


# Function to log the trial data
def log_trial(trial_number, student_name, objective, button_clicked):
    new_row = {'Trial': trial_number, 'Student Name': student_name, 'Objective': objective, 'Button Clicked': button_clicked}
    st.session_state.trial_data = pd.concat([st.session_state.trial_data, pd.DataFrame(new_row, index=[0])], ignore_index=True)

    st.session_state.trial_counter += 1


# Function to display the app interface
def show_app():
    st.title("Speech Squad 💬💪")

    st.divider()

    # Add text input fields for student name and objective
    student_name = st.text_input("Enter Student Name")
    objective = st.text_input("Enter Objective")

    # Initialize and display the trial counter
    trial_counter = st.empty()  # Placeholder for the trial counter
    trial_counter.title(f"Trial #{st.session_state.trial_counter}")

    # create a container to hold the buttons
    buttons_container = st.container()

    # add buttons with different button_clicked values
    with buttons_container:
        col1, col2, col3 = st.columns(3)
        if col1.button("Button 1"):
            log_trial(st.session_state.trial_counter, student_name, objective, "Button 1")
        if col2.button("Button 2"):
            log_trial(st.session_state.trial_counter, student_name, objective, "Button 2")
        if col3.button("Button 3"):
            log_trial(st.session_state.trial_counter, student_name, objective, "Button 3")

    # Display the updated trial counter
    trial_counter.title(f"Trial #{st.session_state.trial_counter}")

    st.divider()

    # Display the trial data table
    st.subheader("Trial Data")
    st.download_button("⬇️ Download as CSV", st.session_state.trial_data.to_csv(index=False), file_name=f"{student_name}-{objective}-trial_counter.csv")
    st.data_editor(st.session_state.trial_data, num_rows='dynamic')


# Run the app
show_app()
