#!/usr/bin/env python3
"""
Test script to verify MySQL connection and database setup
"""

import mysql.connector
import sys

def test_mysql_connection():
    """Test MySQL connection with the provided credentials."""
    
    # MySQL Configuration - Update these with your MySQL credentials
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'mmm1204'  # Update with your MySQL password
    MYSQL_DATABASE = 'shipping_db'  # Update with your database name
    
    try:
        # Test connection without database first
        print("Testing MySQL connection...")
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        
        cursor = connection.cursor()
        print(f"✓ Successfully connected to MySQL server")
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}")
        cursor.execute(f"USE {MYSQL_DATABASE}")
        print(f"✓ Database '{MYSQL_DATABASE}' is ready")
        
        # Test creating tables
        print("Creating test tables...")
        
        # Create product table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                UNIQUE KEY unique_name (name)
            )
        """)
        
        # Create shipment table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shipment (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                origin VARCHAR(255),
                destination VARCHAR(255),
                FOREIGN KEY (product_id) REFERENCES product(id)
            )
        """)
        
        connection.commit()
        print("✓ Database tables created successfully")
        
        # Test inserting sample data
        print("Testing data insertion...")
        cursor.execute("INSERT IGNORE INTO product (name) VALUES (%s)", ("Test Product",))
        product_id = cursor.lastrowid
        
        cursor.execute("""
            INSERT INTO shipment (product_id, quantity, origin, destination) 
            VALUES (%s, %s, %s, %s)
        """, (product_id, 10, "Test Origin", "Test Destination"))
        
        connection.commit()
        print("✓ Sample data inserted successfully")
        
        # Test querying data
        cursor.execute("SELECT COUNT(*) FROM product")
        product_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM shipment")
        shipment_count = cursor.fetchone()[0]
        
        print(f"✓ Database contains {product_count} products and {shipment_count} shipments")
        
        # Clean up test data
        cursor.execute("DELETE FROM shipment WHERE origin = 'Test Origin'")
        cursor.execute("DELETE FROM product WHERE name = 'Test Product'")
        connection.commit()
        print("✓ Test data cleaned up")
        
        connection.close()
        print("✓ MySQL connection test completed successfully!")
        return True
        
    except mysql.connector.Error as e:
        print(f"✗ MySQL connection failed: {e}")
        print("\nPlease check:")
        print("1. MySQL server is running")
        print("2. Database 'shipping_db' exists")
        print("3. User 'root' has proper permissions")
        print("4. Password is correct")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_mysql_connection()
    sys.exit(0 if success else 1)
