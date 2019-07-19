create table users (
	userid serial not null primary key
,	name varchar(32) not null
,	registered timestamp not null default now()
,	isadmin boolean default false
);

create table tokens (
	token varchar(64) not null primary key
,	owner not null references users(userid)
);

create table endpoints (
	endpointname varchar(32) not null primary key
,	registered timestamp not null default now()
,	ispublic boolean default false
);

create table token_endpoints (
	endpointname varchar(32) not null references endpoints(endpointname)
,	token varchar(64) not null references tokens(token)
,	registered timestamp not null default now()
);
