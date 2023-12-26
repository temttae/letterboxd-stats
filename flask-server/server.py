from flask import Flask

app = Flask(__name__)

# API routes
@app.route("/")
def home():
  return "home"

@app.route("/films")
def films():
  return { "films" : ["film1", "film2", "film3"] }

if __name__ == "__main__":
  app.run(debug=True)
