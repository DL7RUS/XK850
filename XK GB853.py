import serial
import time

# Ersetze '/dev/ttyUSB0' mit dem Namen deines RS-232 Ports
ser = serial.Serial('/dev/ttyUSB0', 2400, timeout=1)  # Baudrate auf 2400 setzen

def send_command(serial_port, cmd):
    print(f"Sending: {cmd}")
    serial_port.write(cmd.encode())
    time.sleep(1)  # Justiere die Verzögerung nach Bedarf

    # Lese Antwort, falls dein Gerät Daten zurückschickt
    response = serial_port.readline().decode().strip()
    print(f"Received: {response}")

try:
    while True:  # Endlosschleife starten
        user_input = input("Bitte geben Sie den Befehlsteil ein (z.B. 'H1' oder 'exit' zum Beenden): ")
        
        # Wenn der Benutzer 'exit' eingibt, wird die Schleife beendet
        if user_input.lower() == 'exit':
            print("Beende Programm.")
            break
        
        # Den kompletten Befehl zusammensetzen und senden
        command = f"\n*{user_input}\r"
        send_command(ser, command)

finally:
    ser.close()  # Sicherstellen, dass die Verbindung geschlossen wird

print("Programm beendet.")
