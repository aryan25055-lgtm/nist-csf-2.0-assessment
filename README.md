# NIST Cybersecurity Framework 2.0 Assessment Tool

An educational Python project demonstrating how an organization can assess cybersecurity practices using the NIST Cybersecurity Framework (CSF) 2.0.

## Features

- Framework map: Govern, Identify, Protect, Detect, Respond, Recover.
- Interactive assessment of 26 example control questions.
- 0–4 implementation ratings and function-level scoring.
- Prioritized recommendations based on lower-scoring functions.
- Fictional e-commerce ransomware tabletop scenario.
- Export assessment to TXT and CSV.
- Saves assessment locally as JSON.
- Python standard library only; no third-party dependencies.

## Requirements

- Python 3.9 or newer
- Windows, macOS, or Linux

## Run on Windows

```bash
python main.py
```

Or:
```bash
py main.py
```

## Run on Kali Linux

```bash
python3 main.py
```

## How to use

1. Select **1** to view the framework map.
2. Select **2** to create an assessment and rate controls from 0 to 4.
3. Select **3** to view the dashboard.
4. Select **4** to view prioritized recommendations.
5. Select **5** to explore the ransomware tabletop scenario.
6. Select **6** or **7** to export TXT or CSV reports.
7. Select **8** to save the assessment.

The assessment is also saved automatically when exiting.

## Rating scale

| Rating | Meaning |
|---:|---|
| 0 | Not Implemented |
| 1 | Initial |
| 2 | Developing |
| 3 | Established |
| 4 | Optimized |

These are simplified educational ratings created for this project. They are **not** the official NIST CSF Implementation Tiers.

## Project structure

```text
nist-csf-2.0-assessment/
├── main.py
├── README.md
├── requirements.txt
├── framework_map.txt
└── .gitignore
```

Generated after running the program:
- `assessment_data.json`
- `NIST_CSF_Assessment_Report.txt`
- `NIST_CSF_Control_Ratings.csv`

## Official references

- NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29 (2024): https://doi.org/10.6028/NIST.CSWP.29
- NIST CSF website: https://www.nist.gov/cyberframework

## Disclaimer

This is an educational self-assessment tool. It is not an official NIST product, formal audit, certification, compliance determination, or guarantee of security. Its control questions are simplified examples inspired by CSF 2.0 outcomes.
