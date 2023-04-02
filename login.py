from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key' # Khóa bảo vệ session

# Trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Kiểm tra thông tin đăng nhập
        if username == 'admin' and password == 'admin':
            # Lưu thông tin đăng nhập vào session
            session['logged_in'] = True
            session['username'] = username

            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid login')

    return render_template('login.html')

# Trang dashboard (yêu cầu đăng nhập)
@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session and session['logged_in'] == True:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))

# Đăng xuất
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
