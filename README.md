# My Blog API

This is a simple blog API project built with Python and Flask.

## Features
- Create, Read, Update, Delete blog posts via REST API.
- Easy to extend and deploy.

## Setup Instructions
1. Create and activate virtual environment.
2. Install dependencies from `requirements.txt`.
3. Run the Flask app.

## API Endpoints
- `GET /posts` - Get all posts
- `POST /posts` - Create a new post
- `DELETE /posts/{id}` - Delete a post by ID

## How to Add, Update, and Delete Blog Posts

### Add a Post (Create)
Send a `POST` request to `/posts` with JSON body containing `"title"` and `"content"`.

**You can do this using:**

- **Postman:**  
  1. Set method to `POST`.  
  2. Enter URL `http://127.0.0.1:5000/posts`.  
  3. Select **Body** → **raw** → **JSON**.  
  4. Paste JSON like:  
  ```json
  {
    "title": "My New Post",
    "content": "This is the content of the new post."
  }

- Same way for Update and Delete

