import streamlit as st
from openai import OpenAI

# Configure page
st.set_page_config(
    page_title="CyberChat 3000",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS for gaming theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

.stApp {
    background-color: #000000;
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Cyberpunk_2077_city_view.jpg/1200px-Cyberpunk_2077_city_view.jpg");
    background-size: cover;
    background-blend-mode: overlay;
    color: #00ff00;
    font-family: 'Press Start 2P', cursive;
}

.stTextInput>div>div>input {
    background-color: #111111 !important;
    color: #00ff00 !important;
    border: 2px solid #ff00ff !important;
    border-radius: 5px;
    font-family: 'Press Start 2P', cursive !important;
}

.stChatInput {
    background-color: #00000055 !important;
    backdrop-filter: blur(5px);
}

.stChatMessage {
    border: 2px solid #00ff00;
    border-radius: 10px;
    margin: 10px 0;
    padding: 15px;
    background-color: #000000aa !important;
    backdrop-filter: blur(3px);
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0.7) !important;
}

h1 {
    color: #ff00ff !important;
    text-shadow: 0 0 10px #ff00ff;
    font-size: 2.5rem !important;
    margin-bottom: 30px !important;
}

.stMarkdown {
    color: #00ff00 !important;
}

/* Gaming terminal effect */
.terminal-text {
    animation: blink 1s step-end infinite;
    border-right: 2px solid #00ff00;
}

@keyframes blink {
    0%, 100% {border-color: transparent}
    50% {border-color: #00ff00}
}
</style>
""", unsafe_allow_html=True)

# Show title with gaming theme
st.title("🎮 CYBERCHAT 3000 🕹️")
st.markdown("""
<div style="background: linear-gradient(90deg, #ff00ff 0%, #00ff00 100%); 
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 1.5rem;">
>_ INITIALIZING NEURAL INTERFACE _<
</div>
""", unsafe_allow_html=True)

# API Key Input with gaming style
openai_api_key = st.text_input("🔑 ENTER NEURAL NETWORK ACCESS CODE", type="password")
if not openai_api_key:
    st.markdown("""
    <div class="terminal-text" style="color: #ff0000; padding: 15px; border: 2px solid #ff0000;">
    ⚠️ WARNING: ACCESS CODE REQUIRED FOR SYSTEM INITIALIZATION
    </div>
    """, unsafe_allow_html=True)
else:
    client = OpenAI(api_key=openai_api_key)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # System message with gaming theme
        st.session_state.messages.append({
            "role": "assistant",
            "content": "🖥️ SYSTEM ONLINE\n\n>_ NEURAL NETWORK INITIALIZED\n>_ READY FOR QUERY INPUT\n\n[TYPE YOUR COMMAND]"
        })

    # Display chat messages
    for message in st.session_state.messages:
        role = "user" if message["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(f"""
            <div style="color: { '#00ff00' if role == 'user' else '#ff00ff' };
                        padding: 10px;
                        border-left: 3px solid { '#00ff00' if role == 'user' else '#ff00ff' };
                        margin: 5px 0;">
            {message["content"]}
            </div>
            """, unsafe_allow_html=True)

    # Chat input with gaming style
    if prompt := st.chat_input("🌀 ENTER NEURAL QUERY..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f"""
            <div style="color: #00ff00;
                        padding: 10px;
                        border-left: 3px solid #00ff00;
                        margin: 5px 0;">
            👾 USER: {prompt}
            </div>
            """, unsafe_allow_html=True)

        # Generate AI response
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            
            for chunk in stream:
                full_response += chunk.choices[0].delta.content or ""
                response_placeholder.markdown(f"""
                <div style="color: #ff00ff;
                            padding: 10px;
                            border-left: 3px solid #ff00ff;
                            margin: 5px 0;
                            text-shadow: 0 0 5px #ff00ff55;">
                🤖 SYSTEM: {full_response + " ▌"}
                </div>
                """, unsafe_allow_html=True)
            
            response_placeholder.markdown(f"""
            <div style="color: #ff00ff;
                        padding: 10px;
                        border-left: 3px solid #ff00ff;
                        margin: 5px 0;
                        text-shadow: 0 0 5px #ff00ff55;">
            🤖 SYSTEM: {full_response}
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})