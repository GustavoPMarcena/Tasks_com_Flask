from app import app, db
from flask import render_template, url_for, redirect, request, flash
from models import User, Tasks
from flask_login import login_user, logout_user, current_user

@app.route("/")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    tarefas = Tasks.query.filter_by(usuario=current_user.id)
    return render_template("tasks.html", titulo='Tarefas', tarefas=tarefas)


@app.route("/nova_tarefa",methods=['GET', 'POST'] )
def newtask():
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        info = request.form['info']
        tarefa = Tasks(nome, data, info, current_user.id)
        db.session.add(tarefa)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("novatask.html", titulo='Nova Tarefa')

@app.route("/login" ,methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):   
            return redirect(url_for('login'))
            
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html', titulo='Login')

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("cadastro.html", titulo='Cadastro')

@app.route('/logout')
def logout():
    flash('green')
    flash('Logout feito com sucesso!')
    logout_user()
    return redirect(url_for('login'))

@app.route('/nova_tarefa/Deletar/<int:id>', methods=['GET', 'POST'])
def deletartask(id):
    task = Tasks.query.filter_by(id=id).first()
    if request.method == 'POST':
      db.session.delete(task)
      db.session.commit()
      return redirect(url_for('home'))
    return render_template("excluirtask.html")

@app.route('/nova_tarefa/editar/<int:id>', methods=['GET', 'POST'])
def editartask(id):
    tasks = Tasks.query.filter_by(id=id).first() 
    if request.method == 'POST':
        tasks.tarefa = request.form['nome']
        tasks.data = request.form['data']
        tasks.descricao = request.form['info']
        db.session.commit()
        flash('Filme editado com sucesso!')
        return redirect(url_for('home'))
    return render_template("editartask.html", titulo='Editar Tarefa', task=tasks)