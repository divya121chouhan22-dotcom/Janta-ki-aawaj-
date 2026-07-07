import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(page_title="Janata Ki Awaaz", layout="centered")

st.title("🗣️ Janata Ki Awaaz")
st.subheader("AI for Constituency - People's Priorities")
st.write("Apni constituency ki problem likho. AI top priorities nikalega.")

with st.form("problem_form"):
    problem = st.text_area("Apni problem likho:", placeholder="jaise: Hamare yaha pani nahi aata, sadak tooti hai")
    submitted = st.form_submit_button("Submit Problem")

if "problems" not in st.session_state:
    st.session_state.problems = []

if submitted and problem:
    st.session_state.problems.append(problem)
    st.success("Dhanyawad! Aapki problem record ho gayi.")

def get_category(text):
    text = text.lower()
    if "sadak" in text or "road" in text or "gadda" in text:
        return "Sadak"
    elif "pani" in text or "water" in text:
        return "Pani"
    elif "bijli" in text or "light" in text or "power" in text:
        return "Bijli"
    elif "hospital" in text or "doctor" in text or "health" in text:
        return "Health"
    elif "school" in text or "education" in text:
        return "Education"
    else:
        return "Other"

if st.session_state.problems:
    st.divider()
    st.header("📊 Top Priorities")
    
    categories = [get_category(p) for p in st.session_state.problems]
    counts = Counter(categories)
    
    df = pd.DataFrame(counts.items(), columns=["Category", "Votes"])
    df = df.sort_values("Votes", ascending=False)
    
    st.bar_chart(df.set_index("Category"))
    st.dataframe(df)

st.divider()
st.caption("Built for Build with AI Hackathon 2026")
