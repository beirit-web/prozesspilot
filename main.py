
emails = [
    {
        "id": 1,
        "deine_email": "example@email.de",
        "betreff": "Test",
        "inhalt": "Hallo ich bin 1",
    },
    {
        "id": 2,
        "deine_email": "example@email.de",
        "betreff": "Test",
        "inhalt": "Hallo ich bin 2",
    },
    {
        "id": 3,
        "betreff": "Test",
        "inhalt": "Hallo ich bin 3",
    },
]

deine_email = input("Deine E-Mail: ").strip()
betreff_eingabe = input("Betreff: ").strip()
inhalt = input("Inhalt: ").strip()

print("---------")

ids = []

for vorhandene_email in emails:
    ids.append(vorhandene_email["id"])


def naechste_id(ids):
    if ids == []:
        neue_id = 1
    else:
        neue_id = max(ids) + 1

    return neue_id


neue_id = naechste_id(ids)

print(f"Neue ID: {neue_id}")
print("---------")

email_inhalt = {
    "id": neue_id,
    "deine_email": deine_email,
    "betreff": betreff_eingabe,
    "inhalt": inhalt,
}


def felder_ausfuehlen(werte):
    for k, v in werte.items():

        # Leerzeichen bei Strings entfernen
        if isinstance(werte[k], str):
            werte[k] = werte[k].strip()

        # Eingaben überprüfen
        while not werte[k] or (
            k == "deine_email" and "@" not in werte[k]
        ):
            if not werte[k]:
                werte[k] = input(
                    f"{k} bitte erneut eingeben, es fehlt: "
                ).strip()
            else:
                werte[k] = input(
                    f"{k} erneut mit '@' eingeben: "
                ).strip()

    return True


def email_speichern(email):
    if felder_ausfuehlen(email):
        emails.append(email)
        ids.append(email["id"])

    if len(emails) == 1:
        print(f"Im Postfach ist: {len(emails)} E-Mail")
    else:
        print(f"Im Postfach sind: {len(emails)} E-Mails")


email_speichern(email_inhalt)

print("Alle IDs:", ids)
print("Betreff:", email_inhalt["betreff"])
print("Hinzugefügte ID:", email_inhalt["id"])
