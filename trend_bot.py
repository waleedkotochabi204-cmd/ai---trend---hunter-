import os
import requests
import google.generativeai as genai

# Connexion aux coffres-forts (Secrets)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configuration de l'IA Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_trends():
    # Ici, on simule la récupération des titres du Top Oricon / Natalie
    # Dans la prochaine étape, on y ajoutera un vrai "scraper"
    raw_data = "Nouveaux titres populaires au Japon: [Ichi the Witch, Ogre Bride adaptation, Kagurabachi Volume 3]"
    return raw_data

def analyze_with_ai(data):
    prompt = f"""
    Analyse ces tendances de mangas/animés japonais : {data}
    1. Traduis les titres en français.
    2. Pour chaque titre, explique en une phrase pourquoi il pourrait devenir viral en Europe ou en Afrique.
    3. Donne un 'Score de Hype' sur 10.
    Sois bref et percutant.
    """
    response = model.generate_content(prompt)
    return response.text

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

# Lancement du processus
if __name__ == "__main__":
    print("Analyse en cours...")
    data = get_trends()
    report = analyze_with_ai(data)
    send_telegram(f"🚀 **RAPPORT TENDANCES JAPON** 🚀\n\n{report}")
    print("Rapport envoyé sur Telegram !")
