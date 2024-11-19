from flask import Blueprint, render_template, request, redirect, flash
from models import Paciente, Medico
from database import db

bp_paciente = Blueprint('pacientes', __name__, template_folder='templates')

@bp_paciente.route('/')
def index():
    p = Paciente.query.all()
    return render_template('paciente.html', pacientes = p)

@bp_paciente.route('/add')
def add():
    m = Medico.query.all()
    return render_template('paciente_add.html', medicos = m)

@bp_paciente.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    id_medico = request.form.get('id_medico')
    if nome and idade and id_medico:
        bd_paciente = Paciente(nome, idade, id_medico)
        db.session.add(bd_paciente)
        db.session.commit()
        flash('Paciente salvo com sucesso!!!')
        return redirect('/pacientes')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/pacientes/add')

@bp_paciente.route('/edit/<int:id_paciente>')
def edit(id_paciente):
    dados1 = Paciente.query.get(id_paciente)
    dados2 = Medico.query.all()
    return render_template('paciente_edit.html', pacientes = dados1, medicos = dados2)

@bp_paciente.route('/remove/<int:id_paciente>')
def remove(id_paciente):
    dados = Paciente.query.get(id_paciente)
    if id_paciente > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Paciente removido com sucesso!')
        return redirect('/pacientes')
    else:
        flash("Ops! ID inválido!")
        return redirect("/pacientes")

@bp_paciente.route('/editsave', methods=['POST'])
def editsave():
    id_paciente = request.form.get('id_paciente')
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    id_medico = request.form.get('id_medico')
    if id_paciente and nome and idade and id_medico:
        paciente = Paciente.query.get(id_paciente)
        paciente.nome = nome
        paciente.idade = idade
        paciente.id_medico = id_medico
        db.session.commit()
        flash('Dados editados com sucesso!!!')
        return redirect('/pacientes')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/pacientes')