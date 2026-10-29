import json


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def save_json(file_path, posts):
    with open(file_path, "w") as file:
        json.dump(posts, file, indent=2)


def add_new_post(title, author, content, file_path):
    posts = load_json(file_path)
    id = get_new_post_id(posts)
    posts.append({"id": id, "author": author, "title": title, "content": content})
    save_json(file_path, posts)


def get_new_post_id(posts):
    max_id = max((post["id"] for post in posts), default=0)
    return max_id + 1


def delete_blog_post(id, file_path):
    posts = load_json(file_path)
    new_posts = [post for post in posts if post["id"] != id]
    save_json(file_path, new_posts)


def get_post_by_id(id, file_path):
    posts = load_json(file_path)
    post = [post for post in posts if post["id"] == id]
    if len(post) > 0:
        return post[0]


def update_blog_post(id, title, author, content, file_path):
    posts = load_json(file_path)
    new_posts = [post for post in posts if post["id"] != id]
    new_posts.append({"id": id, "author": author, "title": title, "content": content})
    save_json(file_path, new_posts)
