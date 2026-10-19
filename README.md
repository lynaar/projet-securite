# 🛡️ Web Security Lab

**Academic Project — Web Security, Phishing Simulation and SQL Injection Analysis**

Web Security Lab is an academic cybersecurity project designed to explore common web application vulnerabilities, understand social engineering techniques, and study security best practices in a controlled educational environment.

The repository brings together practical exercises related to phishing simulation and SQL injection, with the goal of understanding potential attack mechanisms and learning how to prevent them.

> **Disclaimer:** This project is intended exclusively for educational purposes and authorized security testing. Any simulation must be conducted in a controlled environment, with appropriate authorization and without collecting real credentials or sensitive personal information.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Project Modules](#-project-modules)
- [Technologies](#-technologies)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Security and Ethical Considerations](#-security-and-ethical-considerations)
- [Future Improvements](#-future-improvements)
- [Academic Context](#-academic-context)

---

## 🌍 Project Overview

Web applications may be exposed to different security risks, including social engineering and injection vulnerabilities.

This project explores these issues through practical exercises:

- Simulating phishing scenarios to understand how fraudulent messages and deceptive interfaces can influence users.
- Studying SQL injection concepts to understand how insecure database queries may compromise application security.
- Exploring server-side validation, secure input handling, and defensive programming.
- Identifying best practices for building safer web applications.

The project emphasizes understanding vulnerabilities and applying appropriate defensive measures.

## 🎯 Objectives

- Understand the principles of social engineering and phishing.
- Explore common web application vulnerabilities.
- Develop a Python web application using Flask.
- Understand HTTP routes, form handling, and server-side validation.
- Study the risks associated with unsafe database queries.
- Explore secure coding practices and input validation.
- Promote cybersecurity awareness and responsible testing.

## 🧪 Project Modules

### 1. Phishing Simulation

**Objective:** Study phishing techniques and user awareness in a controlled academic environment.

The module explores the technical mechanisms that may be used in a phishing scenario.

Key components include:

- A web application built with Flask.
- HTML and CSS interfaces for educational simulation.
- JavaScript for client-side interactions.
- Form processing and server-side input validation.
- Email functionality using SMTP and Python's `smtplib`.
- Dynamic links for controlled testing scenarios.
- JSON-based storage and timestamped event logging.

The module aims to demonstrate why users should verify links, inspect email senders, and avoid submitting sensitive information to untrusted websites.

### 2. SQL Injection

**Objective:** Understand SQL injection vulnerabilities and learn how to prevent them.

SQL injection can occur when untrusted user input is incorporated into database queries without appropriate safeguards.

This module provides a basis for studying:

- The principles of SQL injection.
- The relationship between user input and database queries.
- The risks of insecure query construction.
- Input validation and secure data handling.
- Parameterized queries and other defensive techniques.

The focus is on understanding the vulnerability and applying secure development practices in an authorized test environment.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Application logic and scripting |
| Flask | Web application backend |
| HTML5 | Web page structure |
| CSS3 | Interface styling |
| JavaScript | Client-side interactions |
| SMTP / `smtplib` | Email functionality for controlled simulations |
| JSON | Data storage for the simulation |
| Ngrok | Temporary access to a local application during authorized testing |
| SQL | Database concepts and injection analysis |

## 📁 Repository Structure

```text
web-security-lab/
│
├── README.md
│
├── projet phising/
│   └── Phishing simulation files
│
└── sql injection/
    └── SQL injection study files
```

The structure above reflects the two module folders currently visible in the repository. The files inside each folder may vary according to the implementation.

## 🚀 Getting Started

### Prerequisites

- Python 3
- pip
- A code editor such as Visual Studio Code
- A modern web browser

### 1. Clone the repository

```bash
git clone https://github.com/lynaar/web-security-lab.git
cd web-security-lab
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

If a `requirements.txt` file is available in the relevant module, install its dependencies:

```bash
pip install -r requirements.txt
```

Otherwise, consult the Python imports and setup instructions in the module before installing its dependencies.

### 4. Run the application

Navigate to the phishing module and identify its Flask entry-point file. If the application uses `app.py`, for example, it may be launched with:

```bash
python app.py
```

The exact command depends on the application's entry-point filename and configuration.

Use only test data and a controlled environment. Do not expose an application publicly without reviewing its security settings.

## 🔐 Security and Ethical Considerations

Cybersecurity experiments must be conducted responsibly.

- Obtain authorization before testing systems or sending simulation emails.
- Use test accounts and synthetic data.
- Never collect, store, or transmit real passwords or other sensitive credentials.
- Avoid impersonating real organizations or targeting unsuspecting individuals.
- Protect SMTP credentials and other secrets using environment variables rather than committing them to GitHub.
- Avoid exposing debug mode or sensitive application routes to the public internet.
- Use parameterized SQL queries and appropriate server-side validation when developing secure applications.

The purpose of this project is cybersecurity education, vulnerability awareness, and prevention.

## 🚀 Future Improvements

Potential improvements include:

- Adding a detailed technical report for each module.
- Documenting the application architecture and request flow.
- Adding defensive examples for SQL injection prevention.
- Improving error handling and server-side validation.
- Adding automated tests for input validation.
- Documenting the limitations and security controls of each simulation.
- Adding screenshots of the local application using synthetic test data.
- Providing a setup guide specific to each module.

## 🎓 Academic Context

**Project type:** Academic cybersecurity project  
**Year:** 2026  
**Focus:** Web application security, phishing awareness, and SQL injection analysis

This project provides practical exposure to web application development and cybersecurity concepts, with an emphasis on understanding common vulnerabilities and improving defensive practices.

---

<p align="center">
  <i>Learn how vulnerabilities work. Build safer applications.</i>
</p>
