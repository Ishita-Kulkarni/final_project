# SQL Assignment - FastAPI Calculator Database

This directory contains all SQL scripts for the FastAPI Calculator database assignment.

## 📁 SQL Scripts

The SQL scripts are organized in the order they should be executed:

1. **`01_create_tables.sql`** - Creates the `users` and `calculations` tables
2. **`02_insert_records.sql`** - Inserts sample data into both tables
3. **`03_query_data.sql`** - Queries to retrieve and join data
4. **`04_update_record.sql`** - Updates a calculation record
5. **`05_delete_record.sql`** - Deletes a calculation record
6. **`complete_setup.sql`** - Complete script that runs all steps at once

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Calculations Table
```sql
CREATE TABLE calculations (
    id SERIAL PRIMARY KEY,
    operation VARCHAR(20) NOT NULL,
    operand_a FLOAT NOT NULL,
    operand_b FLOAT NOT NULL,
    result FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

## 🚀 How to Run

### Option 1: Run All at Once
1. Open pgAdmin at http://localhost:5050
2. Connect to the `calculator_db` database
3. Open Query Tool
4. Load and execute `complete_setup.sql`

### Option 2: Run Step by Step
Execute each script in order (01 through 05) to see individual results.

## 📊 Expected Results

### After Insert (Step B)
- **Users table**: 2 rows (alice, bob)
- **Calculations table**: 3 rows

### After Update (Step D)
- Calculation with id=1 has result changed from 5 to 6

### After Delete (Step E)
- Calculation with id=2 is removed
- **Calculations table**: 2 rows remaining

## 🔗 Connection Details

- **Host**: postgres (Docker service name)
- **Port**: 5432
- **Database**: calculator_db
- **Username**: calculator_user
- **Password**: calculator_pass

## 📝 Assignment Steps Covered

- ✅ (A) Create Tables
- ✅ (B) Insert Records
- ✅ (C) Query Data
- ✅ (D) Update a Record
- ✅ (E) Delete a Record
