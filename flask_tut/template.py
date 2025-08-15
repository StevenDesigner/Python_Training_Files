from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return redirect(url_for('thank_you', user=name))
    
    # Render HTML template instead of inline HTML
    return render_template("contact.html")

@app.route("/thank-you")
def thank_you():
    user = request.args.get('user', 'Guest')
    return render_template("thank_you.html", username=user)

if __name__ == "__main__":
    app.run(debug=True)
