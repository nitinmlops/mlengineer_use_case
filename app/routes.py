from flask import Blueprint, request, jsonify
from .sentiment import analyze_comments
import requests

main = Blueprint('main', __name__)

@main.route('/comments/<subfeddit>', methods=['GET'])
def get_comments(subfeddit):
    comments = fetch_comments_from_subfeddit(subfeddit)
    analyzed_comments = analyze_comments(comments)
    return jsonify(analyzed_comments)

def fetch_comments_from_subfeddit(subfeddit):
    # Replace this with the actual API call
    url = f"http://external-api-url/comments/{subfeddit}?limit=25"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []
