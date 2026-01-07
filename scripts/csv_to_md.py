import csv
import os
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def interpret_flags(packet_info):
    if "Flags [S]" in packet_info: return "Connection Request (SYN)"
    if "Flags [P.]" in packet_info: return "Data Transfer (PUSH-ACK)"
    if "Flags [.]" in packet_info: return "Acknowledgment (ACK)"
    if "Flags [R]" in packet_info: return "Connection Refused (RST)"
    if "ICMP" in packet_info: return "Ping/Network Diagnostic"
    if "telnet" in packet_info or ".23" in packet_info: return "Unencrypted Telnet"
    return "Other protocol"

def generate_final_report(input_csv, output_md):
    try:
        if not os.path.exists(input_csv):
            print(f"Error: {input_csv} not found.")
            return

        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            packets = list(reader)

        if not packets:
            print("Error: The CSV file is empty.")
            return

        # --- ANALYSE AVANCÉE ---
        
        # 1. SSH Analysis
        ssh_packets = [p for p in packets if '.ssh' in p['Destination'] or '.22' in p['Destination']]
        ssh_counts = Counter([p['Source'] for p in ssh_packets])
        
        # 2. Port Scan Detection (Seuil abaissé à 5 ports pour détecter les scans furtifs)
        dest_ports = [p['Destination'].split('.')[-1] for p in packets]
        unique_dest_ports = len(set(dest_ports))

        # 3. ICMP Traffic
        icmp_packets = [p for p in packets if "ICMP" in p['Packet_Info']]

        # 4. Telnet (Danger Alert)
        telnet_attempts = [p for p in packets if "telnet" in p['Destination'] or ".23" in p['Destination']]

        # --- GÉNÉRATION DU MARKDOWN ---
        with open(output_md, 'w', encoding='utf-8') as md:
            md.write("# 🛡️ Global Network Security Report\n\n")
            
            md.write("## 1. Critical Threat: Targeted SSH Attack\n")
            if not ssh_counts:
                md.write("- ✅ No specific SSH threats detected.\n")
            else:
                for source, count in ssh_counts.items():
                    if count >= 40: # Seuil adapté
                        md.write(f"- 🔴 **Main Assault**: `{source}` ({count} packets). Brute Force confirmed.\n")
                    else:
                        md.write(f"- 🟡 **Stealth Probe**: `{source}` ({count} packets). Potential reconnaissance.\n")

            md.write("\n## 2. Other Detected Anomalies\n")
            
            # Alerte Port Scan (Abaissé à > 5)
            if unique_dest_ports > 5:
                md.write(f"- ⚠️ **Port Scanning**: Host probed **{unique_dest_ports}** different ports.\n")
            
            # Alerte ICMP (Abaissé à > 20)
            if len(icmp_packets) > 20:
                md.write(f"- ⚠️ **ICMP Flood**: {len(icmp_packets)} packets detected. Potential DoS.\n")

            # Alerte Telnet
            if telnet_attempts:
                md.write(f"- ❌ **Insecure Protocol**: {len(telnet_attempts)} Telnet attempts detected (Port 23).\n")

            md.write("\n## 3. Traffic Sample (Top 30)\n")
            md.write("| Timestamp | Source | Flag Meaning | Technical Summary |\n")
            md.write("| :--- | :--- | :--- | :--- |\n")
            
            for p in packets[:30]:
                time_val = p.get('Timestamp', 'N/A')
                info_val = p.get('Packet_Info', 'N/A')
                md.write(f"| {time_val} | {p['Source']} | **{interpret_flags(info_val)}** | {info_val[:50]}... |\n")

        print(f"Success! Report generated.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(BASE_DIR, '..', 'public', 'Network_Analysis.csv')
    output_file = os.path.join(BASE_DIR, '..', 'Network_Report.md')
    generate_final_report(input_file, output_file)