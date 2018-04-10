from flask import render_template
from . import app

@route.app.errorhandler(404)
def four_Ow_four(error):
    """
    Function to render rhe 404 error page
    """
    return_render_template('four_Ow_four.html'), 404
    