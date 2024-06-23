from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

def get_recommendations():
    movie_title = request.json['movie_title']
    recommendations = recommend(movie_title)
    return jsonify(recommendations.tolist())

if __name__ == '__main__':
    app.run(debug=True)

