emails = [
    # {
    #     "id": 1,
    #     "empfaenger_email": "example@email.de",
    #     "betreff": "Test",
    #     "inhalt": "Hallo ich bin 1",
    # },
    # {
    #     "id": 2,
    #     "empfaenger_email": "example@email.de",
    #     "betreff": "Test",
    #     "inhalt": "Hallo ich bin 2",
    # },
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
    print("Liste ist noch leer")
    print("---------")
else:
    hinzugefuegte_id = max(ids) + 1
    print("Neue ID:", hinzugefuegte_id)

email_inhalt = {
    "id": hinzugefuegte_id,
    "empfaenger_email": deine_email,
    "betreff": betreff_eingabe,
    "inhalt": inhalt,
}
emails.append(email_inhalt)
ids.append(email_inhalt["id"])

if len(emails) == 1:
    print(f"In der Liste ist {len(emails)} E-Mail")
elif len(emails) > 1:
    print(f"In der Liste sind {len(emails)} E-Mails")
else:
    print("Die Liste ist leer")
print("---------")
print("Alle ID's:", ids)
print("Hinzugefügte ID:", hinzugefuegte_id)
