from flask import Flask, render_template
from helper_func import *

app = Flask(__name__)

@app.route("/")
def template_test():
    args = request.args.copy()
    results, counter_msg = process_request(args)
    return render_template('template.html', my_string=counter_msg,
        my_list=results, title="Index")

if __name__ == '__main__':
    app.run(debug=True)
