from flask import Blueprint, render_template, request, redirect, flash
from models import Medico
from database import db

bp_medico = Blueprint('medicos', __name__, template_folder='templates')

@bp_medico.route('/')
def index():
    dados = Medico.query.all()
    return render_template('medico.html', medicos = dados)

@bp_medico.route('/add')
def add():
    return render_template('medico_add.html')

@bp_medico.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    especialidade = request.form.get('especialidade')
    if nome and especialidade:
        bd_medico = Medico(nome, especialidade)
        db.session.add(bd_medico)
        db.session.commit()
        flash('Médico salvo com sucesso!!!')
        return redirect('/medicos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/medicos/add')

@bp_medico.route('/edit/<int:id_medico>')
def edit(id_medico):
    dados = Medico.query.get(id_medico)
    return render_template('medico_edit.html', medicos = dados)

@bp_medico.route('/remove/<int:id_medico>')
def remove(id_medico):
    dados = Medico.query.get(id_medico)
    if id_medico > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Médico removido com sucesso!')
        return redirect('/medicos')
    else:
        flash("Ops! ID inválido!")
        return redirect("/medicos")

@bp_medico.route('/editsave', methods=['POST'])
def editsave():
    id_medico = request.form.get('id_medico')
    nome = request.form.get('nome')
    especialidade = request.form.get('especialidade')
    if id_medico and nome and especialidade:
        medico = Medico.query.get(id_medico)
        medico.nome = nome
        medico.especialidade = especialidade
        db.session.commit()
        flash('Dados editados com sucesso!!!')
        return redirect('/medicos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/medicos')



