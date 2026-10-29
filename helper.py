import json


def load_json(file_path):
    """Loads the json file by a given path"""

    with open(file_path, "r") as file:
        return json.load(file)


def save_json(file_path, posts):
    """Saves the json to a file in the given file path"""

    with open(file_path, "w") as file:
        json.dump(posts, file, indent=2)


def add_new_post(title, author, content, file_path):
    """Adds a new post to the current blog posts"""

    posts = load_json(file_path)
    id = get_new_post_id(posts)
    posts.append({"id": id, "author": author, "title": title, "content": content})
    save_json(file_path, posts)


def get_new_post_id(posts):
    """Returns a new id which is the current max id + 1"""

    max_id = max((post["id"] for post in posts), default=0)
    return max_id + 1


def delete_blog_post(id, file_path):
    """Deletes a post with a given id"""

    posts = load_json(file_path)
    new_posts = [post for post in posts if post["id"] != id]
    save_json(file_path, new_posts)


def get_post_by_id(id, file_path):
    """Returns the data of a post with a given id"""

    posts = load_json(file_path)
    post = [post for post in posts if post["id"] == id]
    if len(post) > 0:
        return post[0]


def update_blog_post(id, title, author, content, file_path):
    """Updates a post with a given id"""

    posts = load_json(file_path)
    new_posts = [post for post in posts if post["id"] != id]
    new_posts.append({"id": id, "author": author, "title": title, "content": content})
    save_json(file_path, new_posts)
