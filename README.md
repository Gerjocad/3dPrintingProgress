# Projektstadt

Projektverwaltung als 3D-Stadt (Three.js), gebaut als Claude-Artifact (`projektstadt.html`).

- Jedes Projekt steht auf einem eigenen Grundstück. Jeder Schritt ist ein Stockwerk.
- Laufende Projekte sind Baustellen mit Gerüst, Kran und Bauzaun. Fertige Projekte bekommen ein Dach, abgebrochene bleiben als Ruine stehen.
- Projekttypen: 3D-Druck (Werkstatt), App (Glasturm), Website (Wohnhaus), Video & Content (Studio), Allgemein (Stadthaus).
- Ein Klick auf ein Stockwerk zoomt auf das Gebäude und öffnet rechts die Details zu diesem Schritt: Notizen, Checkliste, Links, Bilder, PDF-Dokumente (mit eingebautem Viewer) und bei 3D-Druck STL-Dateien mit 3D-Vorschau.
- Tag und Nacht folgen automatisch der Berliner Uhrzeit (Sonnenstand).
- Volltextsuche über alle Etagen (Notizen, Checklisten, Links, Dateinamen), Zeitleiste pro Projekt, Drag & Drop für Bilder/PDF/STL, STL-Vorschaubilder.
- MakerWorld-Link pro 3D-Druck-Projekt: Ein grünes Schild vor dem Gebäude öffnet das Modell. Überfällige Deadlines zeigen eine rote Fahne, bald fällige eine orange.
- Jahreszeiten nach Berliner Datum (Frühlingsblüten, Herbstlaub, Schnee im Winter) und Erfolge im Park bei 3, 10 und 25 fertigen Projekten.
- Gespeichert wird im privaten Speicher des Artifacts (nur für den Besitzer). Außerhalb von claude.ai läuft die Seite mit localStorage. Ein Komplett-Backup als ZIP (alle Daten und Dateien) lässt sich exportieren und wieder importieren, dazu reiner JSON-Export.
- Fertige Projekte lassen sich wieder eröffnen, um einen weiteren Schritt einzubauen. Das Gebäude wird dann wieder zur Baustelle.
- „Update ab diesem Stockwerk“ startet eine neue Version: Alle Stockwerke ab dort werden erneut durchlaufen. Sie stehen so lange unter einer grünen Plane und bekommen nach der Erneuerung ein farbiges Versionsband. Der Stand früherer Versionen bleibt je Stockwerk erhalten.
- **Anbau für Update:** Ein fertiges Projekt bekommt direkt daneben ein kleineres Update-Gebäude mit eigenen Schritten (bis zu 3 Anbauten: rechts, links, hinten).
- **Verzweigung:** Ab dem aktuellen Stockwerk teilt sich das Projekt in zwei Zweige. Über dem letzten fertigen Stockwerk entsteht eine breite Plattform auf Stützen, darauf wachsen zwei Türme mit eigenen Schritten. Zweig A übernimmt den bisherigen Stand, Zweig B startet frisch.
- Die Grundstücke sind größer, damit Anbauten und Zweige Platz haben. Wird ein Gebäude zu breit, wird es auf dem Grundstück passend verkleinert.

## Eigene Stadt für andere

Jede Person braucht eine eigene Kopie, denn die Daten einer Projektstadt gehören immer ihrem Besitzer.

- **Mit Claude:** `projektstadt.html` in Claude hochladen und sagen „Veröffentliche diese Datei als Artifact“. Daraus entsteht eine eigene, private Stadt mit eigenem Speicher, der auf allen Geräten mit demselben Claude-Konto verfügbar ist.
- **Ohne Claude:** `projektstadt-teilen.html` herunterladen und im Browser öffnen (oder auf einen Webspace legen). Alles wird nur lokal in diesem Browser gespeichert, also regelmäßig über „⋯ → Als JSON exportieren“ sichern.

Beide Versionen starten mit einer leeren Stadt. Ein Export aus einer anderen Stadt lässt sich über „⋯ → JSON importieren“ übernehmen (Bilder und STL-Dateien sind darin nur als Verweise enthalten).

`projektstadt-teilen.html` wird mit `python3 tools/build-teilen.py` aus `projektstadt.html` erzeugt. Nach Änderungen an der Hauptdatei bitte neu erzeugen.
