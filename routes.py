from flask import Blueprint, request, jsonify
from models import blogs

blog_bp = Blueprint('blog', __name__)

# Get all blog posts
@blog_bp.route('/posts', methods=['GET'])
def get_all():
    return jsonify(blogs), 200

# Create a new blog post
@blog_bp.route('/posts', methods=['POST'])
def create():
    data = request.get_json()

    # Basic validation
    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "Title and content required"}), 400

    blog = {
        "id": len(blogs) + 1,
        "title": data["title"],
        "content": data["content"]
    }
    blogs.append(blog)
    return jsonify(blog), 201

# Get a single blog post
@blog_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_one(post_id):
    blog = next((b for b in blogs if b["id"] == post_id), None)
    if blog:
        return jsonify(blog)
    return jsonify({"error": "Not found"}), 404

# Update a blog post
@blog_bp.route('/posts/<int:post_id>', methods=['PUT'])
def update(post_id):
    data = request.get_json()
    for blog in blogs:
        if blog["id"] == post_id:
            blog["title"] = data.get("title", blog["title"])
            blog["content"] = data.get("content", blog["content"])
            return jsonify(blog)
    return jsonify({"error": "Not found"}), 404

# Delete a blog post
@blog_bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete(post_id):
    global blogs
    blogs = [b for b in blogs if b["id"] != post_id]
    return jsonify({"message": "Deleted"}), 200

@blog_bp.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Blog API 🎉</h1><p>Use <code>/posts</code> to access blog posts.</p>"