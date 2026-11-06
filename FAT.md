# Factory Acceptance Test (FAT) — Demonstration

**Plan ID:** FAT  
**Revision:** 0.1  
**Planned Tests and Results**

| ID | Setup / Action | Expected Result | Status | Screenshot Evidence |
|---|---|---|---|---|
| FAT-01 | Auto mode, level=34%, pump off; resume | Pump starts within a tick | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-01.png"><img src="../assets/screenshots/FAT-01.png" width="160" alt="FAT-01 test evidence"></a> |
| FAT-02 | Auto mode, level=76%, pump on; resume | Pump stops within a tick | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-02.png"><img src="../assets/screenshots/FAT-02.png" width="160" alt="FAT-02 test evidence"></a> |
| FAT-03 | Auto mode, level=50%, pump on | Pump remains on (hysteresis) | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-03.png"><img src="../assets/screenshots/FAT-03.png" width="160" alt="FAT-03 test evidence"></a> |
| FAT-04 | Manual mode, level=50%, demand on | Pump runs | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-04.png"><img src="../assets/screenshots/FAT-04.png" width="160" alt="FAT-04 test evidence"></a> |
| FAT-05 | Manual mode, level=50%, demand off | Pump stops | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-05.png"><img src="../assets/screenshots/FAT-05.png" width="160" alt="FAT-05 test evidence"></a> |
| FAT-06 | Pause and set level=15% | LOW_LEVEL alarm active | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-06.png"><img src="../assets/screenshots/FAT-06.png" width="160" alt="FAT-06 test evidence"></a> |
| FAT-07 | Pause and set level=90% | HIGH_LEVEL alarm active | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-07.png"><img src="../assets/screenshots/FAT-07.png" width="160" alt="FAT-07 test evidence"></a> |
| FAT-08 | Manual mode, demand on, force level=96% | Trip latches and pump stops | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-08.png"><img src="../assets/screenshots/FAT-08.png" width="160" alt="FAT-08 test evidence"></a> |
| FAT-09 | With trip latched, level=50% | Pump stays off | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-09.png"><img src="../assets/screenshots/FAT-09.png" width="160" alt="FAT-09 test evidence"></a> |
| FAT-10 | Auto mode, level=0% until 75% | No system errors, the tank level reaches 75% and then drops | ![PASS](https://img.shields.io/badge/PASS-2ea44f?style=flat-square) | <a href="../assets/screenshots/FAT-10.png"><img src="../assets/screenshots/FAT-10.png" width="160" alt="FAT-10 test evidence"></a> |
