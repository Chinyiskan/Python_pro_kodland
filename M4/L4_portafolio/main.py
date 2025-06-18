# Import
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_path = os.path.join(app.root_path, 'instance', 'feedback.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Cambia esto en producción

db = SQLAlchemy(app)

# Modelo para feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)

# Página principal (GET)
@app.route('/')
def index():
    return render_template('index.html')

# Procesar formulario de feedback (POST)
@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form.get('email')
    text = request.form.get('text')
    if not email or not text:
        flash('Por favor, completa todos los campos.', 'error')
        return redirect('/')
    nuevo_feedback = Feedback()
    nuevo_feedback.email = email
    nuevo_feedback.text = text
    db.session.add(nuevo_feedback)
    db.session.commit()
    flash('¡Gracias por tu comentario!', 'success')
    return redirect('/')

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    # Crear la carpeta instance si no existe
    instance_dir = os.path.join(app.root_path, 'instance')
    if not os.path.exists(instance_dir):
        os.makedirs(instance_dir)
    # Crear la base de datos si no existe
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
