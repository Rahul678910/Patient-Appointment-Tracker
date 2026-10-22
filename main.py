#!/usr/bin/env python3
"""
Patient Appointment Tracker - Main Application Launcher
Supports both Graphical User Interface (GUI) and Command-Line Interface (CLI).

Usage:
    python main.py             # Launches Graphical User Interface (GUI)
    python main.py --gui       # Explicitly launch GUI
    python main.py --cli       # Launch Interactive Terminal CLI
    python main.py --cli list  # List appointments via CLI
    python main.py --cli --help# View all CLI commands
"""

import sys

# Ensure UTF-8 output encoding across all Windows consoles
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main():
    args = sys.argv[1:]

    # Check for direct booking shortcut: 'python main.py book' or 'python main.py --book'
    if args and args[0] in ("book", "--book", "-b"):
        # If user also specified --cli or -c anywhere in args
        if any(flag in ("--cli", "-c", "cli") for flag in args):
            from tracker.cli import interactive_book
            from tracker.db import Database
            interactive_book(Database())
            return
        else:
            # Launch GUI directly with the Book Patient dialog opened!
            try:
                from tracker.gui import main_gui
                main_gui(auto_open_book=True)
                return
            except Exception as e:
                print(f"Failed to start GUI ({e}). Falling back to Terminal CLI...")
                from tracker.cli import interactive_book
                from tracker.db import Database
                interactive_book(Database())
                return

    # If explicitly requested CLI or any CLI subcommand
    if args and args[0] in ("--cli", "-c", "cli"):
        from tracker.cli import main_cli
        # Pass remaining arguments to CLI
        main_cli(args[1:])
        return

    # Help flag
    if args and args[0] in ("--help", "-h"):
        print("""
🩺 Patient Appointment Tracker
==============================

Modes of Operation:
  python main.py                 Launch modern Desktop Graphical User Interface (GUI)
  python main.py book            Directly open visual 'Book Patient' window & pass
  python main.py --gui           Explicitly launch GUI mode
  python main.py --cli           Launch Interactive Terminal CLI menu
  python main.py book --cli      Launch Interactive Terminal Patient Booking slip
  python main.py --cli [command] Run non-interactive CLI commands

CLI Subcommands:
  book                           Interactive or flag-based booking with visual pass
  add                            Book a new patient appointment
  list                           List appointments (with optional filters)
  status <id> <status>           Update appointment status
  delete <id>                    Delete an appointment
  search <query>                 Search appointments by patient, phone, doctor
  stats                          Display clinic statistics & overview
  export                         Export appointments to CSV or JSON
  seed                           Load sample demo appointments
""")
        return

    # Default: Graphical User Interface (GUI)
    try:
        from tracker.gui import main_gui
        main_gui()
    except Exception as e:
        print(f"Failed to start GUI ({e}). Falling back to Terminal CLI interface...")
        from tracker.cli import main_cli
        main_cli()


if __name__ == "__main__":
    main()
