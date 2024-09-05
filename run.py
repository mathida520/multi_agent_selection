import subprocess


if __name__ == "__main__":
    code_str = """from backend.app import flask_app
flask_app.run(debug=True, host='0.0.0.0', port=11435)"""
    subprocess.Popen(['python', '-c', code_str])
    subprocess.Popen(["npm", "start"], cwd='frontend')

    input()
