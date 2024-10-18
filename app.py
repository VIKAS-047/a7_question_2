from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder="html",         # Specify custom folder for HTML
            static_folder="assets")         # Specify custom folder for static files

# Temporary storage for registered users
users = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['userID']
        password = request.form['password']

        if user_id in users:
            return "User already exists! Please try another User ID."
        else:
            users[user_id] = password
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['userID']
        password = request.form['password']

        if user_id in users and users[user_id] == password:
            return "Login successful!"
        else:
            return "Invalid credentials. Please try again."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
