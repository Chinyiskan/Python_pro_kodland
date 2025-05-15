from flask import Flask, render_template, request, send_file
import tempfile
import os

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
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    # Crear archivo temporal con los datos
    temp = tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt')
    temp.write(f"Nombre: {name}\nCorreo electrónico: {email}\nDirección: {address}\nFecha: {date}\n")
    temp.close()

    # Guardar la ruta temporal en una variable de sesión o pasarla como parámetro
    filename = temp.name

    # Mostrar la página de resultado y pasar la ruta del archivo
    return render_template('form_result.html', name=name, email=email, address=address, date=date, filename=filename)

@app.route('/download/<path:filename>')
def download_file(filename):
    # Seguridad: solo permite descargar archivos temporales
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True, download_name='formulario.txt', mimetype='text/plain')
    else:
        return "Archivo no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)