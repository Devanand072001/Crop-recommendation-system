from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .predict import get_noutput
from .cropdetails import get_data

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', current_url=request.path)

@main.route('/predict', methods=['GET'])
def redirect_index():
    return redirect('/')

@main.route('/predict', methods=['POST', 'GET'])
def predict():
    v1 = float(request.form.get('temperature'))
    v2 = float(request.form.get('humidity'))
    v3 = float(request.form.get('ph'))
    v4 = float(request.form.get('rainfall'))
    v5 = float(request.form.get('water'))
    output = get_noutput(4, v1, v2, v3, v4, v5)
    print(output)
    return render_template('result.html', result=output)


@main.route('/crop/<crop>')
def crop_detail(crop):
    return render_template('crop.html', crop={'name': crop})


@main.route('/crop/<crop>/weather')
def crop_weather(crop):
    data = get_data(crop, 'weather')
    if not data:
        return render_template('crop.html', crop={'name': crop})
    return render_template('crop_detail/crop_weather.html', data=data)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

