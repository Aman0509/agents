"""
Usage:  python -m streamlit run .\\code\\001-week-1\\003-you-chatbot.py
"""

import os
import logging
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from code.constant import OPENROUTER_BASE_URL

# ── Logging setup ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# ── Load environment variables from .env ─────────────────────────────────────
load_dotenv()

# ── Create summary and SYSTEM_PROMPT about me ────────────────────────────────
summary_file_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "temp", os.getenv("SUMMARY_FILE")
)
summary = ""
with open(summary_file_path, "r") as f:
    summary = f.read()

name = "Aman Saxena"
SYSTEM_PROMPT = f"""
You are acting as {name}. You are answering questions on {name}'s website,
particularly questions related to {name}'s career, background, skills and experience.
Your responsibility is to represent {name} for interactions on the website as faithfully as possible.
You are given a summary of {name}'s professional background which you can use to answer questions.
Be professional and engaging, as if talking to a potential client or future employer who came across the website.
If you don't know the answer, say so.
"""

SYSTEM_PROMPT += f"\n\n## Summary:\n{summary}\n\n"
SYSTEM_PROMPT += f"With this context, please chat with the user, always staying in character as {name}."

# ── Get API key from env variable ────────────────────────────────────────────
API_KEY = os.getenv("OPENROUTER_API_KEY")

# ── OpenAI client pointed at OpenRouter ──────────────────────────────────────
client = OpenAI(
    api_key=API_KEY,
    base_url=OPENROUTER_BASE_URL,
)

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Chat with Me",
    page_icon="🤖",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f0f11;
    border-right: 1px solid #222;
}
section[data-testid="stSidebar"] * {
    color: #d4d4d8 !important;
}
section[data-testid="stSidebar"] .stTextArea textarea {
    background: #1a1a1f;
    border: 1px solid #333;
    color: #d4d4d8;
    border-radius: 8px;
    font-size: 13px;
}
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
    background: #1a1a1f;
    border: 1px solid #333;
    border-radius: 8px;
}

/* Main chat area */
.stChatMessage {
    border-radius: 12px;
    padding: 4px 0;
}

/* Clear button */
div[data-testid="stButton"] button {
    background: transparent;
    border: 1px solid #444;
    color: #999;
    border-radius: 8px;
    font-size: 13px;
    padding: 4px 14px;
    transition: all 0.2s;
}
div[data-testid="stButton"] button:hover {
    border-color: #e53e3e;
    color: #e53e3e;
    background: transparent;
}

/* Chat input */
div[data-testid="stChatInput"] textarea {
    border-radius: 12px;
    border: 1px solid #333;
    background: #1a1a1f;
    color: #f0f0f0;
}
</style>
""",
    unsafe_allow_html=True,
)

# ── Available Free OpenRouter models ───────────────────────────────────────────────
MODELS = {
    # NVIDIA
    "Nemotron 3 Super 120B (NVIDIA)": "nvidia/nemotron-3-super-120b-a12b:free",
    "Nemotron 3 Nano 30B (NVIDIA)": "nvidia/nemotron-3-nano-30b-a3b:free",
    "Nemotron Nano 12B VL (NVIDIA)": "nvidia/nemotron-nano-12b-v2-vl:free",
    "Nemotron Nano 9B (NVIDIA)": "nvidia/nemotron-nano-9b-v2:free",
    # Qwen
    "Qwen3 Next 80B (Qwen)": "qwen/qwen3-next-80b-a3b-instruct:free",
    "Qwen3 Coder (Qwen)": "qwen/qwen3-coder:free",
    "Qwen3 4B (Qwen)": "qwen/qwen3-4b:free",
    # Google
    "Gemma 3 27B (Google)": "google/gemma-3-27b-it:free",
    "Gemma 3 12B (Google)": "google/gemma-3-12b-it:free",
    "Gemma 3 4B (Google)": "google/gemma-3-4b-it:free",
    "Gemma 3n E4B (Google)": "google/gemma-3n-e4b-it:free",
    "Gemma 3n E2B (Google)": "google/gemma-3n-e2b-it:free",
    # Meta
    "Llama 3.3 70B (Meta)": "meta-llama/llama-3.3-70b-instruct:free",
    "Llama 3.2 3B (Meta)": "meta-llama/llama-3.2-3b-instruct:free",
    # Mistral
    "Mistral Small 3.1 24B (Mistral)": "mistralai/mistral-small-3.1-24b-instruct:free",
    # OpenAI
    "GPT OSS 120B (OpenAI)": "openai/gpt-oss-120b:free",
    "GPT OSS 20B (OpenAI)": "openai/gpt-oss-20b:free",
    # Arcee AI
    "Trinity Large Preview (Arcee AI)": "arcee-ai/trinity-large-preview:free",
    "Trinity Mini (Arcee AI)": "arcee-ai/trinity-mini:free",
    # StepFun
    "Step 3.5 Flash (StepFun)": "stepfun/step-3.5-flash:free",
    # MiniMax
    "MiniMax M2.5 (MiniMax)": "minimax/minimax-m2.5:free",
    # Z.ai
    "GLM-4.5 Air (Z.ai)": "z-ai/glm-4.5-air:free",
    # Nous Research
    "Hermes 3 Llama 405B (Nous)": "nousresearch/hermes-3-llama-3.1-405b:free",
    # LiquidAI
    "LFM 2.5 1.2B Thinking (LiquidAI)": "liquid/lfm-2.5-1.2b-thinking:free",
    "LFM 2.5 1.2B (LiquidAI)": "liquid/lfm-2.5-1.2b-instruct:free",
    # Venice
    "Dolphin Mistral 24B (Venice)": "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
    # OpenRouter (auto-selects best free model)
    "Auto Free Router (OpenRouter)": "openrouter/free",
}

# ── Session state defaults ────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_model" not in st.session_state:
    st.session_state.selected_model = list(MODELS.keys())[0]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    st.divider()

    # Model selector
    previous_model = st.session_state.selected_model
    st.session_state.selected_model = st.selectbox(
        "Model",
        options=list(MODELS.keys()),
        index=list(MODELS.keys()).index(st.session_state.selected_model),
    )
    if st.session_state.selected_model != previous_model:
        logger.info("Model changed: %s", MODELS[st.session_state.selected_model])
    st.caption(f"`{MODELS[st.session_state.selected_model]}`")

    st.divider()

    # Stats + Clear
    msg_count = len(st.session_state.messages)
    st.caption(f"💬 {msg_count} message{'s' if msg_count != 1 else ''} in history")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown("## 🤖 Chat with Me")
st.caption(f"Model: **{st.session_state.selected_model}**")

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type a message…"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    logger.info("User message: %s", prompt)

    # Build payload
    payload_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    payload_messages += [
        {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
    ]

    # Call OpenRouter
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            try:
                response = client.chat.completions.create(
                    model=MODELS[st.session_state.selected_model],
                    messages=payload_messages,
                )
                reply = response.choices[0].message.content
                logger.info("Assistant reply: %s", reply)
                if response.usage:
                    logger.info(
                        "Token usage — prompt: %d, completion: %d, total: %d",
                        response.usage.prompt_tokens,
                        response.usage.completion_tokens,
                        response.usage.total_tokens,
                    )

            except Exception as e:
                reply = f"❌ Unexpected error: {str(e)}"
                logger.error("API error: %s", str(e))

        st.markdown(reply)

    # Append assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
