from database import db
from sqlalchemy import ForeignKey

class Medico(db.Model):
    __tablename__ = 'medico'
    id_medico = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    especialidade = db.Column(db.String(50))

    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
    
    def __repr__(self):
        return "<Medico {}>".format(self.nome)

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id_paciente = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id_medico'))

    medico = db.relationship('Medico', foreign_keys=id_medico)

    def __init__(self, nome, idade, id_medico):
        self.nome = nome
        self.idade = idade
        self.id_medico = id_medico

    def __repr__(self):
        return "<Paciente {}>".format(self.nome)
