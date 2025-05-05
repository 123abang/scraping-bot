from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("uk_logistics_companies.csv")
    # Convert to HTML, add Bootstrap classes for styling
    table = df.to_html(
        classes="table table-striped table-hover",
        index=False,
        render_links=True,
        escape=False
    )
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>UK Logistics Companies</title>
      <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
      >
    </head>
    <body class="p-4">
      <h1 class="mb-4">UK Logistics Companies</h1>
      {table}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
