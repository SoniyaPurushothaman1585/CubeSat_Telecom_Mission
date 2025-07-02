# 🛰️ CubeSat Telecom Mission

This project involves designing a 1U CubeSat mission for relaying IoT or amateur radio signals using:
- **GMAT** for orbit simulation
- **Python** for link and power budgeting
- **LibreOffice Calc** for performance summaries
- **FreeCAD** for 3D modeling
- **Markdown** for documentation

## 📁 Folder Structure

| Folder | Contents |
|--------|----------|
| `01_Docs/` | Mission report, ICD, slides |
| `02_Orbit_Design/` | GMAT scripts and outputs |
| `03_Budgets/` | Power & link budget code and results |
| `04_Access_Analysis/` | Access plots and analysis |
| `05_3D_Model/` | Optional FreeCAD files |
| `06_Plots/` | Shared visuals for docs |
| `07_Utils/` | Constants, helper files |

## 🚀 Quick Start

1. Run `setup.sh` to generate folder structure.
2. Use `GMAT` to simulate orbit.
3. Use `Python` to run:
   - `03_Budgets/PowerBudget_Calculator.py`
   - `03_Budgets/LinkBudget_Calculator.py`
   - `04_Access_Analysis/AccessPlotter.py`

## 📜 License
MIT 

