CREATE TABLE IF NOT EXISTS clima (
    id SERIAL PRIMARY KEY,
    cidade TEXT NOT NULL,
    temperatura NUMERIC(5,1),
    vento NUMERIC(5,1),
    observado_em TIMESTAMP NOT NULL,
    dthora_coleta TIMESTAMP NOT NULL,
    CONSTRAINT uq_cidade_observado UNIQUE (cidade, observado_em)
);