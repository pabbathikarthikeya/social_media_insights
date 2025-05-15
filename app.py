from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select')
def select_platform():
    return render_template('select_platform.html')

@app.route('/platform', methods=['POST'])
def platform():
    selected = request.form['platform']
    if selected == 'LinkedIn':
        return render_template('linkedin.html')
    elif selected == 'Instagram':
        return render_template('instagram.html')
    else:
        return "Platform not supported yet."

if __name__ == '__main__':
    app.run(debug=True)
