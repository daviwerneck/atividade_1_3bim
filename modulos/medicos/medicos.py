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





