#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Meme # import your models here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/api/')
def index():
    return "Hello"


@app.get('/api/cat-meme')
def get_all_cat_memes():
    return [meme.to_dict() for meme in Meme.query.all()], 200

# write your routes here!

@app.get('/api/cat-meme/<int:id>')
def get_by_id(id):
    meme = Meme.query.where(Meme.id ==id).first()
    if meme:
        return meme.to_dict(),200
    else:
        return {"error":"Not Found"}, 404
    

@app.post('/api/cat-meme')
def post_cat_mame():
    new_cat_meme = Meme(
        caption = request.json.get('caption'),
        img_url = request.json.get('img_url'),
        likes = request.json.get('likes') #None
    )
    db.session.add(new_cat_meme)
    db.session.commit()
    return new_cat_meme.to_dict(),201


@app.delete('/api/cat-meme/<int:id>')
def delete_cat_meme(id:int):
    meme_to_delete = Meme.query.where(Meme.id==id).first()
    if meme_to_delete:
        db.session.delete(meme_to_delete)
        db.session.commit()
        return {}, 204
    else:
        return {"error":"Not Found"}, 404
    
@app.patch('/api/cat-meme/<int:id>')
def patch_cat_meme(id):
    meme_to_update = Meme.query.where(Meme.id==id).first()
    if meme_to_update:
        for key in request.json.keys():
            setattr(meme_to_update, key, request.json[key])
        db.session.add(meme_to_update)
        db.session.commit()
        return meme_to_update.to_dict(),202
    else:
        return {"error":"Not Found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
