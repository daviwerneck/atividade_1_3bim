from flask import Blueprint, render_template, request, redirect, flash
from models import Pedido
from database import db

bp_pedido = Blueprint('pedidos', __name__, template_folder='templates')

@bp_pedido.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedido.html', pedidos = dados)

@bp_pedido.route('pedidos/add')
def add():
    return render_template('pedido_add.html')

@bp_pedido.route('/save', methods=['POST'])
def save():
    usuario_id = request.form.get('usuario_id')
    pizza_id = request.form.get('pizza_id')
    data = request.form.get('data')
    if usuario_id and pizza_id and data:
        bd_usuario = Pedido(usuario_id, pizza_id, data)
        db.session.add(bd_usuario)
        db.session.commit()
        flash('Pedido salvo com sucesso!!!')
        return redirect('/pedidos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/pedidos/add')





