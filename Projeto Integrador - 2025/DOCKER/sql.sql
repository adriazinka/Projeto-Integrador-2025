USE EMPRESA;

CREATE TABLE adm_users (
    id int AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    cargo VARCHAR(60) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(15) NOT NULL,
    data_criacao DATE NOT NULL DEFAULT (CURRENT_DATE),
    ultimo_login DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
);

INSERT INTO adm_users (nome,cargo,email,senha) VALUES ('Denilson', 'Administrador', 'email@email.com','Senha123');

