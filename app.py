from flask import Flask

app = Flask(__name__)

HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Docker on AWS EC2</title>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Segoe UI', Arial, sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .card {
        background: #ffffff;
        padding: 50px 60px;
        border-radius: 16px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.25);
        text-align: center;
        max-width: 480px;
    }
    .icon {
        font-size: 60px;
        margin-bottom: 15px;
    }
    h1 {
        color: #333;
        font-size: 28px;
        margin-bottom: 10px;
    }
    p {
        color: #666;
        font-size: 16px;
        line-height: 1.6;
    }
    .badge {
        display: inline-block;
        margin-top: 20px;
        padding: 8px 18px;
        background: #764ba2;
        color: #fff;
        border-radius: 20px;
        font-size: 13px;
        letter-spacing: 0.5px;
    }
</style>
</head>
<body>
    <div class="card">
        <div class="icon">🐳 ☁️</div>
        <h1>Hello from Docker!</h1>
        <p>This app is running inside a Docker container, deployed on an AWS EC2 instance.</p>
        <span class="badge">Flask &bull; Docker &bull; AWS EC2</span>
    </div>
</body>
</html>
"""

HEALTH_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Health Check</title>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Segoe UI', Arial, sans-serif;
        background: #0f2027;
        background: linear-gradient(135deg, #2c5364, #203a43, #0f2027);
    }
    .card {
        background: #ffffff;
        padding: 40px 55px;
        border-radius: 16px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        text-align: center;
    }
    .dot {
        width: 14px;
        height: 14px;
        background: #22c55e;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        box-shadow: 0 0 0 4px rgba(34,197,94,0.2);
    }
    h1 {
        color: #333;
        font-size: 24px;
    }
    p {
        color: #888;
        margin-top: 10px;
        font-size: 14px;
    }
</style>
</head>
<body>
    <div class="card">
        <h1><span class="dot"></span>Status: UP</h1>
        <p>Service is healthy and running smoothly.</p>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return HOME_HTML


@app.route("/health")
def health():
    return HEALTH_HTML


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    