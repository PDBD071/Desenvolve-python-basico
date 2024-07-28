import csv

def process_file(file_path):
    top_tracks_per_year = {year: None for year in range(2012, 2023)}
    
    with open(file_path, mode='r', encoding='latin-1') as file:
        reader = csv.reader(file)
        next(reader)  # Pular cabeçalho
        
        for row in reader:
            try:
                # Verifica se a linha tem exatamente 24 colunas
                if len(row) != 24:
                    continue
                
                track_name = row[0].strip()
                artist_name = row[1].strip()
                artist_count = int(row[2].strip())
                released_year = int(row[3].strip())
                streams = int(row[8].strip())
                
                # Ignora músicas fora do intervalo de anos 2012 a 2022
                if released_year < 2012 or released_year > 2022:
                    continue
                
                # Ignora linhas com mais de um artista não entre aspas
                if artist_count > 1 and not artist_name.startswith('"'):
                    continue

                # Verifica se a música tem nomes entre aspas
                if track_name.startswith('"') and track_name.endswith('"'):
                    track_name = track_name[1:-1]

                if artist_name.startswith('"') and artist_name.endswith('"'):
                    artist_name = artist_name[1:-1]

                # Atualiza o top track do ano se o atual é menor em streams
                if top_tracks_per_year[released_year] is None or streams > top_tracks_per_year[released_year][3]:
                    top_tracks_per_year[released_year] = [track_name, artist_name, released_year, streams]
            except ValueError:
                continue

    # Filtra apenas os anos de 2012 a 2022 e remove entradas None
    top_tracks_list = [track for track in top_tracks_per_year.values() if track is not None]
    return top_tracks_list

# Caminho para o arquivo CSV
file_path = r'C:\Users\PDBD071\OneDrive\Área de Trabalho\python\spotify_2023.csv'

# Processa o arquivo e obtém a lista de músicas
top_tracks_list = process_file(file_path)

# Exibe a lista produzida
for track in top_tracks_list:
    print(track)

