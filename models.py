from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(40))
    
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash( password)
    
    def verify_password (self, password):
        return check_password_hash(self.password, password)
    
    def __str__(self):
        return self.username
    
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String)
    data = db.Column(db.String)
    descricao = db.Column(db.String)
    usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, tarefa, data, descricao, usuario ):
        self.tarefa = tarefa
        self.data = data
        self.descricao = descricao
        self.usuario = usuario    