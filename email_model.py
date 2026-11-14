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
