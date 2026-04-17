📚 CampusFind – Console Lost & Found System
CampusFind is a Python console-based application that helps manage lost and found items on campus. It provides a simple text-driven interface for students and administrators to record, search, and organize items efficiently.

🚀 Features
🎨 ASCII Art Greeting – Welcomes users with a styled banner using pyfiglet.

🔍 Lost & Found Sections

Found Item Section – Add details (name, quantity, location, date, time, description) and store them in items.json.

Lost Item Section – Search for lost items against stored records, claim them if found, and update delivery status.

👥 User & Admin Modes

User Mode – Report lost or found items.

Admin Mode – Login with credentials from login.json, view all items in tabular format, and update delivery status.

💾 Persistent Storage – Uses JSON files (items.json, login.json) for data management.

✅ Validation & Error Handling – Input validation for quantity, dates, times, and IDs.

🛠️ Tech Stack
Language: Python

Libraries: json, datetime, pyfiglet

Concepts Used: File handling, input validation, modular functions, console UI
