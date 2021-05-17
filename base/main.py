# frontend
import CRUD


def addPost(app):
    author = input("Who is the author? ")
    post = input("Type in their post: ")
    app.addPost(author, post)

def showPost(post):
    print(f"Author: {post.author}\n{post.post}")

def displayPost(app):
    try:
        id = int(input("What is the id of the post? "))
    except ValueError:
        print("Not a valid id")
        return displayPost(app)

    try:
        post = app.getPost(id)
        showPost(post)
    except CRUD.POSTNOTFOUND:
        print(f"{id} not found")

def displayAllPosts(app):
    posts = app.getAllPosts()
    for post in posts:
        showPost(post)

def deletePost(app):
    try:
        id = int(input("What post to delete? "))
    except ValueError:
        print("Not a valid id")
        return deletePost(app)

    success = app.delete(id)
    if success:
        print("Deleted")
    else:
        print("Wasn't able to delete")

def save(app):
    app.save()

def getMenuChoice():
    menu = """
1. Add new post
2. Get specific post
3. Get all posts
4. Delete post
5. Save
X. Exit

>>> """

    choice = input(menu)

    functions = {
        "1": addPost,
        "2": displayPost,
        "3": displayAllPosts,
        "4": deletePost,
        "5": save,
        "X": False
    }
    
    return functions.get(choice.upper(), None)

def main(app):
    func = getMenuChoice()
    if func == False:
        return

    if func:
        func(app)
    else:
        print("[Invalid choice]")

    main(app)

if __name__ == "__main__":
    app = CRUD.App()
    app.load()
    main(app)
