from flask import Blueprint, render_template, request, redirect, flash
from models import Paciente
from models import Medico
from database import db

bp_paciente = Blueprint('pacientes', __name__, template_folder='templates')

@bp_paciente.route('/')
def index():
    dados = Paciente.query.all()
    return render_template('paciente.html', pacientes = dados)

@bp_paciente.route('/add')
def add():
    dados = Medico.query.all()
    return render_template('paciente_add.html', medicos = dados)

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
