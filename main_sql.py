import mysql.connector

class HospitalDB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="colabuser",
            password="colabpass",
            database="HospitalManagementSystem"
        )
        self.cursor = self.conn.cursor()

    # -----------------------------
    # INSERT DATA
    # -----------------------------
    def insert_records(self):
        # Doctor
        self.cursor.execute("""
            INSERT INTO Doctor_0241801 VALUES
            (1, 'Ali', 'A', 'Hassan'),
            (2, 'Sara', 'B', 'Khaled')
        """)

        # Doctor Specialization
        self.cursor.execute("""
            INSERT INTO Doctor_Specialization_0241801 VALUES
            (1, 'Cardiology'),
            (2, 'Neurology')
        """)

        # Doctor Qualification
        self.cursor.execute("""
            INSERT INTO Doctor_Qualification_0241801 VALUES
            (1, 'MBBS'),
            (2, 'MD')
        """)

        # Patient
        self.cursor.execute("""
            INSERT INTO Patient_0241801 VALUES
            (1, '1995-05-10', 'Downtown', 'Amman', 1),
            (2, '1990-08-20', 'Jabal', 'Zarqa', 2)
        """)

        # Medicine
        self.cursor.execute("""
            INSERT INTO Medicine_0241801 VALUES
            (101, 5.00, 50),
            (102, 7.50, 30)
        """)

        # Bill
        self.cursor.execute("""
            INSERT INTO Bill_0241801 VALUES
            (1, 101, CURDATE()),
            (2, 102, CURDATE())
        """)

        self.conn.commit()
        print("âœ… Two records inserted into each table")

    # -----------------------------
    # SELECT PATIENTS
    # -----------------------------
    def select_patients(self):
        self.cursor.execute("SELECT * FROM Patient_0241801")
        rows = self.cursor.fetchall()

        print("\nðŸ“‹ Patient Table:")
        for row in rows:
            print(row)

    # -----------------------------
    # UPDATE MEDICINE PRICE
    # -----------------------------
    def update_medicine_price(self):
        self.cursor.execute("""
            UPDATE Medicine_0241801
            SET price = price + 2
        """)
        self.conn.commit()
        print("\nðŸ’Š Medicine prices updated (+2 JD)")

    # -----------------------------
    # CLOSE CONNECTION
    # -----------------------------
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("\nðŸ”’ Database connection closed")



db = HospitalDB()
db.insert_records()
db.select_patients()
db.update_medicine_price()
db.close()

