# Smart Waste Management System
A menu-driven waste management application developed using Python and MySQL as a Class 12 project by Yash Dubey.

## About the Project
The Smart Waste Management System is designed to manage waste-related records through a Python application connected to a MySQL database. It provides a simple menu-based interface for storing, viewing, and analyzing information related to dustbins, dumping vans, colonies, and dumping locations.
This project was developed to explore how programming and database management can help organize waste management information.

## Features
- **Add Dustbins:** Store dustbin locations and capacities.
- **View Dustbin Records:** Display saved dustbin information.
- **Update Dustbin Fill:** Add waste quantities to a dustbin's recorded fill amount.
- **Manage Dumping Vans:** Add dumping vans and their driver details.
- **View Dumping Van Information:** Retrieve van and driver information using a van ID.
- **Record Colony Waste:** Store waste quantities dumped by different colonies.
- **Analyze Colony Data:** Calculate and display total recorded waste by colony in descending order.
- **Manage Dump Locations:** Add and view dumping locations and their distances from the center.
- **Find Nearby Dump Locations:** Search for dumping locations within a specified distance.

## Technologies Used
- Python
- MySQL
- `mysql-connector-python`

## Requirements
- Python 3
- MySQL Server
- MySQL Connector for Python

## Setup Instructions
1. Install Python 3 and MySQL Server on your computer.
2. Create the MySQL database named `SmartWasteDB`.
3. Create the required tables: `Dustbins`, `DumpingVans`, `DumpLocations`, and `ColonyData`, with columns matching the SQL queries used in the application.
4. Install the required Python package:

   ```bash
   python -m pip install mysql-connector-python
   ```

5. Configure your MySQL connection credentials using environment variables as described in the project setup.
6. Run the Python application:

   ```bash
   python main.py
   ```
**Note:** The database schema must be created separately. The exact table definitions should match the columns used by the application.

## Learning Outcomes
- Practiced Python functions, conditional statements, loops, and exception handling.
- Learned to connect a Python application with a MySQL database.
- Used SQL queries to insert, retrieve, update, and aggregate records.
- Practiced organizing a menu-driven command-line application.

## Author
**Yash Dubey**  
B.Tech CSE (AI/ML) Student

## Copyright
Copyright © 2025 Yash Dubey. All rights reserved.

See [COPYRIGHT.md](COPYRIGHT.md) for the project's copyright notice.