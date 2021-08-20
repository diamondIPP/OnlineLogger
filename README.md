# OnlineLogger
Django based online logger for our beam tests.

### Add host
 - add ip of your pc to log/settings.py "ALLOWED_HOSTS ="
<pre><code> vim log/settings.py </code></pre>

### Create User
<pre><code> python manage.py createsuperuser </code></pre>


### Run
<pre><code> python manage.py runserver &ltip&gt:8000 </code></pre>


### Reload after major project changes
 - if you add fields, eg, 
 - changing names does not require this
<pre><code> reload_db.sh </code></pre>

### Edit fields
<pre><code> vim logger/models.py </code></pre>
