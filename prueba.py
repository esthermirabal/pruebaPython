from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/prueba'
db = SQLAlchemy(app)


class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(20), nullable=False)
    modelo= db.Column(db.String(20), nullable=False)
    precio= db.Column(db.Float, nullable=False)

    def __init__(self, nombre, modelo, precio):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
    
#Agregar modelo de celular
@app.route('/prueba', methods=['POST'])
def agregar_modelo():
    data = request.get_json()
    nuevo_modelo = Modelo(
        nombre=data['nombre'],
        modelo=data['modelo'],
        precio=data['precio']
        )
    db.session.add(nuevo_modelo)
    db.session.commit()
    return jsonify({'message': 'Se agrego un modelo nuevo'}), 200


#Listar 
@app.route('/prueba', methods=['GET'])
def obtener_celulara():
    celular = Modelo.query.all()
    celular_json= [{'nombre': celular.nombre, 'modelo': celular.modelo, 'precio': celular.precio} for celular in celular]
    return jsonify(celular_json), 200

#Buscar
@app.route('/prueba/buscar', methods=['POST'])
def buscar_celular():
    data = request.get_json()
    id = data.get('id')
    if id:
        celular = Modelo.query.filter_by(id=id).first()
        if celular:
            celular_json= [{'nombre': celular.nombre, 'modelo': celular.modelo, 'precio': celular.precio}]
            return jsonify(celular_json), 200
    return jsonify({'mesage': 'No se encontro el modelo que buscabas'}), 404

#Modificar
@app.route('/prueba', methods=['PUT'])
def modificar_modelo():
    data = request.get_json()
    id = data.get('id')
    if id:
        celular = Modelo.query.filter_by(id=id).first()
        if celular:
            celular.nombre = data.get('nombre', celular.nombre)
            celular.apellido = data.get('modelo', celular.modelo)
            celular.precio = data.get('precio', celular.precio)
            db.session.commit()
            return jsonify({'mesage': 'Se han modificado los datos'}), 200
    return jsonify({'mesage': 'No se encontro el modelo que buscabas'}), 404

#Eliminar
@app.route('/prueba/<id>', methods=['DELETE'])
def eliminar_celular(id):
    celular = Modelo.query.filter_by(id=id).first()
    if celular:
        db.session.delete(celular)
        db.session.commit()        
        return jsonify({'mesage': 'Se han eliminado los datos'}), 200
    return jsonify({'mesage': 'No se encontro el modelo que buscabas'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
