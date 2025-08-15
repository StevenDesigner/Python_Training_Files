from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        print(f"Received message from {name}: {message}")  # Just for testing
        return redirect(url_for('thank_you', user=name))
    
    # GET request → Show the form
    return '''
        <h2>Contact Us</h2>
        <form method="POST">
            <label>Name:</label>
            <input type="text" name="name" required><br><br>
            <label>Message:</label>
            <textarea name="message" required></textarea><br><br>
            <button type="submit">Send</button>
        </form>
    '''

@app.route("/thank-you")
def thank_you():
    user = request.args.get('user', 'Guest')
    return f"<h3>Thank you, {user}! Your message has been received.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
