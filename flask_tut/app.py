# from flask import Flask

# # Create a Flask application instance
# app = Flask(__name__)

# # Define a route (URL path) and its function
# @app.route("/")
# def home():
#     return "Hello, World! This is my first Flask app."

# # Run the app (only if this script is run directly)
# if __name__ == "__main__":
#     app.run(debug=True)  # debug=True auto-reloads on changes

####################--------------POST ,GET--------------####################

from flask import Flask, request

app = Flask(__name__)

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"Form submitted! Hello, {username}."
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Enter your name">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
