# ClickJacking
This project demonstrates how to build a simple yet secure web application that protects against two common web vulnerabilities: Clickjacking and Cross-Site Request Forgery (CSRF).

# Key Features
## Clickjacking Protection:
Prevents the web page from being embedded into iframes on other sites using HTTP headers (X-Frame-Options: DENY and Content-Security-Policy: frame-ancestors 'none';). This stops attackers from tricking users into interacting with hidden or disguised UI elements.

# CSRF Token Protection:
Implements a synchronizer token pattern by generating a unique CSRF token for each session. The token is embedded in the form and validated on submission to ensure that requests originate from authorized users and not from malicious third parties.

# How It Works
When a user visits the form page, the server generates a unique CSRF token stored in the user's session and embedded as a hidden field in the form.
The user enters data and submits the form along with the CSRF token.
On receiving the form, the server compares the submitted token against the one stored in the session.
If tokens match, the submission is accepted and processed.
If tokens do not match or are missing, the submission is blocked, indicating a potential CSRF attack.
The server also sets appropriate HTTP headers to disallow framing, protecting against clickjacking.

# User Experience
Users interact with a clean, interactive form to input data safely. If all security checks pass, users receive a confirmation message indicating successful submission. Any malicious attempts to exploit clickjacking or CSRF vulnerabilities result in the request being blocked.

# Technology Stack
### Backend: Python with Flask framework
### Frontend: HTML with optional JavaScript and CSS for interactivity and styling

#### The form is used to securely collect user input while enforcing robust defenses against clickjacking and CSRF attacks, ensuring data integrity and protecting users from unauthorized actions.
#### It serves as a practical demonstration of implementing critical web security measures—embedding a CSRF token for request validation and setting HTTP headers to prevent framing—thereby safeguarding both users and the application

