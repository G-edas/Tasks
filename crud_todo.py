from flask import Flask, flash, jsonify, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()
app = Flask(__name__)

app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    created_date = db.Column(db.DateTime, nullable = False)
    description = db.Column(db.String, nullable = False)

with app.app_context():
    db.create_all()
    
@app.route('/')
def home():
    all_todos = Todo.query.all()
    return render_template("index.html", all_todos = all_todos)


@app.route('/create_todo', methods=["GET" ,"POST"])
def post_todo():
    if request.method == "POST":
        todo = Todo(
            title = request.form['title'],
            created_date = datetime.now(),
            description = request.form['description']
        )
        db.session.add(todo)
        db.session.commit()
        flash("To-Do added successfully!")
        return redirect(url_for("home"))
    else:
        return render_template("create_todo.html")



@app.route('/show_todo/<int:id>', methods=["GET"])
def get_todo(id):
    todo = db.get_or_404(Todo, id)
    return render_template("show_todo.html", todo = todo)


@app.route('/show_todo/<int:id>/update', methods = ["GET", "POST"])
def update_todo(id):
    todo = db.get_or_404(Todo, id)
    if request.method == "POST":
        todo.title = request.form['title']
        todo.description = request.form['description']
        db.session.commit()
        flash('Todo was successfully updated!')
        return redirect(url_for("home"))
    else:
        return render_template("update_todo.html")
    



@app.route('/show_todo/<int:id>/delete', methods = ["GET", "POST"])
def delete_todo(id):
    todo = db.get_or_404(Todo, id)
    if request.method == "POST":
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("show_todo.html")