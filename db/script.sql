create database MBViajens;
use MBViajens;

create table contato (
    id int auto_increment primary key,
    ir_de varchar(255) not null,
    ir_para varchar(255) not null,
    data_ida date,
    data_volta date,
    descrição varchar(255) not null
);