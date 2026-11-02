# Projektstadt

Projektverwaltung als 3D-Stadt (Three.js), gebaut als Claude-Artifact (`projektstadt.html`).

- Jedes Projekt steht auf einem eigenen Grundstück. Jeder Schritt ist ein Stockwerk.
- Laufende Projekte sind Baustellen mit Gerüst, Kran und Bauzaun. Fertige Projekte bekommen ein Dach, abgebrochene bleiben als Ruine stehen.
- Projekttypen: 3D-Druck (Werkstatt), App (Glasturm), Website (Wohnhaus), Video & Content (Studio), Allgemein (Stadthaus).
- Ein Klick auf ein Stockwerk zoomt auf das Gebäude und öffnet rechts die Details zu diesem Schritt: Notizen, Checkliste, Links, Bilder und bei 3D-Druck STL-Dateien mit 3D-Vorschau.
- Tag und Nacht folgen automatisch der Berliner Uhrzeit (Sonnenstand).
- Gespeichert wird im privaten Speicher des Artifacts (nur für den Besitzer). Außerhalb von claude.ai läuft die Seite mit localStorage. JSON-Export und -Import sind eingebaut.
- Fertige Projekte lassen sich wieder eröffnen, um einen weiteren Schritt einzubauen. Das Gebäude wird dann wieder zur Baustelle.
- „Update ab diesem Stockwerk“ startet eine neue Version: Alle Stockwerke ab dort werden erneut durchlaufen. Sie stehen so lange unter einer grünen Plane und bekommen nach der Erneuerung ein farbiges Versionsband. Der Stand früherer Versionen bleibt je Stockwerk erhalten.
