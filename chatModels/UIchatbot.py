# import streamlit as st
# import os
# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# load_dotenv()

# model = ChatMistralAI(
#     model="mistral-small-2603",
#     api_key=os.getenv("MISTRAL_API_KEY"),
#     temperature=0.9,
# )

# st.title("🤖 Sad AI Agent")

# # Initialize chat history in session state, same roles/structure as original script
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         SystemMessage("you are a Sad AI agent")
#     ]

# # Display existing conversation (skip the SystemMessage)
# for msg in st.session_state.messages:
#     if isinstance(msg, HumanMessage):
#         with st.chat_message("user"):
#             st.write(msg.content)
#     elif isinstance(msg, AIMessage):
#         with st.chat_message("assistant"):
#             st.write(msg.content)

# # Chat input
# prompt = st.chat_input("You:")

# if prompt:
#     st.session_state.messages.append(HumanMessage(content=prompt))
#     with st.chat_message("user"):
#         st.write(prompt)

#     response = model.invoke(st.session_state.messages)
#     st.session_state.messages.append(AIMessage(content=response.content))

#     with st.chat_message("assistant"):
#         st.write(response.content)

# --------ab ismei niche wale chatbot mei tumhare pass system beviour choose krne ka option bhi available hoga---------------

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",
    api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.9,
)

st.title("🤖 AI Agent")

# Mode selection (same 3 modes as original script)
if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False

if not st.session_state.mode_selected:
    st.write("Choose your AI mode")
    choice = st.radio(
        "tell your response:-",
        options=[1, 2, 3],
        format_func=lambda x: {1: "Angry mode", 2: "Funny mode", 3: "Sad mode"}[x]
    )

    if st.button("Start"):
        if choice == 1:
            mode = "You are an Angry AI agent. You respond aggressively and impatiently."
        elif choice == 2:
            mode = "You are a very Funny AI agent. You responnd with humor and jokes."
        elif choice == 3:
            mode = "You are a very Sad AI agent. You responnd with sadness"

        st.session_state.messages = [
            SystemMessage(content=mode)
        ]
        st.session_state.mode_selected = True
        st.rerun()

else:
    # Display existing conversation (skip the SystemMessage)
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    prompt = st.chat_input("You:")

    if prompt:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)

        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

        with st.chat_message("assistant"):
            st.write(response.content)