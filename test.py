from flask import Flask, request
app = Flask (__name__)

@app.route("/")
def test():
    return '''<h2>Hello my freind</h2>
    <p>Hello</p>'''
   

if __name__ == '__main__':
    app.run(debug = True)