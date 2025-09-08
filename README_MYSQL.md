# Walmart Shipping Data Processing - MySQL Version

This script processes shipping data from three CSV files and populates a MySQL database with products and shipments.

## Prerequisites

1. **MySQL Server**: Make sure MySQL server is running on your system
2. **Python Dependencies**: Install required packages
3. **Database Setup**: Create the target database

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Create MySQL database:
```sql
CREATE DATABASE shipping_db;
```

3. Update MySQL credentials in `populate_database.py`:
   - Update `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE` variables

## Usage

1. **Test MySQL Connection**:
```bash
python test_mysql_connection.py
```

2. **Run the Main Script**:
```bash
python populate_database.py
```

## Database Schema

The script creates two tables:

### Product Table
- `id` (INT AUTO_INCREMENT PRIMARY KEY)
- `name` (VARCHAR(255) NOT NULL)

### Shipment Table
- `id` (INT AUTO_INCREMENT PRIMARY KEY)
- `product_id` (INT NOT NULL) - Foreign key to product table
- `quantity` (INT NOT NULL)
- `origin` (VARCHAR(255))
- `destination` (VARCHAR(255))

## Data Processing

1. **shipping_data_0.csv**: Self-contained shipping data - inserted directly
2. **shipping_data_1.csv + shipping_data_2.csv**: Combined data where:
   - shipping_data_1.csv contains products per shipment
   - shipping_data_2.csv contains route information
   - Products are grouped by shipment_identifier and quantities are summed

## Configuration

Update these variables in `populate_database.py`:

```python
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'  # Update with your MySQL password
MYSQL_DATABASE = 'shipping_db'    # Update with your database name
```

## Error Handling

The script includes comprehensive error handling and logging. Check the console output for detailed information about the processing status.
