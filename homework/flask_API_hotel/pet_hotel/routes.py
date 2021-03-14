from flask import Blueprint, request
from pet_hotel.models import Owner

check_in_bp = Blueprint('check-in', __name__, url_prefix='/check-in')


@check_in_bp.route('/', methods=['POST'])
@check_in_bp.route('', methods=['POST'])
def check_in():
    return 'success'


@check_in_bp.route('/owners')
def owners():
    resp = Owner.query.all()
    return resp
