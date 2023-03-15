import json
from flask import flash
from crud_todo import app, Todo, db
from datetime import datetime
from sqlalchemy import text
from werkzeug.exceptions import BadRequest
import logging


def test_home_page():
    response = app.test_client().get('/')
    print(response.data)
    assert response.status_code == 200
    assert b"id=\"go-post-form\"" in response.data    
test_home_page()


def test_get_post_todo():
   
    response = app.test_client().get('/create_todo')
    assert response.status_code == 200
    assert b"id=\"new-todo-list\"" in response.data
test_get_post_todo()



def test_db_post_todo():
    with app.app_context():
        test_todo = Todo(
            title = 'Testas',
            created_date = datetime.now(),
            description = 'Testas vykdomas...'
        )
        db.session.add(test_todo)
        db.session.commit()
        
        entity = Todo.query.filter_by(title='Testas').first().title
        assert 'Testas' in entity
        
        db.session.delete(test_todo)
        db.session.commit()
        
test_db_post_todo()


def test_post_post_todo():
    app.config.update({
        "TESTING": True,
    })
    data = {
        'title': "programavimas", 
        'created_Date': '2023-03-13 12:46:15.648042',
        'description': 'pytest testas'
    }
    response = app.test_client().post('/create_todo', data = data)
    assert response.status_code == 302
test_post_post_todo()


def test_get_todo():
    with app.app_context():
        test_todo = Todo(
            title = 'Testas2',
            created_date = datetime.now(),
            description = 'Testas2 vykdomas...'
        )
        db.session.add(test_todo)
        db.session.commit()
        
        entity = Todo.query.filter_by(title='Testas2').first().title
        entity_id = Todo.query.filter_by(title='Testas2').first().id

        response = app.test_client().get('/show_todo/{}'.format(entity_id))

        assert entity in str(response.data)

test_get_todo()


def test_update_todo_post():
     with app.app_context():
        test_todo = Todo(
            title = 'Testas3',
            created_date = datetime.now(),
            description = 'Testas3 vykdomas...'
        )
        db.session.add(test_todo)
        db.session.commit()
        
        entity_id = Todo.query.filter_by(title='Testas3').first().id
        
        data = {
        'title': "Testas3_updated", 
        'created_Date': '2030-03-13 12:46:15.648042',
        'description': 'Testas 3 updated'
        }
        
        response = app.test_client().post('/show_todo/{}/update'.format(entity_id), data = data)
        
        assert response.status_code == 302
        
test_update_todo_post()
        

def test_update_todo_get():
    
    with app.app_context():
        test_todo = Todo(
            title = 'Testas3',
            created_date = datetime.now(),
            description = 'Testas3 vykdomas...'
        )
        db.session.add(test_todo)
        db.session.commit()
        
        entity_id = Todo.query.filter_by(title='Testas3').first().id
        
        response = app.test_client().get('/show_todo/{}/update'.format(entity_id))
        assert response.status_code == 200
        
test_update_todo_get()



def test_delete_todo_post():
    with app.app_context():
        test_todo = Todo(
            title = 'Testas4',
            created_date = datetime.now(),
            description = 'Testas4 vykdomas...'
        )
        db.session.add(test_todo)
        db.session.commit()
        
        entity_id = Todo.query.filter_by(title='Testas4').first().id
        
        response = app.test_client().post('/show_todo/{}/delete'.format(entity_id))
        assert response.status_code == 302

test_delete_todo_post()
        

