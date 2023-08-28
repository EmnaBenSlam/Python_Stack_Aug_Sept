USE users;
INSERT INTO users(first_name, last_name, email) VALUES ('emna','Benslama','emnabensl@gmail.com');
INSERT INTO users(first_name, last_name, email) VALUES ('Mohamed','Bouali', 'mohamedb@gmail.com');
INSERT INTO users(first_name, last_name, email) VALUES ('Hatem','Chtourou', 'hatemch@gmail.com');

SELECT * FROM users
ORDER BY first_name DESC;
