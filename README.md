# Aman-Store
Aman Ka Apna Digital Store Aur Satta King Live Server 
from flask import Flask, request

app = Flask(__name__)

# यहाँ आप अपना रिजल्ट बदल सकते हो
satta_result = "78" 

@app.route('/')
def home():
    return f"""
    <html>
    <body style="background-color:black; color:lime; text-align:center; font-family:sans-serif;">
        <h1>🔥 Faridabad Satta King Live 🔥</h1>
        <div style="border:5px solid red; padding:20px; font-size:50px;">
            LATEST RESULT: {satta_result}
        </div>
        <hr>
        <h2>Welcome to Aman Store</h2>
        <p>Download our latest hacking tools below!</p>
        <button onclick

        <p style="margin-top:50px;">Design by Aman Hacker</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    
