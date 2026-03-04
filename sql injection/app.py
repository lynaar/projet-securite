from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="securite"
)

cursor = db.cursor()

# -------- LOGIN --------
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        # envoyer l'utilisateur vers le formulaire
        return render_template("form.html", user=username)
    else:
        return "Échec de connexion"
# -------- FORMULAIRE --------
@app.route('/submit', methods=['POST'])
def submit():
    username  = request.form['username']
    produit   = request.form['produit']
    quantite  = request.form['quantite']
    telephone = request.form['telephone']
    adresse   = request.form['adresse']
    livraison = request.form['livraison']
    note      = request.form.get('note', '')

    query = f"INSERT INTO messages (username, produit, quantite, telephone, adresse, livraison, note) VALUES ('{username}', '{produit}', {quantite}, '{telephone}', '{adresse}', '{livraison}', '{note}')"
    cursor.execute(query)
    db.commit()
    return "Commande enregistrée !"

if __name__ == '__main__':
    app.run(debug=True)
    

#----test inoutput-----' OR '1'='1
