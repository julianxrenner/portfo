from flask import Flask, render_template, request, redirect
import csv
#flask --app server run --debug
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},    {subject},    {message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)      
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'Thank you! I got your information I will reach out to you soon!' #redirect('/thankyou.html')
        except:
            return 'Did not save to database, try again'
    else:
        return 'Something went wrong try again!'