from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Success is an event, It will gradually happen!!"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)














































