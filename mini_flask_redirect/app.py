from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return redirect(url_for('thank_you', user=name))
    return render_template("form.html")

@app.route("/thank-you")
def thank_you():
    user = request.args.get('user', 'Guest')
    return render_template("thankyou.html", username=user)

if __name__ == "__main__":
    app.run(debug=True)
