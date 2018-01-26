use recys;
drop table if exists train_user;
create table train_user(
  user_id varchar(255)
  ,item_id varchar(255)
  ,behavior_type varchar(255)
  ,user_geosh varchar(255)
  ,item_category varchar(255)
  ,time varchar(255)
)
;
-- E:\\projects\\recys\\scripts\\0_init_train_user.sql