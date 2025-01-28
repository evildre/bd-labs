from flask import Flask, request
from queris import queries_list


app = Flask(__name__)


@app.route("/api/<query_index>")
def index(query_index):
    if not query_index.isdigit() or int(query_index) > len(queries_list) - 1:
        return "Unexpected query ID"

    return queries_list[int(query_index)](request.args)


if __name__ == "__main__":
    app.run(debug=True)
    