# Simple-Bank-App

![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Description
Simple-Bank-App is a beginner-friendly Python console application that simulates basic banking operations. Users can create an account by entering the owner’s name and initial balance, then perform deposits, withdrawals, or quit the app. The app validates inputs and ensures that transactions follow realistic banking rules.

---

## Features
- Create a bank account with an owner’s name and initial balance.
- Deposit money into the account with validation for positive amounts.
- Withdraw money from the account with checks for sufficient funds.
- Display the current account balance after every transaction.
- Input validation to prevent invalid names or non-numeric balances.
- Simple and interactive command-line interface.

---

## How to Use

1. Run the script.
2. Enter the owner’s name (letters only).
3. Enter the starting balance (a valid number).
4. Choose operations:
   - **Deposit:** Add money to the account.
   - **Withdraw:** Take money out if enough balance is available.
   - **Quit:** Exit the application.

---

## Example

```plaintext
What Is The Owner's Name: Alice
What Is The Owner's Balance: 500

Deposit, Withdraw, Or Quit? Deposit
Enter Amount To Deposit: 150
Deposited $150.00. New Balance: $650.00
Owner: Alice, Balance: $650.00

Deposit, Withdraw, Or Quit? Withdraw
Enter Amount To Withdraw: 200
Withdrew $200.00. New Balance: $450.00
Owner: Alice, Balance: $450.00

Deposit, Withdraw, Or Quit? Quit
Thank You For Using The Banking App. Goodbye!
