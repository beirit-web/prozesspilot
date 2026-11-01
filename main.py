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

deine_email = input("Deine E-Mail: ")
betreff_eingabe = input("Betreff: ")
inhalt = input("Inhalt: ")

print("---------")
ids = []

for vorhandene_ids in emails:
    ids.append(vorhandene_ids["id"])

if ids == []:
    hinzugefuegte_id = 1
    print("Postfach ist noch leer")
    print("---------")
else:
    hinzugefuegte_id = max(ids) + 1
    print("Zulezt hinzugefügte ID:", hinzugefuegte_id)

email_inhalt = {
    "id": hinzugefuegte_id,
    "deine_email": deine_email,
    "betreff": betreff_eingabe,
    "inhalt": inhalt,
}


def felder_ausfuehlen(werte):
    for k, v in werte.items():
        while not werte[k] or (k == "deine_email" and not '@' in werte[k]):
            if not werte[k]:
                werte[k] = input(f"{k} bitte erneut eingeben: ")
            else:
                werte[k] = input(f"{k} erneut eingeben: ")
        return True


if felder_ausfuehlen(email_inhalt):
    emails.append(email_inhalt)
    ids.append(email_inhalt["id"])
    if len(emails) == 1:
        print(f"Postfach: {len(emails)} E-Mail")
    elif len(emails) > 1:
        print(f"Postfach: {len(emails)} E-Mails")

print("---------")
print("Alle ID's:", ids)
print("Nächste ID:", hinzugefuegte_id)
