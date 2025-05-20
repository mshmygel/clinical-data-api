# 🧬 Clinical Data Viewer (SDTM/ADaM)

A Dockerized FastAPI-based application for browsing clinical tabular data in SDTM/ADaM formats (`.sas7bdat`, `.xpt`, `.csv`, `.xlsx`).

---

## ✨ Features

* 🔍 Explore datasets through a simple API
* 📁 File format support: `.sas7bdat`, `.xpt`, `.csv`, `.xlsx`
* 📊 View metadata, column stats, and row previews
* ⚙️ Lightweight, cross-platform, Dockerized setup
* 🧼 Clean architecture with modular codebase

---

## ⚡ Quick Start

Before starting the application, make sure to place your dataset files in the `data/` folder. You can use any combination of the supported formats: `.sas7bdat`, `.xpt`, `.csv`, or `.xlsx`.

**Example:**

```bash
clinical-data-api/
├── data/
│   ├── adam_base.sas7bdat
│   ├── dm.xpt
│   ├── trial_results.csv
│   └── SDTM_spec.xlsx
```

Once the files are in place, proceed with the steps below.

### 🐧 On Linux / macOS (with `make` installed):

```bash
make start
```

### 🪟 On Windows (PowerShell or CMD):

```cmd
.\make.bat start
```

To stop:

```bash
make stop         # or .\make.bat stop
```

To rebuild:

```bash
make restart      # or .\make.bat restart
```

> 📎 Note: You must have Docker installed and running.

---

## 🧠 Overview

Clinical Data Viewer is built to provide an API for inspecting the structure and content of clinical datasets. It supports SDTM and ADaM standard file formats commonly used in regulatory submissions. Data is read on-demand and exposed through FastAPI.

---

## 📂 How to Add Datasets

Simply copy your clinical data files into the `data/` directory in the project root.

```
clinical-data-api/
├── data/
│   ├── adam_base.sas7bdat
│   ├── dm.xpt
│   ├── ADAM_spec.xlsx
│   └── SDTM_spec_Variables.csv
```

🟢 No restart required — files are dynamically listed.

Supported formats:

* `.sas7bdat` — SAS binary tables
* `.xpt` — SAS XPORT transport format
* `.csv` — Comma-separated values
* `.xlsx` — Excel spreadsheets

---

## 🔌 API Endpoints

| Method | Endpoint                         | Description                              |
| ------ | -------------------------------- | ---------------------------------------- |
| `GET`  | `/datasets`                      | List all available dataset files         |
| `GET`  | `/datasets/{name}`               | Get number of rows and columns           |
| `GET`  | `/datasets/{name}/head?limit=10` | Preview top `n` rows                     |
| `GET`  | `/datasets/{name}/columns`       | Show column names, types, and null count |

🔗 Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧱 Project Structure

```
clinical-data-api/
├── app/
│   ├── api.py            # FastAPI routes
│   ├── main.py           # FastAPI app instance
│   ├── models/           # Pydantic response models
│   ├── services/         # Dataset loading logic
│   └── utils/            # Format-specific file readers
├── data/                 # Drop .sas7bdat/.xpt/.csv/.xlsx files here
├── Dockerfile
├── docker-compose.yml
├── Makefile              # Unix launcher
├── make.bat              # Windows launcher
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## 💻 System Requirements

* **Docker** — required to build and run the project
* **make** (Linux/macOS) or `make.bat` (Windows)
* No need to install Python unless working in dev mode


