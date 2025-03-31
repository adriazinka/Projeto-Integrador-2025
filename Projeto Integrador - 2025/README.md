# Repositótio oficial de referência para o projeto integrador
## Turma do curso técnico em informática 22 
## Senac Jaboticabal

* Infraestrutura básica
* Servidor Linux Ubuntu 24.04
* Docker 27.5.1
* MySQL 9.2.0
* Python 3.10 ou superior
** Bibliotecas tkinter, flask, mysql-connection-python

* sudo docker build -t usuario/mysql:1.0 .
* sudo docker run -d -p 3306:3306 --name mysql usuario/mysql:1.0
