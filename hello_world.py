import os
from flask import Flask, url_for, render_template, request, send_from_directory
from werkzeug import secure_filename


UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return 'Hey Pardo. Wassup!'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        print request.form['name']
        print request.form['email']
    return render_template('login.html', error=error)


@app.route('/hp/')
def redirect():
    return hello("Peter")


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("uploaded_file.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug=True)
    # show the user profile for that user

for css_file in os.listdir('./static/css/'):
    url_for('static/css', filename=css_file)

for img_file in os.listdir('./static/img/'):
    url_for('static/img', filename=img_file)

for upload_file in os.listdir('./uploads/'):
    url_for('uploads', filename=upload_file)
