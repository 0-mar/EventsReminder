<h1>Events reminder</h1>
<p>
Simple web app for reminding events built with Django framework.
</p>
<h2>Installation instructions</h2>
<p>
Clone this repository via <code>git clone https://github.com/0-mar/EventsReminder.git</code> command.
</p>
<h3>Linux only</h3>
<p>
Run the <i>run_me.sh</i> file, which will create venv and all dependencies.
Skip the next part, since the script will do it automatically.
</p>

<h3>Other OS</h3>
Create virtual environment by running the <code>python -m venv ./venv</code> command.
Then run <code>pip install -r requirements.txt</code> in the virtual environment to install all dependencies.
<br>
<br>
Rename file <i>.env.local</i> to <i>.env</i>. You will need to setup a PostgreSQL database.
Database name, port, username, password and host can be changed in the <i>.env</i> file, or
you can create the database and the user with the default names from it.
