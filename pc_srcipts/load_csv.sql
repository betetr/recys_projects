use recys;
load data local infile 'E:\\projects\\recys\\dataset\\tianchi_mobile_recommend_train_user.csv'
into table train_user character set utf8
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\n';

-- E:\\projects\\recys\\scripts\\load_csv.sql