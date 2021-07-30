# SQL_Injection_Test
## What is this?
This project build a simple web server for testing SQL injection attack.

![cloud server architecture](https://i.imgur.com/hfCiYBz.png)

In the above diagram, this project run the web server in GCP Compute Engine.
## How to run?
- Add `.env` file to configure Database setting
```
DB_HOST=XX
DB_USER=XX
DB_PASS=XX
DB_NAME=XX
```
- Build docker image
```
docker build -t sql_injection .
```
- Run docker
```
docker run -d -p 80:80 sql_injection 
```
- Open your browser and input `http://localhost:80` in the search bar
- In the website, try input some sql injection commands to hack into the website.

e.g. Input `'OR 1=1 -- `(last character is space) in username. 

![example](https://i.imgur.com/ZStv72Q.png)

If successful, you should see this page

![example](https://i.imgur.com/Q4uDYdC.png)
