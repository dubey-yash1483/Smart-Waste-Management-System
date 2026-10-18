import os
import mysql.connector

# Read database settings from environment variables
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME", "SmartWasteDB")
)

cursor = db.cursor()

if db.is_connected():
    print("THE CONNECTION IS SUCCESSFUL")



# ---------- All functions are written here, before the loop ----------

def add_dustbin():
    location = input("Enter dustbin location: ")
    try:
        capacity = int(input("Enter dustbin capacity (in kg): "))
    except:
        print("Please enter a number for capacity.")
        return

    query = "INSERT INTO Dustbins (location, capacity) VALUES (%s, %s)"
    cursor.execute(query, (location, capacity))
    db.commit()
    print("Dustbin added at", location, "with capacity", capacity, ".")


def view_records(table_name):
    # only allow these table names, to keep the query safe
    allowed_tables = ["Dustbins", "DumpingVans", "DumpLocations", "ColonyData"]
    if table_name not in allowed_tables:
        print("Invalid table name.")
        return

    cursor.execute("SELECT * FROM " + table_name)
    results = cursor.fetchall()
    for row in results:
        print(row)


def update_dustbin_fill():
    print("Enter dustbin ID like as D01")
    dustbin_id = input("Enter dustbin ID: ")
    try:
        fill = int(input("Enter fill amount (in kg): "))
    except:
        print("Please enter a number for fill amount.")
        return

    query = "UPDATE Dustbins SET filled_amount = filled_amount + %s WHERE dustbin_id = %s"
    cursor.execute(query, (fill, dustbin_id))
    db.commit()
    print("Dustbin", dustbin_id, "updated with", fill, "units.")


def add_dumping_van():
    van_number = input("Enter van number: ")
    driver_name = input("Enter driver name: ")
    query = "INSERT INTO DumpingVans (van_number, driver_name) VALUES (%s, %s)"
    cursor.execute(query, (van_number, driver_name))
    db.commit()
    print("Dumping van", van_number, "driven by", driver_name, "added.")


def view_dumping_van():
    van_id = input("Enter dumping van ID (it is like as V02): ")
    query = "SELECT van_number, driver_name FROM DumpingVans WHERE Van_id = %s"
    cursor.execute(query, (van_id,))
    van = cursor.fetchone()
    if van:
        print("ALERT: Dumping van", van[0], "driven by", van[1], "is on its way!!")
    else:
        print("No van found with that ID.")


def record_colony_dump():
    colony_name = input("Enter colony name: ")
    try:
        waste_dumped = int(input("Enter waste dumped (in kg): "))
    except:
        print("Please enter a number for waste dumped.")
        return

    query = "INSERT INTO ColonyData (colony_name, waste_dumped) VALUES (%s, %s)"
    cursor.execute(query, (colony_name, waste_dumped))
    db.commit()
    print(colony_name, "has dumped", waste_dumped, "units of waste.")


def analyze_colonies():
    query = "SELECT colony_name, SUM(waste_dumped) as total_dumped FROM ColonyData GROUP BY colony_name ORDER BY total_dumped DESC"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Colony Performance:")
    for row in results:
        print("Colony:", row[0], ", Total Waste Dumped:", row[1])


def add_dump_location():
    location_name = input("Enter dump location name: ")
    try:
        distance = float(input("Enter distance from center (in km): "))
    except:
        print("Please enter a number for distance.")
        return

    query = "INSERT INTO DumpLocations (location_name, distance_from_center) VALUES (%s, %s)"
    cursor.execute(query, (location_name, distance))
    db.commit()
    print("Dumping location", location_name, "added,", distance, "km from center.")


def find_nearby_locations():
    try:
        max_distance = float(input("Enter maximum distance (in km): "))
    except:
        print("Please enter a number for distance.")
        return

    query = "SELECT location_name, distance_from_center FROM DumpLocations WHERE distance_from_center <= %s"
    cursor.execute(query, (max_distance,))
    results = cursor.fetchall()
    print("Nearby Dump Locations within", max_distance, "km:")
    for row in results:
        print(row[0], "(", row[1], "km)")


# ---------- Main program starts here ----------

print("**************************************SMART WASTE MANAGEMENT SYSTEM***************************************")

while True:

    print("Choose according to your needs")
    print("1. Add Dustbin")
    print("2. View Dustbins")
    print("3. Update Dustbin Fill")
    print("4. Add Dumping Van")
    print("5. View Dumping Vans")
    print("6. Record Colony Dump")
    print("7. Analyze Colonies")
    print("8. Add Dump Location")
    print("9. View Dump Locations")
    print("10. Find Nearby Dump Locations")
    print("11. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Please enter a number from the menu.")
        continue

    if choice == 1:
        add_dustbin()
    elif choice == 2:
        print("Dustbin Records:")
        view_records("Dustbins")
    elif choice == 3:
        update_dustbin_fill()
    elif choice == 4:
        add_dumping_van()
    elif choice == 5:
        print("Dumping Van Records:")
        view_dumping_van()
    elif choice == 6:
        record_colony_dump()
    elif choice == 7:
        analyze_colonies()
    elif choice == 8:
        add_dump_location()
    elif choice == 9:
        print("Dump Location Records:")
        view_records("DumpLocations")
    elif choice == 10:
        find_nearby_locations()
    elif choice == 11:
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")

# close the connection after exiting the loop
cursor.close()
db.close()
