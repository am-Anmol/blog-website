create database blogdata;
use blogdata;
create table User(UserId int auto_increment primary key, Name varchar(100), Email varchar(100),Password varchar(100));

desc user;

create table Blogs(BlogId int auto_increment primary key, blogTitle varchar(250),blogDesc text,blogImg blob, createTime date, UserId int, isActive varchar(50),foreign key(UserId) references User(UserId));