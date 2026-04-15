"""
Project Title: Simple Blog App
Name: Your Name
Date: 2026
Description: A basic CRUD blog using Flask (no database)
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (list of dictionaries)
posts = []

# HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html', posts=posts)

# CREATE POST
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        posts.append({'title': title, 'content': content})
        return redirect(url_for('home'))

    return render_template('create.html')

# EDIT POST
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    post = posts[index]

    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        return redirect(url_for('home'))

    return render_template('edit.html', post=post, index=index)

# DELETE POST
@app.route('/delete/<int:index>')
def delete(index):
    posts.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)