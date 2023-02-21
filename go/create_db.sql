CREATE TABLE IF NOT EXISTS "routes" (
  "id" integer PRIMARY KEY,
  "name" varchar(128) UNIQUE NOT NULL,
  "url" varchar(256) UNIQUE NOT NULL,
  "icon" varchar(32) default "go.png",
  "active" integer default 1 NOT NULL,
  "hits" int default 0 NOT NULL,
  "last_access" timestamp default CURRENT_TIMESTAMP NOT NULL
);
