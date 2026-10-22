# 🩺 Patient Appointment Tracker

A comprehensive, production-ready Patient Appointment Tracking and Clinical Scheduling system featuring **both a modern Graphical User Interface (GUI)** and a **full-featured Command-Line Interface (CLI)**.

Built entirely with standard Python libraries (`tkinter`, `sqlite3`, `csv`, `json`), requiring **zero third-party dependencies** or external installations.

---

## 🌟 Key Features

- **Modern Desktop GUI (Tkinter / ttk)**:
  - **Dynamic KPI Dashboard**: Live summary cards showing Total, Today's, Upcoming Active, Completed, and Cancelled appointments. Click any card to filter instantly!
  - **Live Search & Multi-Criteria Filtering**: Search by patient name, phone, doctor, or ID, with instant status, department, and date filters.
  - **Interactive Table**: Sortable columns, zebra striping, status color badges, and double-click to view details.
  - **Right-Click Context Menu**: Quick access to edit, mark as confirmed/completed/cancelled, or delete appointments.
  - **Schedule Conflict Detection**: Proactively detects and warns if a doctor is already booked for the selected date and time slot.
  - **Modal Forms**: Guided appointment booking with date shortcuts (*Today*, *Tomorrow*, *+7 Days*) and standardized time slots.
  - **1-Click Export & Demo Data**: Easily export to CSV or load realistic sample records.

- **Dual-Mode Command-Line Interface (CLI)**:
  - **Interactive Terminal Console**: Numbered navigation menu with color-coded status badges, ASCII formatted tables, and guided prompts.
  - **Non-Interactive CLI Subcommands**: Scriptable commands (`list`, `add`, `status`, `delete`, `search`, `stats`, `export`, `seed`) for fast terminal use or automation.

- **Robust Data Engine (SQLite3)**:
  - Local persistent database (`appointments.db`) with automatic schema setup and indexing for fast query performance.
  - Safe transaction management with automatic connection release.

---

## 📁 Project Architecture

```
Patient-Appointment-Tracker/
├── tracker/
│   ├── __init__.py         # Package initialization & version metadata
│   ├── models.py           # Dataclass model, constants & field validators
│   ├── db.py               # SQLite database access layer & CRUD operations
│   ├── gui.py              # Tkinter/ttk desktop graphical interface
│   ├── cli.py              # Interactive terminal menu & CLI subcommands
│   └── sample_data.py      # Realistic sample patient appointment generator
├── tests/
│   └── test_tracker.py     # Comprehensive automated unit test suite
├── main.py                 # Unified launcher (GUI default, CLI via flags)
├── run_gui.bat             # 1-Click Windows launcher for GUI
├── run_cli.bat             # 1-Click Windows launcher for CLI
├── appointments.db         # Persistent SQLite database file
└── README.md               # Documentation & usage guide
```

---

## 🚀 Quick Start Guide

### Option 1: 1-Click Launchers (Windows)
- **Launch GUI**: Double-click [`run_gui.bat`](file:///c:/Users/RAM%20DAS%20MURMU/OneDrive/Desktop/Patient-Appointment-Tracker/run_gui.bat)
- **Launch CLI**: Double-click [`run_cli.bat`](file:///c:/Users/RAM%20DAS%20MURMU/OneDrive/Desktop/Patient-Appointment-Tracker/run_cli.bat)

### Option 2: Running with Python

#### 1. Launch Modern GUI
```bash
python main.py
# or explicitly
python main.py --gui
```

#### 2. Book a Patient with Direct Visual Output
```bash
# Directly launches GUI with Book Patient window & visual Booking Pass
python main.py book

# Or book via Terminal CLI with visual ASCII Pass Slip
python main.py book --cli
```

#### 3. Launch Interactive Terminal CLI Console
```bash
python main.py --cli
```

---

## 🖥️ CLI Commands Cheatsheet

In addition to the interactive menu, you can run direct subcommands:

| Action | Command |
|---|---|
| **List all appointments** | `python main.py --cli list` |
| **Filter by status** | `python main.py --cli list --status Confirmed` |
| **Filter by date** | `python main.py --cli list --date today` *(or `tomorrow`, `upcoming`)* |
| **Search appointments** | `python main.py --cli search "Alice"` |
| **Book new appointment** | `python main.py --cli add --name "John Doe" --phone "555-0123" --doctor "Dr. Sarah Johnson (General Medicine)" --date "2026-10-25" --time "10:00 AM" --reason "Annual checkup"` |
| **Update status** | `python main.py --cli status 1 Completed` |
| **Delete appointment** | `python main.py --cli delete 1` |
| **Clinic stats overview** | `python main.py --cli stats` |
| **Export to CSV** | `python main.py --cli export --output clinic_records.csv` |
| **Export to JSON** | `python main.py --cli export --output clinic_records.json` |
| **Load sample records** | `python main.py --cli seed` |
| **Help reference** | `python main.py --help` |

---

## 🧪 Running Automated Tests

Run the complete test suite verifying database transactions, conflict detection, models, and export logic:

```bash
python -m unittest discover tests
```

---

## 🏥 Clinical Fields Tracked

- **Patient Name & Phone** (required)
- **Email, Age, & Gender**
- **Doctor Assigned** (with support for custom specialist entries)
- **Department** (General Medicine, Cardiology, Dermatology, Pediatrics, Orthopedics, Neurology, Ophthalmology, etc.)
- **Date & Time Slot** (standardized and validated)
- **Status** (`Scheduled`, `Confirmed`, `Completed`, `Cancelled`, `No-Show`)
- **Reason for Visit / Symptoms**
- **Clinical & Receptionist Notes**
- **Audit Timestamp** (`created_at`)

---

## 📄 License

This project is licensed under the MIT License.
