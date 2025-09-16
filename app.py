from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Banco de dados simples em memória
tarefas = []
contador_id = 1

# Modelo Tarefa
class Tarefa:
    def __init__(self, id, titulo, descricao, data):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data

# Rota: Listar todas as tarefas
@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

# Rota: Criar nova tarefa
@app.route("/create", methods=["GET", "POST"])
def create():
    global contador_id
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        data = request.form["data"]
        nova_tarefa = Tarefa(contador_id, titulo, descricao, data)
        tarefas.append(nova_tarefa)
        contador_id += 1
        return redirect(url_for("index"))
    return render_template("create.html")

# Rota: Editar tarefa
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    tarefa = next((t for t in tarefas if t.id == id), None)
    if not tarefa:
        return "Tarefa não encontrada!", 404
    if request.method == "POST":
        tarefa.titulo = request.form["titulo"]
        tarefa.descricao = request.form["descricao"]
        tarefa.data = request.form["data"]
        return redirect(url_for("index"))
    return render_template("edit.html", tarefa=tarefa)

# Rota: Deletar tarefa
@app.route("/delete/<int:id>")
def delete(id):
    global tarefas
    tarefas = [t for t in tarefas if t.id != id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)