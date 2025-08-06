
from flask import Flask, session, render_template, request, redirect, make_response
import os
import secrets

app = Flask(__name__)
app.secret_key = os.urandom(24)  

@app.after_request
def set_security_headers(resp):
    resp.headers['X-Frame-Options'] = 'DENY'  # Mitigate Clickjacking
    resp.headers['Content-Security-Policy'] = "frame-ancestors 'none';"
    return resp

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        submitted_token = request.form.get('csrf_token', '')
        session_token = session.get('csrf_token', '')
        if not submitted_token or session_token != submitted_token:
            return 'CSRF attempt detected!', 403
        # Simulate safe update
        return 'Form submitted successfully!'

    # For GET request, generate CSRF token
    csrf_token = secrets.token_hex(16)
    session['csrf_token'] = csrf_token
    return render_template('form.html', csrf_token=csrf_token)

if __name__ == '__main__':
    app.run(debug=True)
