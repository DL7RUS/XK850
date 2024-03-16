#!/usr/bin/env python3
import subprocess

# Navigiere zum Repository-Verzeichnis
repository_path = "/home/pi/XKGB853"

# Führe den Git Pull-Befehl aus
try:
    subprocess.run(["git", "-C", repository_path, "pull", "origin", "master"], check=True)
    print("Git pull erfolgreich ausgeführt.")
except subprocess.CalledProcessError as e:
    print("Fehler beim Ausführen von git pull:", e)
