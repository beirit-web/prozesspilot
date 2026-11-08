# ProzessPilot – aktueller Projektstand

**Stand: 8. November 2026**

Dieses Dokument beschreibt den tatsächlich vorhandenen lokalen Projektstand und erklärt die derzeitige Ordnerstruktur. Es ergänzt die [README.md](README.md), die überwiegend die geplante Entwicklung beschreibt. Die unten genannten Verbesserungen sind Empfehlungen und noch nicht umgesetzt.

## 1. Überblick

ProzessPilot ist ein Python-Lernprojekt zur schrittweisen Automatisierung von Geschäftsabläufen. Aktuell besteht die Hauptanwendung aus einem Konsolenskript zur Erfassung und Prüfung von E-Mail-Daten.

Im Arbeitsverzeichnis liegen zusätzlich ein eigenständiger TicketManager, ein lokales SMTP-Versandskript und Übungsdateien. Zwischen E-Mail-Erfassung, TicketManager und Versand gibt es derzeit keine programmatische Verbindung.

| Bereich | Aktueller Stand |
| --- | --- |
| E-Mail-Erfassung | Interaktive Eingabe von Adresse, Betreff und Inhalt |
| E-Mail-Validierung | Prüfung von Pflichtfeldern, ID, Textwerten und Vorhandensein eines `@` |
| ID-Vergabe | Höchste vorhandene ID plus eins; Start bei eins für eine leere Liste |
| Speicherung | E-Mails und Tickets bleiben nur während der Ausführung im Arbeitsspeicher |
| TicketManager | Tickets erstellen, filtern, abschließen, prüfen und statistisch auswerten |
| E-Mail-Versand | Separates lokales SMTP-Skript mit Gmail-Anbindung |
| Automatisierte Tests | Keine Testsuite vorhanden |
| API, Weboberfläche und KI | Noch nicht implementiert |

## 2. Derzeitige Projektstruktur

Der folgende Baum zeigt die wesentlichen lokalen Dateien. Git-Inhalte, installierte Pakete und weitere interne Dateien sind zusammengefasst. Lokale, von Git ignorierte Dateien sind ebenfalls aufgeführt; sie sind deshalb nicht automatisch Bestandteil eines frischen Klons.

```text
ProzessPilot/
├── AKt-Stand-README.md             # Diese Bestandsaufnahme
├── README.md                      # Projektidee und geplante Entwicklung
├── LICENSE                        # Lizenz des Hauptprojekts
├── Plan.txt                       # Lokale Roadmap, von Git ignoriert
├── main.py                        # E-Mail-Erfassung und Validierung
├── send_mail.py                   # Lokales SMTP-Skript, von Git ignoriert
├── test.py                        # Auskommentierte Übungen, von Git ignoriert
├── .gitignore                     # Ausschlussregeln des Hauptprojekts
├── .env                           # Lokale Konfiguration, von Git ignoriert
├── .venv/                         # Lokale virtuelle Python-Umgebung
├── .git/                          # Git-Verwaltung von ProzessPilot
├── __pycache__/                   # Generierter Python-Bytecode
│   └── main.cpython-313.pyc
├── assets/
│   └── svg/
│       ├── banner.svg             # Grafik für die Haupt-README
│       └── architektur.svg        # Darstellung der geplanten Architektur
├── daten/
│   └── emails.json                # Enthält derzeit eine leere Liste: []
└── ticket-manager/                # Eigenständiges, verschachteltes Git-Repository
    ├── .git/                      # Eigene Git-Verwaltung des TicketManagers
    ├── .gitignore                 # Ignoriert die lokale Datei .task.py
    ├── .task.py                   # Lokale, derzeit leere Datei
    ├── README.md                  # Beschreibung des TicketManagers
    ├── LICENSE                    # Lizenz des TicketManagers
    ├── ticket.manager.py          # Aktuell vorhandenes Ticket-Skript
    └── ticket-manager/
        └── assets/               # Banner, Badges und Footer der Ticket-README
```

Die lokalen Verzeichnisse `.agents/`, `.codex/` und `.aws/` sind in dieser Übersicht ausgelassen. Die untersuchten Anwendungsskripte greifen nicht darauf zu.

### Hauptanwendung: main.py

[main.py](main.py) enthält derzeit die gesamte E-Mail-Anwendung in einer Datei:

- Drei fest eingetragene Beispieldatensätze; beim dritten fehlt die E-Mail-Adresse.
- `naechste_id()` berechnet die nächste ID.
- `felder_ausfuehlen()` bereinigt Eingaben und fragt bei leeren Werten oder fehlendem `@` erneut nach. Der Funktionsname ist im aktuellen Code so geschrieben.
- `email_adresse_validieren()` prüft, ob die Adresse ein String ist und ein `@` enthält.
- `email_validieren()` prüft die Pflichtfelder, eine positive ganzzahlige ID sowie nicht leeren Betreff und Inhalt.
- `email_speichern()` ergänzt gültige Datensätze in der globalen Liste `emails` und gibt Meldungen aus.

