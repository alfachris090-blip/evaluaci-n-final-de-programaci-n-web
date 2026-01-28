from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/calcular_total', methods=['POST'])
def calcular_total():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    cantidad_tarros = int(request.form['cantidad_tarros'])

    precio_por_tarro = 9000
    total_sin_descuento = cantidad_tarros * precio_por_tarro
    descuento = 0

    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25

    total_con_descuento = total_sin_descuento * (1 - descuento)

    return f"Nombre: {nombre}<br>Total sin descuento: ${total_sin_descuento}<br>Total a pagar: ${total_con_descuento}"

@app.route('/validar_login', methods=['POST'])
def validar_login():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    if usuario == "juan" and contrasena == "admin":
        return "Bienvenido administrador juan"
    elif usuario == "pepe" and contrasena == "user":
        return "Bienvenido usuario pepe"
    else:
        return "Credenciales incorrectas. Inténtalo de nuevo."

if __name__ == '__main__':
    app.run(debug=True)