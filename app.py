from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify(status='ok')

@app.route('/')
def home():
    return '<h1>Flask Backend</h1><p>Visit /api/health for health check</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


