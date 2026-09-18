import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """<!doctype html>
<html lang="ar" dir="rtl">
<head><meta charset="utf-8"><title>اختبار alz3by</title>
<style>body{font-family:Arial,sans-serif;background:#101827;color:#f8fafc;display:grid;place-items:center;min-height:100vh;margin:0}.card{max-width:620px;padding:36px;border-radius:20px;background:#1e293b;box-shadow:0 15px 50px #0006;text-align:center}h1{color:#38bdf8}code{color:#a7f3d0}</style>
</head><body><main class="card"><h1>موقع alz3by التجريبي يعمل</h1><p>تم تشغيل هذا الموقع الديناميكي على Render بنجاح.</p><p>المنفذ المستخدم: <code>PORT</code></p></main></body></html>"""

@app.get("/api/health")
def health():
    return jsonify(status="ok", service="alz3by-render-test", port=os.getenv("PORT", "unknown"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "10000")))
