"""
this porgram update helps to the user improving new activities verification 
and  a new structured menu, where the clients and the new users could move
as they want  with any requirements that they have.

Author: Nicolas Avendaño Barajas
"""



from flask import Flask, request, jsonify

app = Flask(__name__)

# Servicio para agregar un nuevo motor
@app.route('/add_engine', methods=['POST'])
def add_engine():
    data = request.json
    # Aquí iría la lógica para agregar el motor a la base de datos
    # Supongamos que se agregó con éxito
    return jsonify({'status': 'success', 'message': 'Engine added successfully'})

# Servicio para agregar un nuevo vehículo
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    data = request.json
    # Aquí iría la lógica para agregar el vehículo a la base de datos
    # Supongamos que se agregó con éxito
    return jsonify({'status': 'success', 'message': 'Vehicle added successfully'})

# Servicio para obtener todos los motores
@app.route('/all_engines', methods=['GET'])
def get_all_engines():
    # Aquí iría la lógica para obtener todos los motores de la base de datos
    # Supongamos que los motores se recuperan con éxito
    engines = [
        {'id': 1, 'model': 'Engine Model 1', 'fuel_type': 'Gasoline', 'power': 200},
        {'id': 2, 'model': 'Engine Model 2', 'fuel_type': 'Diesel', 'power': 250}
    ]
    return jsonify(engines)

# Servicio para obtener todos los vehículos
@app.route('/all_vehicles', methods=['GET'])
def get_all_vehicles():
    # Aquí iría la lógica para obtener todos los vehículos de la base de datos
    # Supongamos que los vehículos se recuperan con éxito
    vehicles = [
        {'id': 1, 'make': 'Toyota', 'model': 'Corolla', 'year': 2022, 'engine_id': 1},
        {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2021, 'engine_id': 2}
    ]
    return jsonify(vehicles)

if __name__ == '__main__':
    app.run(debug=True)
