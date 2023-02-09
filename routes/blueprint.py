from flask import Blueprint
from controller.readcsv import *
from controller.writecsv import *

blueprint = Blueprint('blueprint', __name__)

#READ 
blueprint.route('/read_by_row/csv', methods=['GET'])(read_by_row_csv_main)
blueprint.route('/read/csv', methods=['GET'])(read_csv_main)
blueprint.route('/write/csv', methods=['GET'])(write_csv_main)