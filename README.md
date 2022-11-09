# All-In-One
SPM Project


## Getting Started


### Setting up development environemnt 
1. Check your python version    
   ```sh 
   python --version
   ``` 
   
If you do no have python or python version is below 3.3, install the latest version [here](https://www.python.org/downloads/)


### Setting up virtual environment 

1. Create virtual environment     
   ```sh
   python3 -m venv venv OR
   python -m venv venv
   
2. Activate virtual environment  
   ```sh
   source venv/bin/activate (for Mac)
   venv\Scripts\activate.bat (for Win)
   
3. Install modules in requirements.txt     
   ```sh
   pip install -r requirements.txt

### Setting up the Database
1. Import Import_LMS_Data.sql (either through phpmyadmin or SQL Workbench or any sql database)

2. Go to SQL Workbench or Import through phpmyadmin

3a. For SQL Workbench:
    ```sh
    a. On the SCHEMAS tab on the left, right click on 'course'
    b. Table Data Import Wizard
    c. Import the course.csv (inside Raw_Data folder)
    d. Done then make sure u can see course table populated now
    e. then repeat for each csv IN THIS EXACT ORDER: role --> staff --> registration
    ```

3b. For phpadmin:
    ```sh
    a. When importing individual raw data, under each Partial Import, set the Skip this number of queries (for SQL) starting from the first one: 1
    b. Import the respective csv file (inside Raw_Data folder) to the respective table
    c. Repeat for each csv IN THIS EXACT ORDER: course --> role --> staff --> registration
    d. Check if the table is populated correctly
    ```

4. Import Create_LJPS_Data.sql


### Setting up the HTTP Server

   1. Python HTTP-Server: Run this command in another terminal
   ```sh
   python -m http.server 8008 --bind 127.0.0.1
   ```

### Testing the app

   1. Use your favourite browser and type the link below: 
   ```sh
   127.0.0.1:8008/frontend/role_toggle.html

   2. Choose according to the user role u want to access to the different functions available to the different roles.
   ```


## Linter Badge
[![GitHub Super-Linter](https://github.com/alimsihui/All-In-One/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)




