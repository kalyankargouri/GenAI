import streamlit as st

with st.form(key="reg_form"):
    st.header("registration form")
    first_name=st.text_input(key="fname",label="first name")
    last_name=st.text_input(key="lname",label="last name")
    age=st.slider("age",10,100,25,1)
    addr=st.text_area("address")
    submit_btn=st.form_submit_button("submit",type="primary")

if submit_btn:
    err_message=""
    is_error=False
    if not first_name:
        is_error=True
        err_message+="first name cannot be empty.\n"
    if not last_name:
        is_error = True
        err_message += "Last name cannot be empty.\n"
    if not addr:
        is_error = True
        err_message += "Address cannot be empty.\n"
    # if any error, display the error
    if is_error:
        st.error(err_message)
    else:
        message = f"Successfully registered: {st.session_state['fname']} {st.session_state['lname']}.\nAge: {age}. Living at {addr}"
        st.success(message)