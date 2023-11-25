from flask import Blueprint, render_template,request

from utils import *

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/', methods = ['GET'])
def index_b():
    return "Hello World!"
    #return render_template('index.html')
