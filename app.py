from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'stringqueninguémsabe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Medico, Paciente
db.init_app(app)
migrate = Migrate(app, db)
from modulos.medicos.medicos import bp_medico
app.register_blueprint(bp_medico, url_prefix='/medicos')


from modulos.pacientes.pacientes import bp_paciente
app.register_blueprint(bp_paciente, url_prefix='/pacientes')

@app.route('/')
def index():
    return render_template("ola.html")