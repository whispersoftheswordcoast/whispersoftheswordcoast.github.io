import os

def estrai_intestazioni_da_file(file_path):
    intestazioni = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                intestazioni.append(line)
    return intestazioni

def estrai_intestazioni_da_cartella_corrente():
    cartella_corrente = os.getcwd()
    md_files = [f for f in os.listdir(cartella_corrente) if f.endswith('.md')]
    for file_name in md_files:
        full_path = os.path.join(cartella_corrente, file_name)
        intestazioni = estrai_intestazioni_da_file(full_path)
        salva_indice_su_file(file_name, intestazioni)

def salva_indice_su_file(nome_file_md, intestazioni):
    nome_file_txt = f"indice_{nome_file_md.replace('.md', '')}.txt"
    with open(nome_file_txt, 'w', encoding='utf-8') as f:
        f.write(f"Indice intestazioni per il file: {nome_file_md}\n\n")
        for header in intestazioni:
            f.write(header + "\n")
    print(f"Indice salvato in: {nome_file_txt}")

if __name__ == "__main__":
    estrai_intestazioni_da_cartella_corrente()
