# Password Strength Checker

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)

---

## Overview

This is a simple Python project that checks the strength of a user's password based on predefined criteria. It ensures the password meets minimum security standards and provides feedback on its strength — Weak, Fair, or Strong — based on its length. If the password is weak, the program suggests a stronger password.

---

## Features

- Validates password against these rules:
  - At least 2 uppercase letters
  - At least 2 lowercase letters
  - At least 2 digits
  - At least 1 special character (e.g., !@#$%^&*)
  - Minimum length of 8 characters
- Calculates password strength (Weak, Fair, Strong) based on length
- Suggests a stronger password if requirements are not met or strength is weak
- User-friendly interaction with clear feedback messages

---

## How to Use

1. Run the Python script.
2. Enter a password when prompted.
3. The program will check the password against the criteria.
4. It will print the password strength.
5. If the password is weak, a suggested stronger password will be displayed.
6. Repeat until you enter a valid and strong password.

---

## Example Output

```plaintext
Your password must meet the following requirements:

At least 2 uppercase letters

At least 2 lowercase letters

At least 2 digits

At least 1 special character (e.g., !@#$%^&*)

Minimum length of 8 characters

Enter your password: Pass123! Password is missing some requirements. Please try again.

At least 2 uppercase letters

At least 2 digits

Password Strength: Weak 
Suggested Stronger Password: Ab7&Fg9#QpX

