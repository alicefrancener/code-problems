"""
  problem: 1019 - Time Conversion
  https://www.urionlinejudge.com.br/judge/en/problems/view/1019
"""

def segundos_para_horas(s):
    h = s // 3600
    s = s % 3600
    m = s // 60
    s = s % 60
    print('{:d}:{:d}:{:d}'.format(h, m, s))
    

total_s = int(input())
segundos_para_horas(total_s)
