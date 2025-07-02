# 🛰️ CubeSat Interface Control Document (ICD)

**Mission**: CubeRelay-IoT  
**Version**: 1.0  
**Date**: 2025-07-01  
**Author**: Soniya Purushothaman

---

## 1. Introduction

This Interface Control Document defines the physical, electrical, and logical interfaces between the subsystems of the CubeRelay-IoT 1U CubeSat. It serves as a reference for integration, verification, and mission operation planning.

---

## 2. Subsystems Covered

- Payload (UHF/VHF Transceiver)
- On-Board Computer (OBC)
- Electrical Power System (EPS)
- Attitude Determination and Control System (ADCS)
- Structure & Thermal
- Solar Panels & Battery Pack

---

## 3. Interface Summary Table

| From        | To          | Interface Type | Signal/Power     | Description                   |
|-------------|-------------|----------------|------------------|-------------------------------|
| Payload     | OBC         | UART            | 3.3V logic       | Uplink/downlink data control |
| OBC         | EPS         | GPIO, I2C       | 3.3V I/O, PWR_OK | Power control, telemetry     |
| OBC         | ADCS        | I2C             | 3.3V logic       | Attitude data & sensor input |
| EPS         | Battery     | Power lines     | 4.2V max @ 1A    | Battery charge and discharge |
| Solar Panel | EPS         | Power lines     | 5–7V input       | Solar energy input           |

---

## 4. Mechanical Interface

- Structure conforms to 1U CubeSat (10 × 10 × 10 cm)
- Aluminum rails with standard PC/104 mounting
- Payload occupies central tray; battery at base; PCBs stacked

---

## 5. Electrical Interface

- Operating voltages: 3.3V (logic), 5V (bus), 4.2V (battery)
- Total power draw: ≤ 4.0 W average
- Ground: Common ground plane via mechanical structure

---

## 6. Data Interfaces

### 6.1 UART Interface (Payload ↔ OBC)

| Pin # | Signal Name | Direction | Description              |
|-------|-------------|-----------|--------------------------|
| 1     | TX          | Payload → OBC | Transmit (data uplink) |
| 2     | RX          | OBC → Payload | Receive (data downlink) |
| 3     | GND         | –         | Ground                   |
| 4     | VCC (3.3V)  | –         | Logic power (optional)   |

- Baud Rate: 9600 bps (configurable)
- Format: 8N1 (8 data bits, no parity, 1 stop)

### 6.2 I2C Interface (OBC ↔ ADCS, EPS)

| Pin # | Signal Name | Direction | Description              |
|-------|-------------|-----------|--------------------------|
| 1     | SDA         | Bi-directional | Data line          |
| 2     | SCL         | OBC → Subsystem | Clock line        |
| 3     | GND         | –         | Ground                   |
| 4     | VCC (3.3V)  | –         | Logic power              |

- I2C speed: 100 kHz (standard mode)
- Addresses:
  - ADCS: 0x42
  - EPS:  0x30

---

## 7. Thermal Interface

- Passive thermal control
- Interface pads for payload and EPS heat sinking
- Components rated for -20°C to +60°C operating range

---

## 8. Interface Block Diagram

Below is a simplified system architecture showing logical data/power flows.



---


*Legend:*
- Arrows represent data/power flow
- EPS: Electrical Power System  
- ADCS: Attitude Determination and Control System  
- OBC: On-Board Computer

---

## 9. Change Log

| Version | Date       | Author              | Change Description         |
|---------|------------|---------------------|-----------------------------|
| 1.0     | 2025-07-01 | Soniya Purushothaman | Initial ICD release         |

---

