from flask import Flask, render_template,request,redirect
app = Flask(__name__)
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)