from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)

# email credentials
my_gmail = os.environ.get("GMAIL")
password = os.environ.get("GMAIL_PASSWORD")


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/programming')
def programming():
    return render_template('programming.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/contact', methods=["POST", "GET"])
def contact():
    return render_template('contact.html')


@app.route('/contact/confirmation', methods=["POST"])
def confirmation():
    email = request.form.get('email')
    message = request.form.get('message')
    email_message = f"Subject: Website Enquiry: \n\n{message}"
    try:
        # specifying host for the connection
        with smtplib.SMTP("smtp.gmail.com") as connection:

            # encrypting
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            connection.sendmail(from_addr=my_gmail,
                                to_addrs=email,
                                msg=email_message)
        return render_template('confirmation.html')

    except:
        return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)