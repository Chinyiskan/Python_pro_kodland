# Importar las librerías necesarias de Flask
from flask import Flask, render_template, request, redirect
# Importar la extensión para bases de datos SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Crear la aplicación Flask
app = Flask(__name__)
# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializar la base de datos con la app
# Esto permite usar db.Model para crear tablas
# y db.session para interactuar con la base de datos
# (agregar, consultar, modificar, eliminar datos)
db = SQLAlchemy(app)

# Definir la tabla Card para las entradas del diario
class Card(db.Model):
    # id: identificador único de cada tarjeta
    id = db.Column(db.Integer, primary_key=True)
    # title: título de la tarjeta
    title = db.Column(db.String(100), nullable=False)
    # subtitle: descripción corta
    subtitle = db.Column(db.String(300), nullable=False)
    # text: contenido principal de la tarjeta
    text = db.Column(db.Text, nullable=False)

    # Representación de la tarjeta (útil para depuración)
    def __repr__(self):
        return f'<Card {self.id}>'
    
#Asignación #2. Crear la tabla Usuario
# Definir la tabla User para los usuarios registrados
class User(db.Model):
    # id: identificador único de usuario
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # login: correo electrónico del usuario
    login = db.Column(db.String(100),  nullable=False)
    # password: contraseña del usuario
    password = db.Column(db.String(30), nullable=False)

# Ruta principal: login de usuario
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            # Obtener datos del formulario
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Asignación #4. Aplicar la autorización
            # Buscar usuario con ese login y contraseña
            user = User.query.filter_by(login=form_login, password=form_password).first()
            if user:
                # Si existe, redirigir a la página principal
                return redirect('/index')
            else:
                # Si no existe, mostrar error
                error = 'Nombre de usuario o contraseña incorrectos'
            return render_template('login.html', error=error)

        else:
            # Si es GET, mostrar el formulario de login
            return render_template('login.html')

# Ruta de registro de usuario
@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        # Obtener datos del formulario
        login= request.form['email']
        password = request.form['password']
        
        #Asignación #3. Hacer que los datos del usuario se registren en la base de datos.
        # Verificar si el usuario ya existe
        existing_user = User.query.filter_by(login=login).first()
        if existing_user:
            error = 'El usuario ya existe'
            return render_template('registration.html', error=error)
        # Crear nuevo usuario y guardar en la base de datos
        user = User()
        user.login = login
        user.password = password
        db.session.add(user)
        db.session.commit()

        # Redirigir al login después de registrarse
        return redirect('/')
    
    else:    
        # Si es GET, mostrar el formulario de registro
        return render_template('registration.html')

# Página principal después de iniciar sesión
@app.route('/index')
def index():
    # Visualización de las entradas de la base de datos
    # Consulta todas las tarjetas ordenadas por id
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Página para ver una tarjeta específica
@app.route('/card/<int:id>')
def card(id):
    # Buscar la tarjeta por id
    card = Card.query.get(id)
    return render_template('card.html', card=card)

# Página para mostrar el formulario de creación de tarjeta
@app.route('/create')
def create():
    return render_template('create_card.html')

# El formulario de inscripción de nuevas tarjetas
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        # Obtener datos del formulario
        title =  request.form['title']
        subtitle = request.form['subtitle']
        text = request.form['text']

        # Creación de un objeto que se enviará a la base de datos
        card = Card()
        card.title = title
        card.subtitle = subtitle
        card.text = text

        db.session.add(card)
        db.session.commit()
        # Redirigir a la página principal después de crear la tarjeta
        return redirect('/index')
    else:
        # Si es GET, mostrar el formulario de creación
        return render_template('create_card.html')

# Ejecutar la aplicación en modo debug
if __name__ == "__main__":
    app.run(debug=True)
