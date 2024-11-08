from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/de/messageInfo/01939050', methods=['GET', 'POST'])
def home_de():
    return render_template('de.html')


@app.route('/en/messageInfo/01939050', methods=['GET', 'POST'])
def home_en():
    return render_template('en.html')


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=False, host='0.0.0.0')
