# 🛡️ Global Network Security Report

## 1. Critical Threat: Targeted SSH Attack
- 🟡 **Stealth Probe**: `192.168.190.130.50019` (4 packets). Potential reconnaissance.
- 🔴 **Main Assault**: `192.168.190.130.50245` (60 packets). Brute Force confirmed.
- 🟡 **Stealth Probe**: `BP-Linux8.43717` (6 packets). Potential reconnaissance.
- 🟡 **Stealth Probe**: `BP-Linux8.34621` (6 packets). Potential reconnaissance.
- 🟡 **Stealth Probe**: `192.168.190.130.50374` (2 packets). Potential reconnaissance.

## 2. Other Detected Anomalies
- ⚠️ **Port Scanning**: Host probed **135** different ports.
- ⚠️ **ICMP Flood**: 84 packets detected. Potential DoS.

## 3. Traffic Sample (Top 30)
| Timestamp | Source | Flag Meaning | Technical Summary |
| :--- | :--- | :--- | :--- |
| 15:34:04.766656 | BP-Linux8.ssh | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 2243505564:2243505672, ack 1972915... |
| 15:34:04.766694 | BP-Linux8.ssh | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 108:144, ack 1, win 312, options [... |
| 15:34:04.766723 | BP-Linux8.ssh | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 144:252, ack 1, win 312, options [... |
| 15:34:04.766744 | BP-Linux8.ssh | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 252:288, ack 1, win 312, options [... |
| 15:34:04.785366 | 192.168.190.130.50019 | **Acknowledgment (ACK)** | Flags [.], ack 108, win 7319, options [nop,nop,TS ... |
| 15:34:04.785384 | 192.168.190.130.50019 | **Acknowledgment (ACK)** | Flags [.], ack 144, win 7318, options [nop,nop,TS ... |
| 15:34:04.785406 | 192.168.190.130.50019 | **Acknowledgment (ACK)** | Flags [.], ack 252, win 7316, options [nop,nop,TS ... |
| 15:34:04.785454 | 192.168.190.130.50019 | **Acknowledgment (ACK)** | Flags [.], ack 288, win 7320, options [nop,nop,TS ... |
| 15:34:05.768334 | BP-Linux8.58466 | **Other protocol** | 16550+ PTR? 130.190.168.192.in-addr.arpa. (46)... |
| 15:34:05.769075 | ns1.lan.rt.domain | **Other protocol** | 16550 NXDomain 0/1/0 (112)... |
| 15:34:06.669393 | 192.168.190.130.50245 | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 1601828178:1601828214, ack 1851233... |
| 15:34:06.669906 | BP-Linux8.ssh | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 1:37, ack 36, win 291, options [no... |
| 15:34:06.679262 | BP-Linux8.53220 | **Other protocol** | 54801+ A? lacampora.org. (31)... |
| 15:34:06.679971 | ns1.lan.rt.domain | **Other protocol** | 54801 1/0/0 A 184.107.43.74 (47)... |
| 15:34:06.681188 | BP-Linux8.ssh | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 37:153, ack 36, win 291, options [... |
| 15:34:06.681222 | BP-Linux8.ssh | **Data Transfer (PUSH-ACK)** | Flags [P.], seq 153:189, ack 36, win 291, options ... |
| 15:34:06.681248 | 190-0-175-100.gba.solunet.com.ar.2465 | **Connection Request (SYN)** | Flags [S], seq 326991629:326991749, win 512, lengt... |
| 15:34:06.681274 | 190-0-175-100.gba.solunet.com.ar.2466 | **Connection Request (SYN)** | Flags [S], seq 920517760:920517880, win 512, lengt... |
| 15:34:06.681294 | 190-0-175-100.gba.solunet.com.ar.2467 | **Connection Request (SYN)** | Flags [S], seq 556803824:556803944, win 512, lengt... |
| 15:34:06.681312 | 190-0-175-100.gba.solunet.com.ar.2468 | **Connection Request (SYN)** | Flags [S], seq 1921632185:1921632305, win 512, len... |
| 15:34:06.681328 | 190-0-175-100.gba.solunet.com.ar.2469 | **Connection Request (SYN)** | Flags [S], seq 1170972654:1170972774, win 512, len... |
| 15:34:06.681345 | 190-0-175-100.gba.solunet.com.ar.2470 | **Connection Request (SYN)** | Flags [S], seq 754504426:754504546, win 512, lengt... |
| 15:34:06.681362 | 190-0-175-100.gba.solunet.com.ar.2471 | **Connection Request (SYN)** | Flags [S], seq 669863147:669863267, win 512, lengt... |
| 15:34:06.681379 | 190-0-175-100.gba.solunet.com.ar.2472 | **Connection Request (SYN)** | Flags [S], seq 1036593434:1036593554, win 512, len... |
| 15:34:06.681396 | 190-0-175-100.gba.solunet.com.ar.2473 | **Connection Request (SYN)** | Flags [S], seq 473640609:473640729, win 512, lengt... |
| 15:34:06.681413 | 190-0-175-100.gba.solunet.com.ar.2474 | **Connection Request (SYN)** | Flags [S], seq 294639309:294639429, win 512, lengt... |
| 15:34:06.681430 | 190-0-175-100.gba.solunet.com.ar.2475 | **Connection Request (SYN)** | Flags [S], seq 2003734750:2003734870, win 512, len... |
| 15:34:06.681446 | 190-0-175-100.gba.solunet.com.ar.2476 | **Connection Request (SYN)** | Flags [S], seq 943277646:943277766, win 512, lengt... |
| 15:34:06.681463 | 190-0-175-100.gba.solunet.com.ar.2477 | **Connection Request (SYN)** | Flags [S], seq 612921749:612921869, win 512, lengt... |
| 15:34:06.681480 | 190-0-175-100.gba.solunet.com.ar.2478 | **Connection Request (SYN)** | Flags [S], seq 1079269685:1079269805, win 512, len... |
