from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rename_files', methods=['POST'])
def rename_files():
    path = request.form['path']
    file_name = request.form['file_name']
    file_format = request.form['file_format']
    i = 0

    try:
        for filename in os.listdir(path):
            my_dest = file_name + str(i) + file_format
            my_source = os.path.join(path, filename)
            my_dest = os.path.join(path, my_dest)
            os.rename(my_source, my_dest)
            i += 1
        return redirect(url_for('index', success=True))
    except Exception as e:
        return redirect(url_for('index', error=str(e)))

if __name__ == '__main__':
    app.run(debug=True)
