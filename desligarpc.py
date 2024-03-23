import os

def agendar_desligamento(tempo_em_minutos):
    os.system(f'shutdown /s /t {tempo_em_minutos * 60}')

# Defina o tempo em minutos para o desligamento
tempo_em_minutos = 180  # Por exemplo, 60 minutos

agendar_desligamento(tempo_em_minutos)