-- creates the MySQL server user user_0d_1
CREATE USR IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL ON *.* FOR user_0d_1;
