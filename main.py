emails = [
    {
        "id": 21,
        "absender": "kunde@beispiel.de",
        "betreff": "Anfrage zur Bestellung",
        "inhalt": "Guten Tag, ich möchte wissen, wann meine Bestellung geliefert wird.",
        "status": "neu"
    },
    {
        "id": 2,
        "absender": "kunde@beispiel.de",
        "betreff": "Frage zu den Öffnungszeiten",
        "inhalt": "Guten Tag, ich möchte wissen, wann meine Bestellung geliefert wird.",
        "status": "neu"
    },
    {
        "id": 3,
        "absender": "kunde@beispiel.de",
        "betreff": "Rechnung für Oktober",
        "inhalt": "Guten Tag, ich möchte wissen, wann meine Bestellung geliefert wird.",
        "status": "neu"
    },
    {
        "absender": "kunde@beispiel.de",
        "betreff": "Änderung der Bestellung",
        "inhalt": "Guten Tag, ich möchte wissen, wann meine Bestellung geliefert wird.",
        "status": "neu"
    },
]


# E-Mail-Klassifizierung
def email_analysieren(email):
    betreff = email.get("betreff", "").lower()

    if "bestellung" in betreff:
        return "Bestellung"
    elif "rechnung" in betreff:
        return "Rechnung"
    else:
        return "Allgemein"


for nummer, email in enumerate(emails, start=1):
    if "id" not in email:
        email['id'] = nummer
    print(
        f"Email {email.get('id', nummer)} Betreff {email_analysieren(email)}")
