from test_cases import test_cases
import streamlit as st
from mpin_checker import check_mpin_strength_part_d

st.set_page_config(page_title="MPIN Strength Checker", layout="centered")

st.title("🔐 MPIN Strength Checker")
st.markdown("This tool evaluates the security strength of your MPIN based on common patterns and personal info.")

# --- Inputs ---
mpin = st.text_input("Enter MPIN (4 or 6 digits)", max_chars=6)

col1, col2, col3 = st.columns(3)
with col1:
    dob_self = st.text_input("Your DOB (DD-MM-YYYY)", placeholder="e.g. 02-01-1998")
with col2:
    dob_spouse = st.text_input("Spouse DOB (DD-MM-YYYY)", placeholder="e.g. 01-02-1996")
with col3:
    wedding_date = st.text_input("Wedding Date (DD-MM-YYYY)", placeholder="e.g. 15-08-2020")

# --- Output ---
if st.button("Check MPIN Strength"):
    if not mpin.isdigit() or len(mpin) not in [4, 6]:
        st.error("Please enter a valid 4 or 6-digit MPIN.")
    else:
        strength, reasons = check_mpin_strength_part_d(mpin, dob_self, dob_spouse, wedding_date)
        st.subheader(f"🧠 Strength: {strength}")
        if strength == "WEAK":
            st.warning("⚠️ Your MPIN is weak due to:")
            for reason in reasons:
                st.markdown(f"- `{reason}`")
        else:
            st.success("✅ Your MPIN is strong and not easily guessable.")


with st.expander("🧪 Run 20+ Test Cases with Full Details"):
    st.markdown("Below are the defined test cases with their expected and actual outputs:")

    passed = 0
    for idx, (mpin, dob1, dob2, anniv, expected_strength, expected_reasons) in enumerate(test_cases, 1):
        strength, reasons = check_mpin_strength_part_d(mpin, dob1, dob2, anniv)

        test_passed = strength == expected_strength and set(reasons) == set(expected_reasons)

        with st.container():
            st.markdown(f"### 🔹 Test Case {idx}")
            st.markdown(f"**MPIN:** `{mpin}`")
            st.markdown(f"**DOB (Self):** `{dob1}` &nbsp;&nbsp;&nbsp; **DOB (Spouse):** `{dob2}` &nbsp;&nbsp;&nbsp; **Wedding Date:** `{anniv}`")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Expected Output:**")
                st.code(f"Strength: {expected_strength}\nReasons: {expected_reasons}", language='python')

            with col2:
                st.markdown("**Actual Output:**")
                st.code(f"Strength: {strength}\nReasons: {reasons}", language='python')

            if test_passed:
                st.success("✅ Test Passed")
                passed += 1
            else:
                st.error("❌ Test Failed")

    st.info(f"🏁 Total Passed: **{passed}/{len(test_cases)}**")