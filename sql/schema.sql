CREATE TABLE IF NOT EXISTS clima (
    id SERIAL PRIMARY KEY,
    cidade TEXT NOT NULL,
    temperatura NUMERIC(5,1),
    vento NUMERIC(5,1),
    dthora_coleta TIMESTAMP NOT NULL
)