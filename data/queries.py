sql_queries = []

sql_queries.append("create schema if not exists bot")

sql_queries.append("create schema if not exists file_link")

sql_queries.append("create schema if not exists weather")

sql_queries.append("""create table if not exists bot.users
                      (
    user_id    bigint                  not null
        primary key,
    first_name varchar,
    last_name  varchar,
    username   varchar,
    lang       varchar                 not null,
    last_seen  timestamp default now() not null,
    apps       jsonb     default '{}'::jsonb
                      );""")

sql_queries.append("""create table if not exists file_link.storage
                      (
    file_id      varchar not null,
    content_type varchar,
    code         varchar unique
                      );""")

sql_queries.append("""create table if not exists weather.users
                      (
    user_id    bigint not null,
    unit       varchar default 'metric',
    cities     TEXT[]
        );""")
