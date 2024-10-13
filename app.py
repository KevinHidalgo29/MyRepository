from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://kevin:kevinr2beat@cluster0.teyaw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" 
mongo = PyMongo(app)

@app.route('/estudiantes', methods=['GET'])
def get_estudiantes():
    estudiantes = mongo.db.estudiantes.find()
    return jsonify([estudiante for estudiante in estudiantes])

@app.route('/estudiantes/<id>', methods=['GET'])
def get_estudiante(id):
    estudiante = mongo.db.estudiantes.find_one({"_id": id})
    return jsonify(estudiante)

@app.route('/estudiantes', methods=['POST'])
def create_estudiante():
    nuevo_estudiante = request.json
    mongo.db.estudiantes.insert_one(nuevo_estudiante)
    return jsonify(nuevo_estudiante), 201

@app.route('/estudiantes/<id>', methods=['PUT'])
def update_estudiante(id):
    estudiante_actualizado = request.json
    mongo.db.estudiantes.update_one({"_id": id}, {"$set": estudiante_actualizado})
    return jsonify(estudiante_actualizado)

@app.route('/estudiantes/<id>', methods=['DELETE'])
def delete_estudiante(id):
    mongo.db.estudiantes.delete_one({"_id": id})
    return jsonify({"result": "Estudiante eliminado"}), 204

if __name__ == '__main__':
    app.run(debug=True)
