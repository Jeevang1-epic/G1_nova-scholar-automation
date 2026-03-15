import sys
import asyncio
import os
import re
import streamlit as st
from nova_scholar_core import scrape_arxiv, analyze_with_nova

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, "icons", "logo.png")
SETTINGS_ICON = os.path.join(BASE_DIR, "icons", "settings.png")
ERROR_ICON = os.path.join(BASE_DIR, "icons", "error.png")

if os.path.exists(ICON_PATH):
    st.set_page_config(page_title="Nova-Scholar", page_icon=ICON_PATH, layout="centered")
else:
    st.set_page_config(page_title="Nova-Scholar", layout="centered")

with st.sidebar:
    col_s1, col_s2 = st.columns([1, 5])
    with col_s1:
        if os.path.exists(SETTINGS_ICON):
            st.image(SETTINGS_ICON, width=28)
    with col_s2:
        st.markdown("### Configuration")
        
    st.markdown("To use this public app, please enter your own AWS API Key.")
    user_api_key = st.text_input("AWS Bedrock Key (ABSK...)", type="password")
    st.markdown("[Get your key here](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/apikeys)")

st.markdown("""
    <style>
    .main {background-color: #0E1117;}
    h1 {color: #00A8E8; font-family: 'Helvetica Neue', sans-serif;}
    .stButton>button {
        border-radius: 8px; 
        border: 1px solid #00A8E8; 
        color: #00A8E8;
        background-color: transparent;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00A8E8; 
        color: white;
        border: 1px solid #00A8E8;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 5])
with col1:
    if os.path.exists(ICON_PATH):
        st.image(ICON_PATH, width=80)
    else:
        st.markdown("<div style='height: 80px; width: 80px; background-color: #333; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px; text-align: center;'>Missing<br>logo.png</div>", unsafe_allow_html=True)

with col2:
    st.title("Nova-Scholar")
    st.markdown("<p style='color: #888; font-size: 18px;'>Agentic Web Research & Automation Assistant</p>", unsafe_allow_html=True)

st.markdown("---")

query = st.text_input("Enter your complex research topic:", placeholder="e.g., Multi-agent reinforcement learning")

if st.button("Deploy Autonomous Agent"):
    if not user_api_key:
        err_col1, err_col2 = st.columns([1, 20])
        with err_col1:
            if os.path.exists(ERROR_ICON):
                st.image(ERROR_ICON, width=24)
        with err_col2:
            st.markdown("<p style='color: #ff4b4b; font-weight: bold;'>API Key required. Check the sidebar!</p>", unsafe_allow_html=True)
            
        with st.sidebar:
            s_err_col1, s_err_col2 = st.columns([1, 6])
            with s_err_col1:
                if os.path.exists(ERROR_ICON):
                    st.image(ERROR_ICON, width=24)
            with s_err_col2:
                st.markdown("<p style='color: #ff4b4b; font-weight: bold;'>Please enter your AWS Bedrock API key above to run the agent.</p>", unsafe_allow_html=True)
    
    elif query:
        match = re.search(r'(ABSK[\w\-]+)', user_api_key)
        if match:
            clean_key = match.group(1)
        else:
            clean_key = user_api_key.strip().replace('"', '').replace("'", "")
            
        os.environ["AWS_BEARER_TOKEN_BEDROCK"] = clean_key
        
        with st.spinner(f"Agent navigating ArXiv UI for '{query}'... Watch your screen!"):
            papers = scrape_arxiv(query)
        
        if papers:
            st.success("UI Automation complete! Data extracted.")
            
            st.markdown("### Scraped Research Papers:")
            for p in papers:
                st.markdown(f"- **{p}**")
            
            with st.spinner("Amazon Nova 2 Lite synthesizing data..."):
                analysis = analyze_with_nova(papers, query)
            
            st.markdown("### Agentic Summary:")
            st.info(analysis)
        else:
            err_col1, err_col2 = st.columns([1, 20])
            with err_col1:
                if os.path.exists(ERROR_ICON):
                    st.image(ERROR_ICON, width=24)
            with err_col2:
                st.markdown("<p style='color: #ff4b4b; font-weight: bold;'>Automation failed to find papers. Try a broader topic.</p>", unsafe_allow_html=True)
    else:
        err_col1, err_col2 = st.columns([1, 20])
        with err_col1:
            if os.path.exists(ERROR_ICON):
                st.image(ERROR_ICON, width=24)
        with err_col2:
            st.markdown("<p style='color: #ff4b4b; font-weight: bold;'>Please enter a topic first.</p>", unsafe_allow_html=True)
