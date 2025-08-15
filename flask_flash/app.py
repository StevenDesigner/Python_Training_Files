from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f"Thanks, {name}! Your message has been received.", "success")
        # print(flash.get_flashed_messages())
        return redirect(url_for('home'))
    return render_template("form_with_flash.html")

if __name__ == "__main__":
    app.run(debug=True)
