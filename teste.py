import pyperclip

# Caminho base dos arquivos de imagem
base_path = r"C:\Users\Dell\Pictures\WallPapers\data\frame"

# Número inicial e final dos frames
start_frame = 862
end_frame = 1604

# Gerando a lista de caminhos
file_paths = [f"{base_path}{i}.jpg" for i in range(start_frame, end_frame + 1)]

# Juntando tudo em uma única string, separada por quebras de linha
output_text = "\n".join(file_paths)

# Copiando para a área de transferência
pyperclip.copy(output_text)

print("Caminhos copiados para a área de transferência.")
