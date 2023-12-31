from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__)

# Beispiel-Liste von Döner-Optionen
doener_liste = [
    {'name': 'Döner Klassik', 'preis': 5.0},
    {'name': 'Döner mit Extra Fleisch', 'preis': 7.0},
    {'name': 'Vegetarischer Döner', 'preis': 4.5},
]

# Beispiel-Liste von Admins (zum Testen)
admins = ['admin1', 'admin2']

doener_liste = [
    {'name': 'Döner Klassik', 'preis': 5.0, 'saucen': ['Kräuter'], 'salate': ['Tomate']},
    {'name': 'Döner mit Extra Fleisch', 'preis': 7.0, 'saucen': ['Kräuter', 'Knoblauch'], 'salate': ['Tomate', 'Gurke']},
    {'name': 'Vegetarischer Döner', 'preis': 4.5, 'saucen': ['Kräuter', 'Scharf'], 'salate': ['Tomate', 'Gurke', 'Kopfsalat']},
]

# Authentifizierungsfunktion
def is_admin(username):
    return username in admins

@app.route('/doener', methods=['GET'])
def get_doener_list():
    return jsonify(doener_liste)

@app.route('/doener/<int:index>', methods=['GET'])
def get_doener_by_index(index):
    if 0 <= index < len(doener_liste):
        return jsonify(doener_liste[index])
    else:
        return jsonify({'error': 'Index nicht gefunden'}), 404

@app.route('/doener', methods=['POST'])
def add_doener():
    # Überprüfe, ob der Benutzer ein Admin ist
    username = request.authorization.get('username')
    if not is_admin(username):
        abort(401, description="Nicht autorisiert, um Döner hinzuzufügen.")

    # Füge neuen Döner hinzu
    new_doener = {'name': request.json.get('name'), 'preis': request.json.get('preis')}
    doener_liste.append(new_doener)

    return jsonify({'message': 'Döner erfolgreich hinzugefügt'}), 201

@app.route('/')
def index():
    # Rendere die index.html-Seite
    return render_template('index.html')
@app.route('/bestellungen', methods=['GET'])
def bestellungen_ansicht():
    return render_template('bestellungen.html', bestellungen=bestellungen)
# Liste zur Speicherung von Bestellungen
bestellungen = []

@app.route('/bestellen', methods=['POST'])
def bestellen():
    bestellDaten = {
        'doener': request.json.get('doener'),
        'saucen': request.json.get('saucen'),
        'salate': request.json.get('salate')
    }

    # Bestellung zur Liste hinzufügen
    bestellungen.append(bestellDaten)

    return jsonify({'message': 'Bestellung erfolgreich aufgegeben'}), 201

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
