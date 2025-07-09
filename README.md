# 🔐 MPIN Strength Checker

A smart tool to analyze the strength of 4-digit and 6-digit MPINs used in mobile banking.  
This tool detects whether an MPIN is **commonly used** or **derived from user demographics** such as:

- Date of Birth (DOB)
- Spouse's DOB
- Wedding Anniversary
  
  ![image](https://github.com/user-attachments/assets/81a59e8f-ccf9-4f2e-8da2-a09f1e87c993)
  
  ## 🌐 Live Demo

Click below to try the MPIN Strength Checker (no setup required):
To simplify usage and improve evaluation, I have deployed the MPIN Strength Checker as a web application using Streamlit Cloud 
Please have a look .....
👉 https://mpin-strength-checker-j8devgw4hu4krad6nyverz.streamlit.app/

> ✅ Enter MPIN and optional DOBs/Anniversary  
> ✅ Get real-time feedback on strength & reasons  
> ✅ View 20+ test cases in a friendly UI

Developed as a part of a Data Science technical assessment for **OneBanc**.
## 🖼️ App Preview

### 🔹 Input Section
![image](https://github.com/user-attachments/assets/81a59e8f-ccf9-4f2e-8da2-a09f1e87c993)

### Output (In case of strong MPIN Password)
![image](https://github.com/user-attachments/assets/509f9d3e-0262-4b15-acb1-d175e07ea75d)

### Output (In case of weak MPIN Password)
![image](https://github.com/user-attachments/assets/a4646add-6748-4f89-862b-ff22000204b4)

### 🧪 Test Case Coverage
The app includes a wide variety of 20+ test cases:
Covers all edge cases: common pins, birthday patterns, mixed formats
Clearly shows Expected vs Actual
Visually displays:
🔢 Input MPIN
🎂 Demographic values
✅/❌ Test result
Reason(s) if weak

### 🔹 Test Case Results ( Some of the Screenshots .....)
![image](https://github.com/user-attachments/assets/44d9cd62-4eee-4f8c-8901-5a5f0beab407)
![image](https://github.com/user-attachments/assets/525a6d21-ad49-4a38-89b3-0f875dcb1476)
![image](https://github.com/user-attachments/assets/7eee9c78-deb8-4790-b6eb-6de8bd801ab9)
![image](https://github.com/user-attachments/assets/f874dcc2-a3f4-4484-8e07-08895475deae)
![image](https://github.com/user-attachments/assets/7b4c852d-4b3a-4228-991a-fe1ee471d13b)
![image](https://github.com/user-attachments/assets/79dc69e7-905b-4b8b-a9e9-df84a555b631)
![image](https://github.com/user-attachments/assets/29d0b55a-b735-496e-a844-9ce4c4ab7d90)
![image](https://github.com/user-attachments/assets/fe0876be-4241-43b3-a929-f49b4c0abde4)

## 🚀 Features

- ✅ Supports **4-digit** and **6-digit** MPINs
- ✅ Detects weak MPINs from:
  - Repeating/sequential patterns (e.g., `0000`, `1234`, `654321`)
  - Demographic data (`0201` from `02-01-1998`)
- ✅ Classifies MPIN as **WEAK** or **STRONG**
- ✅ Gives clear **reason labels** if MPIN is weak:
  - `COMMONLY_USED`
  - `DEMOGRAPHIC_DOB_SELF`
  - `DEMOGRAPHIC_DOB_SPOUSE`
  - `DEMOGRAPHIC_ANNIVERSARY`
- ✅ Includes 20+ test cases
- ✅ Clean and intuitive **Streamlit UI**

## 📁 Folder Structure
MPIN-Strength-Checker/
│
├── mpin_app.py # 🔘 Streamlit frontend
├── mpin_logic.py # 🧠 Core logic
├── test_cases.py # 🧪 20+ test cases
├── requirements.txt # 📦 Python dependencies
├── screenshots/ # 📸 App UI images
└── README.md # 📘 Project documentation




