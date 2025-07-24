import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",     # replace with your username
    password="root", # replace with your password
    database="student_db",
    port=3307                        # use your port if different
)

cursor = con.cursor()

def create_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    query = "INSERT INTO student (name, age) VALUES (%s, %s)"
    values = (name,age)
    cursor.execute(query, values)
    con.commit()
    print("✅ Student record added successfully.")

def read_student():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("\n📋 All Students:")
    for row in rows:
        print(row)

def update_student():
    id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    
    query = "UPDATE student SET name=%s, age=%s WHERE id=%s"
    values = (name, age, id)
    cursor.execute(query, values)
    con.commit()

    if cursor.rowcount == 0:
        print("❌ No student found with that ID.")
    else:
        print("✅ Student record updated successfully.")

def delete_student():
    id = int(input("Enter student ID to delete: "))
    query = "DELETE FROM student WHERE id = %s"
    cursor.execute(query, (id,))
    con.commit()

    if cursor.rowcount == 0:
        print("❌ No student found with that ID.")
    else:
        print("✅ Student record deleted successfully.")

# Main loop
while True:
    print("\n--- Student Management System ---")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_student()
    elif choice == '2':
        read_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")

# Close connection
cursor.close()
con.close()