Der Ablauf ist: **Eingabe → ID vergeben → Eingaben korrigieren → Datensatz prüfen → Liste ergänzen → Ergebnisse ausgeben.**

Die Bezeichnung „speichern“ bedeutet hier ausschließlich das Anhängen an eine Python-Liste. Es wird keine Datei geschrieben. Nach dem Beenden gehen neu erfasste Daten verloren.

### Daten und Grafiken

[daten/emails.json](daten/emails.json) ist bereits angelegt, wird aber von `main.py` weder gelesen noch beschrieben. Die verwendeten Beispieldaten stehen direkt im Python-Code.

Unter `assets/svg/` liegen Dokumentationsgrafiken. Die Architekturgrafik beschreibt die geplante Entwicklung und ist kein Nachweis bereits implementierter Komponenten.

### TicketManager

[ticket-manager/ticket.manager.py](ticket-manager/ticket.manager.py) ist eine separate Konsolenanwendung mit einer eigenen Liste `tickets`.

| Funktion | Aufgabe |
| --- | --- |
| `kritische_tickets()` | Offene Tickets mit hoher Priorität auswählen |
| `ticket_abschliessen()` | Ein Ticket anhand seiner ID suchen und von `offen` auf `erledigt` setzen |
| `ticket_statistik()` | Gesamtzahl, offene und erledigte Tickets, hohe Priorität sowie fehlenden Status zählen |
| `ticket_validieren()` | Vorhandensein der Schlüssel `id`, `titel` und `status` prüfen |
| `ticket_erstellen()` | Eine ID vergeben und ein neues Ticket mit Status `offen` hinzufügen |

Beim Start werden zwei Beispieltickets erstellt, eines abgeschlossen und Statistik sowie Validierungsergebnisse ausgegeben. Eine interaktive Menüführung oder dauerhafte Speicherung gibt es noch nicht. Die Funktion zum Filtern kritischer Tickets ist vorhanden, wird im Beispielablauf aber nicht aufgerufen.

Der zusätzliche Unterordner `ticket-manager/ticket-manager/` enthält nur die Dokumentationsgrafiken. Er stellt keine weitere Anwendungsschicht dar.

### Lokaler Versand und Übungen

`send_mail.py` erstellt eine Testnachricht und versucht, sie über Gmail-SMTP zu versenden. Das Skript verwendet `python-dotenv`, liest `GMAIL_APP_PASSWORD` aus der Umgebung beziehungsweise einer `.env`-Datei und enthält feste Absender- und Empfängerangaben. Es behandelt Authentifizierungs-, SMTP- und Verbindungsfehler. Es wird von `main.py` nicht aufgerufen.

**Das Versandskript kann beim Ausführen oder Importieren eine echte Nachricht versenden, wenn die Konfiguration gültig ist.** Es gehört deshalb nicht zum unten beschriebenen Start der lokalen E-Mail-Erfassung. Die Inhalte der `.env` wurden für diese Bestandsaufnahme nicht ausgelesen.

`test.py` enthält auskommentierte Lernbeispiele zu Fehlerbehandlung und Klassen. Die Datei ist keine automatisierte Testsuite.

## 3. Anwendungen lokal starten

Für die E-Mail-Erfassung und den TicketManager reicht Python 3; beide Skripte benötigen derzeit keine externen Pakete. Die Befehle werden im Hauptverzeichnis `ProzessPilot/` ausgeführt.

E-Mail-Erfassung starten:

```bash
python3 main.py
```

Anschließend Adresse, Betreff und Inhalt eingeben. Bei den vorhandenen Beispieldaten erhält die neu erfasste E-Mail die ID `4`. Der dritte Beispieldatensatz wird wegen seiner fehlenden Adresse als ungültig ausgegeben.

TicketManager-Beispiel starten:

```bash
python3 ticket-manager/ticket.manager.py
```

Eine `pyproject.toml` oder `requirements.txt` zur Deklaration von Python-Version und Abhängigkeiten ist noch nicht vorhanden. Das zusätzliche SMTP-Skript benötigt das externe Paket `python-dotenv`.

## 4. Git-Struktur und Dokumentationsstand

Diese Angaben sind eine Momentaufnahme zum oben genannten Datum:

