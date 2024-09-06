import subprocess


if __name__ == "__main__":
    code_str = """from backend.app import create_app
flask_app = create_app()
flask_app.run(debug=True, host='0.0.0.0', port=8080)"""
    subprocess.Popen(['python', '-c', code_str])
    subprocess.Popen(["npm", "start"], cwd='frontend')

    input()
