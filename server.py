from flask import Flask, render_template, url_for, request, redirect
import os
import csv
app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    file_exists = os.path.isfile('database.csv')
    with open('database.csv', mode='a', newline='') as database:
        fieldnames = ['email', 'subject', 'message']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if not file_exists:
            csv_writer.writerow(fieldnames)

        csv_writer.writerow([email, subject, message])

        #  writer.writeheader()


def write_to_csv2(data):
    with open('database.csv', mode='a', newline='') as database:
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(database, fieldnames=fieldnames)
      #  writer.writeheader()
        # email = data['email']
        # subject = data['subject']
        # message = data['message']
        writer.writerow(data)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, try again'


# @app.route('/components.html')
# def components():
#     return render_template('components.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/contact.html')
# def contact():
#   #  return 'Hello, Ralston!'
#     return render_template('contact.html')


# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs!!!'


# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my dog'


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/<username>/<int:post_id>')
# def hello_username(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


# for item in os.listdir('templates'):
#     print(item)
#     print(f"@app.route('/{item}')")
