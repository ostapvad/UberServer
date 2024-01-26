DROP TABLE IF EXISTS credentials;

CREATE TABLE IF NOT EXISTS credentials (
    id serial PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Insert data into the credentials table
INSERT INTO credentials (username, password) VALUES
    ('user1', '111'),
    ('user2', '222'),
    ('user3', '333'),
    ('user4', '444'),
    ('user5', '555');