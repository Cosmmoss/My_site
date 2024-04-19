from flask import Flask, request
app = Flask (__name__)

@app.route("/get_example")
def get_example():
   framework = 5
   language = request.args.get('language')
   version = request.args.get('version')
   return f"language = {language}, framework = {framework}, version = {version}"

if __name__ == '__main__':
    app.run(debug = True)