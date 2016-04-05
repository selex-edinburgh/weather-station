drop table if exists entries;
create table entries(
	datetime timestamp primary key,
	inches numeric not null
);