from flask import Flask, request, jsonify
import hashlib
import time
import random

app = Flask(__name__)
email_status = {} 

def generate_id(to, subject, body):
    return hashlib.sha1(f"{to}{subject}{body}".encode()).hexdigest()

def send_email_mock(provider, to, subject, body):
    # mock success/fail randomly
    return random.choice([True, False])

@app.route('/send', methods=['POST'])
def send_email():
    data = request.json
    to, subject, body = data['to'], data['subject'], data['body']
    email_id = generate_id(to, subject, body)

    if email_id in email_status:
        return jsonify({'status': 'duplicate', 'id': email_id})

    for attempt in range(3):
        provider = 'A' if attempt % 2 == 0 else 'B'
        success = send_email_mock(provider, to, subject, body)
        if success:
            email_status[email_id] = 'sent'
            return jsonify({'status': 'sent', 'id': email_id})
        time.sleep(2 ** attempt)

    email_status[email_id] = 'failed'
    return jsonify({'status': 'failed', 'id': email_id})

@app.route('/status/<email_id>')
def check_status(email_id):
    status = email_status.get(email_id, 'not_found')
    return jsonify({'id': email_id, 'status': status})

if __name__ == '__main__':
    app.run(debug=True)




