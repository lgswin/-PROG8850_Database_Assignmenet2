# -PROG8850_Database_Assignmenet2

* workflows
- Triggers on a Push to main
- Runs the Workflow on ubuntu-latest Machine
- Downloads the latest code from the repository.
- Installs MySQL tools
- Installs Python and the mysql-connector-python package
- Uses environment variables from GitHub Secrets for secure database connection.
- Runs the Python script 

* Whenever I have new SQL file, it can be added it on the variable, SQL files to apply automatically when I pushed the changes.

sql_files = ["newtable.sql", "add_departments.sql"]  # Add the new SQL script

