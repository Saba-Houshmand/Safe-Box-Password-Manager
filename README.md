# 🔐 Safe Box Password Manager

A secure Command Line Interface (CLI) application for managing and retrieving safebox passwords using SHA-256 hashing and multi-factor identity verification.

---

## 📺 Video Demo
**Watch the project in action here:** [https://youtu.be/rZp_p7yc_Ec](https://youtu.be/rZp_p7yc_Ec)

---

## 🚀 Features

* **Cryptographic Security:** Passwords are never stored as plain text; they are protected using **SHA-256 hashing**.
* **Identity Verification:** Users must verify their Email, Full Name, Birth Date, and Father's Name to access records.
* **Anti-Bot Protection:** Includes a "Human Test" (Math CAPTCHA) to ensure physical user interaction.
* **Format Validation:** * Strict email validation via `validator-collection`.
    * Date validation (ISO 8601 format).
    * Regex-based password enforcement (4-digit PINs).
* **Automated Data Management:** Creates and manages user-specific CSV files for persistent storage.

---

## 🛠 Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
    cd REPO_NAME
    ```

2.  **Install Required Libraries:**
    ```bash
    pip install validator-collection
    ```

---

## 📋 How It Works

### Saving Data (S)
The program prompts for your personal information and the number of safeboxes you own. Each 4-digit PIN you enter is instantly hashed before being written to a local CSV file, ensuring your real passwords never touch the disk.

### Viewing Data (V)
To retrieve a password, the system performs a strict identity check. Once verified, it uses a secure lookup method to identify your 4-digit PIN from the stored hash and displays it to you.

---

## 🛡 Security Note
This project is designed with a "Zero Plain-Text" policy. By hashing passwords with SHA-256, even if the storage file is compromised, your original PINs remain protected against direct exposure.

---

## 👤 Author
**Your Name** [Your GitHub Profile](https://github.com/YOUR_USERNAME)
