# from flask import Flask, request,redirect, url_for,session,Response,render_template
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello User! This is my First flask app.'

# app.run(debug=True)



# app = Flask(__name__)
# app.secret_key = 'SuperSecret'

# @app.route("/", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':                        # ← must be uppercase
#         username = request.form.get('username')
#         password = request.form.get('password')

#         if username == 'admin' and password == '123':
#             session['username'] = username
#             return redirect(url_for('welcome'))
#         else:
#             # note: mimetype, not minetype
#             return Response(
#                 'Invalid credentials, please try again.',
#                 mimetype='text/plain'
#             )

#     # GET request: show form
#     return '''
#         <h2>Login Page</h2>
#         <form method="post">
#           Username: <input type="text" name="username"><br>
#           Password: <input type="password" name="password"><br>
#           <input type="submit" value="Login">
#         </form>
#     '''

# @app.route("/welcome")
# def welcome():
#     if 'username' in session:
#         return f'''
#             <h2>Welcome, {session['username']}!</h2>
#             <a href="{url_for('logout')}">Logout</a>
#         '''
#     # if no session, send back to login
#     return redirect(url_for('login'))

# @app.route("/logout")                               # ← fixed decorator
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)                              # ← restart after saving


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('home.html')


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_templatef

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("profile.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# if __name__ == "__main__":
#     app.run(debug=True)


