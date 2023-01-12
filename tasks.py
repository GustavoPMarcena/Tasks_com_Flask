from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("tasks.html", titulo='Tarefas')


@app.route("/nova_tarefa")
def newtask():
    return render_template("novatask.html", titulo='Nova Tarefa')

@app.route("/login")
def login():
    return render_template('login.html', titulo='Login')

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html", titulo='Cadastro')

# TASKS 
# LOGIN
# CRIAR NOVA TASK
# CADASTRO

if __name__ == '__main__':
   app.run(debug=True)