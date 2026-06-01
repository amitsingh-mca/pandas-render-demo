from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "Name": ["Amit", "Rahul", "Priya"],
        "Marks": [85, 92, 78]
    }

    df = pd.DataFrame(data)
    table_html = df.to_html(classes="table table-striped", index=False)

    return render_template("index.html", table=table_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)