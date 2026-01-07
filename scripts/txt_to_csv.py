import csv
import os

# On définit le dossier du script pour gérer les chemins relatifs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_clean_csv():
    # Chemins précis
    input_path = os.path.join(BASE_DIR, 'DumpFile.txt')
    # On remonte d'un dossier (..) pour aller dans /public
    output_path = os.path.join(BASE_DIR, '..', 'public', 'Network_Analysis.csv')

    try:
        with open(input_path, 'r') as f:
            lines = f.readlines()

        # On s'assure que le dossier public existe (au cas où)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow(['Timestamp', 'Source', 'Destination', 'Packet_Info'])

            for line in lines:
                if "IP" in line:
                    elements = line.split()
                    if len(elements) >= 5: # Sécurité pour éviter les lignes vides
                        timestamp = elements[0]
                        source = elements[2]
                        destination = elements[4].replace(':', '')
                        packet_details = " ".join(elements[5:])
                        writer.writerow([timestamp, source, destination, packet_details])
        
        print(f"Success: {output_path} created!")
    
    except FileNotFoundError:
        print(f"Error: {input_path} not found.")

if __name__ == "__main__":
    generate_clean_csv()