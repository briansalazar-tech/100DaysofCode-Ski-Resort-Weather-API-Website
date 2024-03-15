from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from weatherdata import generate_tables

resort_tables = generate_tables() # Stores the returned data from weatherdata to a variable.

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    resort_names = []
    for resort in range(len(resort_tables)):
        resort_names.append(resort_tables[resort][0]) # Resort names are appended to list.
    return render_template("index.html", resort_names=resort_names)


@app.route("/resorts/<num>")
def resort(num):
    resort_names = []
    for resort in range(len(resort_tables)):
        resort_names.append(resort_tables[resort][0]) # Names are used as a 'nav section' below the rendered table.
    
    resort_values = resort_tables[int(num)] # resort tables is made up of sublists that contain each resorts information.
    
    return render_template("resort.html", resort_names=resort_names, resort_values=resort_values)


if __name__ == "__main__":
    app.run(debug=True, port=5002)