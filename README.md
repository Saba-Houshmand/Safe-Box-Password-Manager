# 🔐 Safe Box Password Manager
#### 🎥 Video Demo: [Watch on YouTube](https://youtu.be/rZp_p7yc_Ec)

---

## 📖 Overview
**Safe Box Password Manager** is a robust security tool built with **Python**. It allows users to store and retrieve sensitive passwords for their physical safe boxes. Unlike standard managers, it prioritizes privacy by using **SHA-256 Hashing**, ensuring that your actual passwords are never stored in plain text.

This project was developed as the **Final Project for CS50’s Introduction to Programming with Python (CS50P)** from Harvard University.

## ✨ Key Features
* **Hash-Based Security:** Utilizes the SHA-256 cryptographic algorithm for password protection.
* **Multi-Factor Verification:** Access is guarded by personal details including Email, Full Name, Birth Date, and Father's Name.
* **Human Test (Anti-Bot):** Features a randomized mathematical challenge to prevent automated access.
* **Input Validation:** Strict format checking for Emails, ISO Dates, and 4-digit passwords.
* **Local Persistence:** Saves data efficiently in structured CSV files.

## 🛠️ Technical Stack
* **Language:** Python 3
* **Security:** `hashlib` (SHA-256)
* **Validation:** `re` (Regex) & `validator-collection`
* **Data Handling:** `csv` & `os`

---
*Developed by Saba Houshmand*
