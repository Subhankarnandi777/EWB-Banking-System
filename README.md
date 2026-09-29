# 🏦 Banking System

> 🎓 **Developed as part of the EWB Python Internship**

A Python-based **Banking System Mini Project** developed as part of the **Python With AI – Day 9** series.

---

## 🎓 Internship Information

| Detail           | Information                   |
| ---------------- | ----------------------------- |
| **Internship**   | EWB Python Internship         |
| **Project**      | Banking System – Mini Project |
| **Session**      | Python With AI – Day 9        |
| **Technology**   | Python                        |
| **Project Type** | Individual Mini Project       |

This project demonstrates the practical application of fundamental Python programming concepts covered during the EWB Python Internship.

---

## 📌 Project Overview

The Banking System is a menu-driven Python application that simulates basic banking operations.

Users can:

* Create a bank account
* Set a 4-digit PIN
* Login using Account Number and PIN
* Check account balance
* Deposit money
* Withdraw money
* Transfer money between accounts
* View transaction history
* Change their PIN
* Logout

---

## 🛠️ Technologies Used

* Python 3
* `random` module
* `datetime` module

No external libraries are required.

---

## 🧠 Python Concepts Used

* Variables
* Data Types
* Conditional Statements
* `if`, `elif`, `else`
* `while` loops
* `for` loops
* Functions
* Lists
* Dictionaries
* String Operations
* User Input
* Modules

---

## 📁 Project Structure

```text
Banking-System/
│
├── main.py
├── README.md
└── .gitignore
```

---

## 🔄 Application Flow

```text
                 BANKING SYSTEM
                       │
                       ▼
                  MAIN MENU
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Create        Login         Exit
       Account          │
                        ▼
                  ACCOUNT MENU
                        │
       ┌────────┬───────┼────────┬──────────┐
       │        │       │        │          │
       ▼        ▼       ▼        ▼          ▼
    Balance  Deposit Withdraw Transfer  History
                                             │
                                             ▼
                                         Change PIN
                                             │
                                             ▼
                                           Logout
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Open the project

```bash
cd Banking-System
```

### Run the application

```bash
python main.py
```

---

## 💰 Features

### Create Account

Users can create an account by providing:

* Name
* Phone Number
* 4-digit PIN

A unique Account Number is generated using the `random` module.

### Login

Users can log in using:

* Account Number
* PIN

### Check Balance

Displays the user's current account balance.

### Deposit

Allows users to deposit money into their account.

### Withdraw

Allows users to withdraw money after checking their available balance.

### Transfer

Allows users to transfer money between registered accounts.

### Transaction History

Displays deposits, withdrawals, and transfers with date and time.

### Change PIN

Allows users to securely change their existing PIN.

### Logout

Ends the current account session and returns to the main menu.

---

## 📋 Transaction Example

```text
29-09-2026 18:20:11 | Deposit | ₹5000 | Balance: ₹5000

29-09-2026 18:21:32 | Withdrawal | ₹1000 | Balance: ₹4000

29-09-2026 18:23:44 | Transfer to 72193452 | ₹1500 | Balance: ₹2500
```

---

## 🔒 Data Storage

The application uses Python dictionaries and lists to store account and transaction information during program execution.

The current version stores data in memory, so account information is reset when the application is closed.

---

## 📚 Learning Objective

The main objective of this project is to combine fundamental Python concepts into a practical real-world application and understand how variables, conditions, loops, functions, lists, dictionaries, and modules work together.

---

## ⚠️ Disclaimer

This project is developed for **educational purposes** as part of the **EWB Python Internship**.

It is a simplified banking simulation and is not intended for real-world banking or financial use.

---

## 👨‍💻 Author

**Subhankar Nandi**

Computer Science & Engineering
Artificial Intelligence & Machine Learning

**EWB Python Internship**

---

## 🎓 Internship Project

**EWB Python Internship — Banking System Mini Project**

Built using fundamental Python concepts as part of the **Python With AI – Day 9** series.
