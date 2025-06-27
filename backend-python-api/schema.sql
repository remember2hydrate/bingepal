CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR NOT NULL UNIQUE,
  name VARCHAR,
  mail VARCHAR UNIQUE,
  status VARCHAR NOT NULL DEFAULT 'pal'
);

CREATE TYPE userrole AS ENUM ('admin', 'mod', 'pal');

ALTER TABLE users ALTER COLUMN status TYPE userrole USING status::userrole;

CREATE TABLE ratings (
  id SERIAL PRIMARY KEY,
  source VARCHAR NOT NULL,
  source_id VARCHAR NOT NULL,
  username VARCHAR NOT NULL REFERENCES users(username),
  rate_score REAL NOT NULL,
  rate_descr TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE search_logs (
  id SERIAL PRIMARY KEY,
  source VARCHAR NOT NULL,
  source_id VARCHAR NOT NULL,
  type VARCHAR NOT NULL,
  title VARCHAR NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