- Das Hauptrepository versioniert unter anderem `main.py`, `README.md`, die Grafiken und `daten/emails.json`.
- Die Haupt-`.gitignore` schließt `Plan.txt`, `test.py`, `send_mail.py`, `.venv`, `.env` und `__pycache__/` aus.
- `__pycache__/main.cpython-313.pyc` wird trotzdem bereits von Git verfolgt. Eine Ignore-Regel entfernt zuvor aufgenommene Dateien nicht aus dem Git-Index.
- `ticket-manager/` hat ein eigenes `.git`-Verzeichnis. Im Hauptrepository erscheint der Ordner als unversioniert; er ist dort nicht als Submodul eingerichtet.
- Im TicketManager-Repository wird die zuvor versionierte `main.py` als lokal gelöscht angezeigt, während `ticket.manager.py` unversioniert ist. Die Änderung des Skriptpfads ist dort noch nicht als Commit festgehalten.
- Die Haupt-README beschreibt die Anwendung noch als nicht ausführbar, obwohl die interaktive E-Mail-Erfassung bereits vorhanden ist.
- Die TicketManager-README nennt noch `python main.py`; zum aktuellen lokalen Dateinamen passt der Startbefehl aus Abschnitt 3.
- `Plan.txt` verwendet noch den Projektnamen „MailFlow AI“ und führt bereits teilweise erledigte Schritte als offen. Die Datei ist in der Haupt-README verlinkt, wird aber nicht versioniert.

## 5. Bekannte Grenzen des aktuellen Codes

1. **Eingabe und Fachlogik sind gekoppelt.** Funktionen zur Datenprüfung enthalten teilweise `input()`, während die Speicherung `print()` verwendet und eine globale Liste verändert.
2. **Programmcode läuft beim Import.** Ein `if __name__ == "__main__":`-Einstieg fehlt in den Anwendungsskripten. Das erschwert die isolierte Wiederverwendung und Tests.
3. **Die Adressprüfung ist sehr einfach.** Schon `"@"` wird als gültige E-Mail-Adresse akzeptiert.
4. **Die Ticketprüfung kontrolliert nur Schlüssel.** Leere Titel, `id=None` und unbekannte Statuswerte können die Prüfung bestehen. Auch die Ticketerstellung prüft Titel und Priorität nicht.
5. **Unbekannte Ticketstatus werden nicht eindeutig behandelt.** Beim Abschluss gilt jeder vorhandene Status außer `offen` als bereits erledigt. In der Statistik werden unbekannte, nicht leere Statuswerte keiner Statuskategorie zugeordnet.
6. **Rückgabewerte sind uneinheitlich.** `ticket_abschliessen()` liefert je nach Ergebnis ein Dictionary oder einen Meldungstext.
7. **Dauerhafte Speicherung und automatisierte Qualitätssicherung fehlen.** Es gibt weder JSON-Lade-/Speicherfunktionen noch eine Testsuite oder eine CI-Konfiguration.

Noch nicht umgesetzt sind außerdem E-Mail-Kategorisierung, E-Mail-Priorisierung, Duplikaterkennung, ein zentraler Verarbeitungsablauf, Anwendungslogging, eine Datenbank, eine REST-API und KI-Funktionen.

## 6. Empfohlene nächste Schritte

Die vorhandene Anwendung kann schrittweise verbessert werden:

1. Startcode in `main()` und einen geschützten Programmeinstieg verschieben.
2. Tests für Validierung, ID-Vergabe und Ticketstatus ergänzen; bekannte Randfälle ausdrücklich abdecken.
3. Konsoleneingaben, Fachlogik und Speicherung in kleine Module trennen.
4. JSON laden und speichern sowie Fehlerfälle bei der Dateiverarbeitung behandeln.
5. Git-Regeln, Dateinamen und Dokumentation mit dem tatsächlichen Stand abstimmen.
6. Entscheiden, ob der TicketManager eigenständig bleibt oder fachlich in ProzessPilot integriert wird.
7. Python-Version und Abhängigkeiten deklarieren und anschließend automatisierte Prüfungen ergänzen.

Für den aktuellen Umfang genügt eine Anwendung mit klar getrennten Python-Modulen. API, Datenbank und mögliche Microservices können folgen, sobald der grundlegende Ablauf zuverlässig funktioniert.

## 7. Grundlage dieser Bestandsaufnahme

Die Aussagen beruhen auf der Prüfung der lokalen Dateien, beider Git-Arbeitsverzeichnisse und ausgewählter Funktionsaufrufe mit Randfällen. Die Syntax von `main.py`, `send_mail.py`, `test.py` und `ticket-manager/ticket.manager.py` wurde erfolgreich geprüft. Eine vollständige automatisierte Testsuite existiert noch nicht. SMTP-Versand und Netzwerkzugriffe wurden nicht ausgeführt.
