import streamlit as st
if 'message' not in st.session_state:
    st.session_state.message=[]

with st.sidebar:
    st.header("settings")
    choices=["upper","lower","toggle"]
    mode=st.selectbox("select mode",choices)
    count= st.slider("message count",min_value=10,value=6,step=2)
    st.subheader("config")
    st.json({"mode":mode,"count":count})

st.title("GOURI Chatbot")
msg=st.chat_input("say something...")
if msg:
    outmsg=msg
    if mode=="upper":
            outmsg = msg.upper()
    elif mode == "Lower":
        outmsg = msg.lower()
    elif mode == "Toggle":
        outmsg = msg.swapcase()

    st.session_state.messages.append(msg)
    st.session_state.messages.append(outmsg)

    msglist = st.session_state.messages
    for idx, message in enumerate(msglist):
        role = "human" if idx % 2 == 0 else "ai"
        with st.chat_message(role):
            st.write(message)