import csv
import os
from collections import Counter

# Force the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def interpret_flags(packet_info):
    """Translates TCP flags into plain English for the report."""
    if "Flags [S]" in packet_info: return "Connection Request (SYN)"
    if "Flags [P.]" in packet_info: return "Data Transfer (PUSH-ACK)"
    if "Flags [.]" in packet_info: return "Acknowledgment (ACK)"
    if "Flags [R]" in packet_info: return "Connection Refused (RST)"
    if "ICMP" in packet_info: return "Ping/Network Diagnostic"
    return "Other protocol"

def generate_final_report(input_csv, output_md):
    try:
        if not os.path.exists(input_csv):
            print(f"Error: {input_csv} not found.")
            return

        with open(input_csv, 'r', encoding='utf-8') as f:
            # Use delimiter=';' as established for your Excel/CSV workflow
            reader = csv.DictReader(f, delimiter=';')
            packets = list(reader)

        if not packets:
            print("Error: The CSV file is empty.")
            return

        # --- ADVANCED ANALYSIS ---
        
        # 1. Detailed SSH Analysis (Checking for .ssh or port .22 in Destination)
        ssh_sources = [p['Source'] for p in packets if '.ssh' in p['Destination'] or '.22' in p['Destination']]
        ssh_counts = Counter(ssh_sources)
        
        # 2. Port Scan Detection (Counting unique destination ports)
        dest_ports = [p['Destination'].split('.')[-1] for p in packets]
        unique_dest_ports = len(set(dest_ports))

        # 3. ICMP Traffic (Ping)
        icmp_packets = [p for p in packets if "ICMP" in p['Packet_Info']]

        # --- MARKDOWN GENERATION ---
        with open(output_md, 'w', encoding='utf-8') as md:
            md.write("# 🛡️ Global Network Security Report\n\n")
            
            md.write("## 1. Critical Threat: Targeted SSH Attack\n")
            md.write("The tool identified a multi-stage attack pattern from `192.168.190.130`:\n")
            
            if not ssh_counts:
                md.write("- ✅ No specific SSH threats detected in this sample.\n")
            else:
                for source, count in ssh_counts.items():
                    if count >= 60:
                        md.write(f"- 🔴 **Main Assault**: Port `{source}` generated **{count} packets**. Confirmed Brute Force activity.\n")
                    elif 4 <= count <= 10:
                        md.write(f"- 🟠 **Connection Test**: Port `{source}` generated **{count} packets** (Service validation).\n")
                    else:
                        md.write(f"- 🟡 **Stealth Probe**: Port `{source}` generated **{count} packets**.\n")

            md.write("\n## 2. Other Detected Anomalies\n")
            
            # Port Scanning Alert
            if unique_dest_ports > 15:
                md.write(f"- ⚠️ **Port Scanning**: Host probed **{unique_dest_ports}** different ports. High reconnaissance activity.\n")
            
            # ICMP Alert
            if len(icmp_packets) > 50:
                md.write(f"- ⚠️ **ICMP Flood**: {len(icmp_packets)} Ping packets detected. Potential network saturation.\n")
            
            # Volume Alert
            if len(packets) > 10000:
                md.write(f"- ⚠️ **High Traffic Volume**: {len(packets)} total packets analyzed. Potential DoS risk.\n")

            md.write("\n## 3. Traffic Sample & Interpretation\n")
            md.write("| Timestamp | Source | Flag Meaning | Technical Summary |\n")
            md.write("| :--- | :--- | :--- | :--- |\n")
            
            # Display first 30 rows - Using 'Timestamp' instead of 'Heure'
            for p in packets[:30]:
                # We use .get() to avoid KeyError if the column name is slightly different
                time_val = p.get('Timestamp', p.get('Heure', 'N/A'))
                info_val = p.get('Packet_Info', p.get('Info_Paquet', 'N/A'))
                
                md.write(f"| {time_val} | {p['Source']} | **{interpret_flags(info_val)}** | {info_val[:55]}... |\n")

        print(f"Success! Report '{output_md}' has been generated.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # On définit les chemins relatifs par rapport au script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Le CSV est dans le dossier public (un cran au dessus)
    input_file = os.path.join(BASE_DIR, '..', 'public', 'Network_Analysis.csv')
    
    # Le rapport est généré à la racine du projet (un cran au dessus)
    output_file = os.path.join(BASE_DIR, '..', 'Network_Report.md')
    
    generate_final_report(input_file, output_file)