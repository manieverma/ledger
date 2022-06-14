# ledger

### SQL Alchemy Migrations

1. Create a migration project

        migrate create migration "ledger project"

2. Create a version control for a database

        python migration/manage.py version_control postgresql://postgres:root@localhost:5432/ledger migration

3. Project management script

         migrate manage manage.py --repository=migration --url=postgresql://postgres:root@localhost:5432/ledger

4. Create version file/script

         python manage.py script "filename"

5. Upgrade the database

         python manage.py upgrade [<version_number>]

6. Downgrade the database

         python manage.py downgrade <version_number>

7. Get the version number

         python manage.py db_version


