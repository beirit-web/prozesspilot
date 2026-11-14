from email_model import Email
from email_data import emails


def naechste_id(ids):
    if ids == []:
        neue_id = 1
    else:
        neue_id = max(ids) + 1

    return neue_id


def felder_ausfuehlen(email):
    email.betreff = email.betreff.strip()
    email.inhalt = email.inhalt.strip()

    while not email.betreff:
        email.betreff = input("Betreff fehlt: ").strip()

    while not email.inhalt:
        email.inhalt = input("Inhalt fehlt: ").strip()


def email_adresse_validieren(email):
    adresse = email.deine_email_adr

    if isinstance(adresse, str) and "@" in adresse:
        return True

    return False


def email_validieren(email):
    if type(email.id) is int and email.id >= 1:
        if email_adresse_validieren(email):
            if (
                isinstance(email.betreff, str)
                and email.betreff.strip()
                and isinstance(email.inhalt, str)
                and email.inhalt.strip()
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


def main():
    print("ProzessPilot gestartet")

    # Neue E-Mail erstellen
    deine_email_adr = input("Deine E-Mail: ").strip()
    betreff_eingabe = input("Betreff: ").strip()
    inhalt = input("Inhalt: ").strip()

    print("---------")

    # Vorhandene IDs sammeln
    ids = []

    for vorhandene_email in emails:
        ids.append(vorhandene_email.id)

    # Nächste ID ermitteln
    neue_id = naechste_id(ids)

    # E-Mail-Objekt erstellen
    email_inhalt = Email(
        neue_id,
        deine_email_adr,
        betreff_eingabe,
        inhalt
    )

    # Eingaben überprüfen und korrigieren
    felder_ausfuehlen(email_inhalt)

    # E-Mail speichern
    email_speichern(email_inhalt)

    # Ergebnisse ausgeben
    print("---------")
    print("Alle IDs:", [email.id for email in emails])
    print("Betreff:", email_inhalt.betreff)
    print("Hinzugefügte ID:", email_inhalt.id)

    print("---------")
    print("Neue E-Mail gültig:", email_validieren(email_inhalt))
    print("Anzahl E-Mails:", len(emails))

    if len(emails) >= 3:
        print(
            "Dritte E-Mail gültig:",
            email_validieren(emails[2])
        )
    else:
        print("Dritte E-Mail gibt's nicht")


if __name__ == "__main__":
    main()
