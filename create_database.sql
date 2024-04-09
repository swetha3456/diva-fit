create table users(
    username varchar(40) PRIMARY KEY,
    password varchar(60),
    age int,
    weight float,
    avg_cycle_length int,
    avg_period_duration int,
    next_period_start_date date,
    default_difficulty smallint,
    fitness_goals varchar(200),
    health_conditions varchar(200)
);