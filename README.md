# 🔐 Safe Box Password Manager

A secure Command Line Interface (CLI) application for managing and retrieving safebox passwords using SHA-256 hashing and multi-factor identity verification.


## 🎥 Video Demo
**Watch the project in action here:** [https://youtu.be/rZp_p7yc_Ec](https://youtu.be/rZp_p7yc_Ec)


## ✨ Features

* **Cryptographic Security:** Passwords are never stored as plain text; they are protected using **SHA-256 hashing**.
* **Identity Verification:** Users must verify their Email, Full Name, Birth Date, and Father's Name to access records.
* **Anti-Bot Protection:** Includes a "Human Test" (Math CAPTCHA) to ensure physical user interaction.
* **Format Validation:** * Strict email validation via `validator-collection`.
    * Date validation (ISO 8601 format).
    * Regex-based password enforcement (4-digit PINs).
* **Automated Data Management:** Creates and manages user-specific CSV files for persistent storage.

---
*Developed by Saba Houshmand*
