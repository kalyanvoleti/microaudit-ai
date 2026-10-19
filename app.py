import streamlit as st

st.set_page_config(page_title="MicroAudit AI — Freelance Contract Checker", page_icon="⚖️")

st.title("⚖️ MicroAudit AI")
st.caption("A local-first contract risk analyzer for freelancers and small businesses.")

st.markdown("""
Upload or paste raw agreement clauses to audit potential financial and legal risks before signing. 
All analysis runs locally on your device to keep sensitive client terms confidential.
""")

# Input section
contract_text = st.text_area("Paste Agreement Terms / Contract Clauses Here:", height=220)

# Risk detection rule sets
RISK_PATTERNS = {
    "Unlimited Revisions": ["unlimited revisions", "until satisfied", "endless changes"],
    "Delayed Payment Terms": ["net 60", "net 90", "payment upon client receipt"],
    "IP Ownership Before Payment": ["transfers upon creation", "works made for hire immediately"],
    "Broad Indemnification": ["indemnify and hold harmless", "unlimited liability"]
}

if st.button("Audit Contract Risks"):
    if not contract_text.strip():
        st.warning("Please paste contract text to analyze.")
    else:
        st.subheader("📊 Clause Audit Results")
        
        detected_risks = []
        text_lower = contract_text.lower()
        
        for risk, keywords in RISK_PATTERNS.items():
            for kw in keywords:
                if kw in text_lower:
                    detected_risks.append((risk, kw))
                    break
        
        if detected_risks:
            st.error(f"Found {len(detected_risks)} Potential Risk Area(s):")
            for risk_title, match in detected_risks:
                st.write(f"⚠️ **{risk_title}**: Triggered by keyword *'{match}'*")
                if risk_title == "Unlimited Revisions":
                    st.info("💡 **Recommendation:** Cap revisions to 2 or 3 rounds in your scope of work.")
                elif risk_title == "Delayed Payment Terms":
                    st.info("💡 **Recommendation:** Request Net-15 or Net-30 terms with late fee penalties.")
                elif risk_title == "IP Ownership Before Payment":
                    st.info("💡 **Recommendation:** Specify that IP transfers *only after full payment*.")
                elif risk_title == "Broad Indemnification":
                    st.info("💡 **Recommendation:** Cap your liability to the total value of the invoice.")
        else:
            st.success("✅ No standard high-risk clauses detected. (Always review manually as well!)")

st.divider()
st.caption("🔒 Privacy Note: No contract data is transmitted over the network.")