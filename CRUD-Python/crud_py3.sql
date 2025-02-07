create database crud_py;

use crud_py;

create table usuario (
	id int not null auto_increment,
    nome varchar(150) not null,
    cpf char(11),
    email varchar(150),
    senha varchar(150),
    primary key (id)
);

select * from usuario;

create table produto (
	id_prod int not null auto_increment,
    nome varchar(100) not null,
    descricao text not null,
    marca varchar(50) not null,
    modelo varchar(50) not null,
    preco float(6,2) not null,
    qte int not null,
    cor varchar(45) not null,
    peso varchar(45) not null,
    primary key (id_prod)
);

select * from produto;

