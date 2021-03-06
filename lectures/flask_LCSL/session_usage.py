from flask import Flask, session, redirect, url_for, request
from datetime import timedelta

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'4GriphUfveegFom~'
ttt = timedelta(minutes=1)


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['permanent'] = True
        session['permanent_session_lifetime'] = str(ttt)
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
