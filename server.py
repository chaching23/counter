from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it safe'

print(__name__)

@app.route("/")
def index():
    if not 'count' in session:
        session ['count'] = 0

    else:
        session ['count']  +=2 
    return render_template("index.html")


@app.route('/destroy_session')
def index2():
    session.clear()		
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
