# -*- coding: utf-8 -*-
horas_string = input()
minutos_sono = []

while horas_string != '0 0 0 0':
    horas_string = horas_string.split(' ')
    h_inicio = int(horas_string[0])
    m_inicio = int(horas_string[1])
    h_fim = int(horas_string[2])
    m_fim = int(horas_string[3])
    if h_inicio == 0 and m_inicio == 0 and h_fim == 0 and m_fim == 0:
        break
    # calcular minutos de sono
    minutos_sono.append(0)
    if h_inicio == h_fim:
        # caso horas iguais mesmo dia
        if m_inicio < m_fim:
            minutos_sono[len(minutos_sono) - 1] = m_fim - m_inicio
        # caso horas iguais dias diferentes
        else:
            minutos_sono[len(minutos_sono) - 1] = 24 * 60 - (m_inicio - m_fim)
    else:
        # caso horas diferentes mesmo dia
        if h_inicio < h_fim:
            minutos_sono[len(minutos_sono) - 1] = (
                (h_fim - h_inicio) * 60) - (m_inicio - m_fim)
        # caso horas diferentes dias diferentes
        else:
            minutos_sono[len(minutos_sono) - 1] = (
                (24 - h_inicio) * 60) - m_inicio + (h_fim * 60) + m_fim
    # ler próximo hora
    horas_string = input()

for minutos in minutos_sono:
    print(minutos)
