emails = [
    {
        "id": 1,
        "deine_email_adr": "example@email.de",
        "betreff": "Test",
        "inhalt": "Hallo ich bin 1",
    },
    {
        "id": 2,
        "deine_email_adr": "example@email.de",
        "betreff": "Test",
        "inhalt": "Hallo ich bin 2",
    },
    {
        "id": 3,
        "betreff": "Test",
        "inhalt": "Hallo ich bin 3",
    },
]


def naechste_id(ids):
    if ids == []:
        neue_id = 1
    else:
        neue_id = max(ids) + 1

    return neue_id


def felder_ausfuehlen(werte):
    for k, v in werte.items():

        if isinstance(v, str):
            werte[k] = v.strip()

        while not werte[k] or (
            k == "deine_email_adr"
            and "@" not in werte[k]
        ):
            if not werte[k]:
                werte[k] = input(
                    f"{k} erneut eingeben: "
                ).strip()
            else:
                werte[k] = input(
                    f"{k}: @-Zeichen fehlt: "
                ).strip()

    return True


def email_adresse_validieren(email):
    adresse = email.get("deine_email_adr")

    if isinstance(adresse, str) and "@" in adresse:
        return True

    return False


def email_validieren(email):

    # Prüfen, ob alle Schlüssel vorhanden sind
    if (
        "id" in email
        and "deine_email_adr" in email
        and "betreff" in email
        and "inhalt" in email
    ):

        # ID überprüfen
        if (
            type(email["id"]) is int
            and email["id"] >= 1
        ):

            # E-Mail-Adresse überprüfen
            if email_adresse_validieren(email):

                # Betreff überprüfen
                if (
                    isinstance(email.get("betreff"), str)
                    and email.get("betreff").strip()
                ):

                    # Inhalt überprüfen
                    if (
                        isinstance(email.get("inhalt"), str)
                        and email.get("inhalt").strip()
                    ):
                        return True

    return False


def email_speichern(email):

    if email_validieren(email):
        emails.append(email)
        print("E-Mail erfolgreich gespeichert.")
    else:
        print("E-Mail ist ungültig und wurde nicht gespeichert.")

    if len(emails) == 1:
        print(f"Im Postfach ist: {len(emails)} E-Mail")
    else:
        print(f"Im Postfach sind: {len(emails)} E-Mails")


# Neue E-Mail erstellen
deine_email_adr = input("Deine E-Mail: ").strip()
betreff_eingabe = input("Betreff: ").strip()
inhalt = input("Inhalt: ").strip()

print("---------")

ids = []

for vorhandene_email in emails:
    ids.append(vorhandene_email["id"])

neue_id = naechste_id(ids)

email_inhalt = {
    "id": neue_id,
    "deine_email_adr": deine_email_adr,
    "betreff": betreff_eingabe,
    "inhalt": inhalt,
}

# Eingaben überprüfen und gegebenenfalls korrigieren
felder_ausfuehlen(email_inhalt)

# E-Mail speichern
email_speichern(email_inhalt)

print("---------")
print("Alle IDs:", [email["id"] for email in emails])
print("Betreff:", email_inhalt["betreff"])
print("Hinzugefügte ID:", email_inhalt["id"])

print("---------")
print("Neue E-Mail gültig:", email_validieren(email_inhalt))
print("Dritte E-Mail gültig:", email_validieren(emails[2]))
