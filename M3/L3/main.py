from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size: int, lights: int, devices: int) -> float:
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + devices * devices_coef

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/size/<int:size>')
def select_lights(size):
    return render_template('lights.html', size=size)

@app.route('/size/<int:size>/lights/<int:lights>')
def select_devices(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

@app.route('/size/<int:size>/lights/<int:lights>/devices/<int:devices>')
def show_result(size, lights, devices):
    result = result_calculate(size, lights, devices)
    return render_template('end.html', result=result)

# 🆕 NUEVA RUTA: mostrar formulario
@app.route('/form')
def form():
    return render_template('form.html')

# 🆕 NUEVA RUTA: procesar formulario
@app.route('/form/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    address = request.form['address']
    date = request.form['date']
    return render_template('form_result.html', name=name, address=address, date=date)

if __name__ == '__main__':
    app.run(debug=True)