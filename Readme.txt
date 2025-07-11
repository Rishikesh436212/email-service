Description:
1	Creates Flask app
2	Stores sent email status
3	Generates unique ID for each email
4	Simulates email sending with retry
5	Avoids sending same email twice
6	Lets you check status of email later
**Resilient Email Sending Service (Flask)**

*This is a simple email sending service built using Python and Flask.

**Features**
- Retry with exponential backoff
- Fallback between two mock providers (A & B)
- Idempotency to prevent duplicate sends
- Email status tracking
 **How to Run**
bash
pip install -r requirements.txt
python app.py
**how to test**
curl -X POST http://localhost:5000/send \
 -H "Content-Type: application/json" \
 -d "{\"to\":\"rishi@example.com\",\"subject\":\"Test\",\"body\":\"Hello\"}"
