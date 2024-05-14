from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Meme(db.Model):
    __tablename__= 'cat_names_table'
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String)
    caption = db.Column(db.String)
    likes = db.Column(db.Integer, default=0)

    def to_dict(self):
        return{
            'id':self.id,
            'caption':self.caption,
            'img_url':self.img_url,
            'likes':self.likes
        }

# Meme ########
# id -> int
# img_url -> str
# caption -> str
# likes -> int
# #############

