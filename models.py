from datetime import datetime
from app import mongo


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date_posted = datetime.utcnow()

    @staticmethod
    def get_all_posts():
        return mongo.db.posts.find()

    @staticmethod
    def get_post_by_id(id):
        return mongo.db.posts.find_one({"_id": id})

    def save(self):
        return mongo.db.posts.insert_one({
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "date_posted": self.date_posted
        })


class Project:
    def __init__(self, title, description, skills, budget, deadline, author):
        self.title = title
        self.description = description
        self.skills = skills
        self.budget = budget
        self.deadline = deadline
        self.author = author

    @staticmethod
    def get_all_projects():
        return mongo.db.projects.find()

    @staticmethod
    def get_project_by_id(id):
        return mongo.db.projects.find_one({"_id": id})

    def save(self):
        return mongo.db.projects.insert_one({
            "title": self.title,
            "description": self.description,
            "skills": self.skills,
            "budget": self.budget,
            "deadline": self.deadline,
            "author": self.author
        })
