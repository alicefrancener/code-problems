"""
  problem: 1020 - Age in Days
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1020
"""

# -*- coding: utf-8 -*-

def idade(dias):
  anos = dias // 365
  dias %= 365
  meses = dias // 30
  dias %= 30
  print('{:d} ano(s)\n{:d} mes(es)\n{:d} dia(s)'.format(anos, meses, dias)) 

dias = int(input())
idade(dias)
