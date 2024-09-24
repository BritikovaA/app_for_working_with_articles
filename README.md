<h2>Application for work with articles, using FastAPI and SQLite</h2>
<br>
To run on Windows - run the file start_project.bat, for Linux - start_project.sh.
<br>
Then open http://127.0.0.1:8060 to use the functionality and find out what endpoints exist, or visit http://127.0.0.1:8060/docs

<h4>End-points:</h4>
<br>
<p><b>.../articles</b> - Getting all records in the database</p>
<p><b>.../articles/{article_id}</b> - Getting a record from the database with <i>id</i> equal to <i>article_id</i></p>
<p><b>.../new_article</b> - Adding a record to the database</p>
<p><b>.../update_article/{article_id}</b> - Updating a database record with <i>id</i> equal to <i>article_id</i></p>
<p><b>.../delete_article/{article_id}</b> - Deleting a database entry with <i>id</i> equal to <i>article_id</i></p>
