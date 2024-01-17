# Import necessary libraries
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')

class AMS():
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.dob = ""
        self.mbno = ""
        self.mail = ""
        self.pwsd = ""

data = AMS()

# Define the signup route
@app.route('/signup', methods=["POST", "GET"])
def signup():
    password_match_error = None
    account_created = None

    if request.method == "POST":
        # Get data from the form
        data.fname = request.form.get('fname')
        data.lname = request.form.get('lname')
        data.dob = request.form.get('dob')
        data.mbno = request.form.get('mbno')
        data.mail = request.form.get('mail')
        password = request.form.get('p')
        confirm_password = request.form.get('pwsd')

        # Check if passwords match
        if password != confirm_password:
            password_match_error = "Passwords do not match. Please try again."
        else:
            data.pwsd = password
            account_created = "Account has been created Succesfully !"

    return render_template('signup.html', password_match_error=password_match_error,
                           account_created = account_created)

# Define the profile route
@app.route('/profile', methods=["GET"])
def profile():
    return render_template('profile.html', fname=data.fname, lname=data.lname, dob=data.dob,
                            mbno=data.mbno, mail=data.mail, pwsd=data.pwsd)


#Login to the Account
@app.route('/login', methods = ["GET", "POST"])
def login():
    msg1 = None
    msg2 = None
    if request.method == "POST":
        lmail = request.form.get('lmail')
        lpass = request.form.get('lpass')
        if (lmail == data.mail) and (lpass == data.pwsd):
            msg1 = "Acoount Login Successfull !"
            return render_template('main.html')
        else:
            msg2 = "Entered Mail-ID or Password are mismatched with each other !"
    
    return render_template('login.html', msg1 = msg1, msg2 = msg2 )

#Change Password for the User
@app.route('/c_password', methods = ["GET","POST"])
def change_pass():
    msg = None
    if request.method == "POST":
        data.mail = request.form.get('cmail')
        cpass = request.form.get('cpass')
        pwsd = request.form.get('pwsd')
        if (cpass == pwsd):
            data.pwsd = pwsd
            msg = "Password has changes Successfully !"
    return render_template('cpass.html', msg = msg)

if __name__ == "__main__":
    app.run(debug=True)
