from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(host=app.config["HOSTNAME"], port=app.config["PORT"])
