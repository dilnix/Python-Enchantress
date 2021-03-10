from re import L
from flask_login import login_required, current_user
from flask import Blueprint, render_template

from .models import Order, OrderLine


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return {'mainpage': 'no data here'}, 200


@main.route('/profile')
@login_required
def profile():
    orders_count = Order.objects.filter_by(
        user_id=current_user.id).all().count()
    return {'profile of user': current_user.email, 'user_id': current_user.id, 'name': current_user.name, 'orders': orders_count}, 200


@main.route('/orders')
@login_required
def orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return {f'orders of user {current_user.email}': orders}, 200


@main.route('/order/<int:_id>')
@login_required
def order_details(_id):
    order = Order.query.filter_by(id=_id).first()
    order_lines = OrderLine.query.filter_by(order_id=order.id).all()
    return {f'order with id {order.id}': order_lines}, 200
