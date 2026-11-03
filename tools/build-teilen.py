#!/usr/bin/env python3
"""Erzeugt projektstadt-teilen.html aus projektstadt.html.

projektstadt.html ist für Claude-Artifacts geschrieben (ohne <html>/<head>-Rahmen).
Die Teilen-Version ist ein vollständiges HTML-Dokument, das man direkt im Browser
öffnen oder auf einem Webspace hosten kann. Sie startet mit einer leeren Stadt und
speichert alles lokal im Browser (localStorage + IndexedDB).

Aufruf:  python3 tools/build-teilen.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / "projektstadt.html").read_text(encoding="utf-8")

split = src.index('<canvas id="scene"')
head, body = src[:split].strip(), src[split:].strip()

doc = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Projektstadt: Projekte als 3D-Stadt verwalten. Jedes Projekt ist ein Gebäude, jeder Schritt ein Stockwerk.">
<!-- Teilen-Version: läuft eigenständig im Browser, alle Daten bleiben lokal in diesem Browser. -->
<!-- Automatisch erzeugt aus projektstadt.html mit tools/build-teilen.py, bitte dort ändern. -->
{head}
</head>
<body>
{body}
</body>
</html>
"""
(root / "projektstadt-teilen.html").write_text(doc, encoding="utf-8")
print("projektstadt-teilen.html erzeugt")
