class Email:
    def __init__(self, id, deine_email_adr,  betreff, inhalt):
        self.id = id
        self.deine_email_adr = deine_email_adr
        self.betreff = betreff
        self.inhalt = inhalt

    def email_info(self):
        return f"ID: {self.id} Deine Adrese: {self.deine_email_adr}, Betreff: {self.betreff} Inhalt: {self.inhalt}"

    def anzeigen(self):
        return self.betreff

    def betreff_aendern(self, neuer_betreff):
        neuer_betreff = neuer_betreff.strip()
        if neuer_betreff:
            self.betreff = neuer_betreff


# email1 = Email(1, "test@example.de", "Testbetreff", "Meine erste E-Mail",)
# print(email1.email_info())

email1 = Email(1, "test@example1.de", "Testbetreff", "Meine erste E-Mail",)

email2 = Email(2, "test@example2.de", "Bewerbung", "Test2")
print(email1.anzeigen())
print(email2.anzeigen())

email1.betreff_aendern("Neue Bewerbung")
print(email1.anzeigen())
