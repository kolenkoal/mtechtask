CREATE DATABASE mtekhtest;

\c;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE log_entries (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    ip_address VARCHAR NOT NULL,
    http_method VARCHAR NOT NULL,
    uri VARCHAR NOT NULL,
    http_status INTEGER NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);