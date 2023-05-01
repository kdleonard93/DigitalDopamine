from flask import Flask
from flask_pymongo import PyMongo
from models import Post

app.config["MONGO_URI"] = "mongodb+srv://admin:j0HLZlbyuUR4lU2Y@cluster1.51guhmb.mongodb.net/?retryWrites=true&w=majority"
mongo = PyMongo(app)
app = Flask(__name__)


@app.route("/")
def home():
    posts = Post.get_all_posts()
    return render_template("blog.html", posts=posts)


@app.route("/post/<string:id>")
def post(id):
    post = Post.get_post_by_id(id)
    return render_template("post.html", post=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    projects = Project.get_all_projects()
    return render_template("projects.html", projects=projects)


@app.route("/project/<string:id>")
def project(id):
    project = Project.get_project_by_id(id)
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)
