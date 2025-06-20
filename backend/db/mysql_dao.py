import mysql.connector
import os

def insert_invoice_mysql(invoice):
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DATABASE", "invoices")
    )
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO cleaned_invoices (vendor, date, total, notes)
        VALUES (%s, %s, %s, %s)
        """,
        (invoice.vendor, invoice.date, invoice.total, invoice.notes)
    )

    connection.commit()
    cursor.close()
    connection.close()