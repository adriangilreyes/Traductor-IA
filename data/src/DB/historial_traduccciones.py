CREATE TABLE traducciones(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto_original TEXT NOT NULL,
    traducccion TEXT NOT NULL,
    src_lang TEXT NOT NULL,
    tgt_lang TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 


