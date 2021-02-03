"""
  author: Alice Francener
  problem: 1257 - Array Hash
  description: https://www.urionlinejudge.com.br/judge/en/problems/view/1257
"""

nTrials = int(input())
hashs = []

for trial in range(nTrials):
    nLines = int(input())
    hash = 0
    for line in range(nLines):
        phrase = input()
        for charPosition in range(len(phrase)):
            char = phrase[charPosition]
            # ASCII: A = 65, Z = 90
            if ord(char) in range(65, 91):
                hash += ord(char)-65 + line + charPosition
    hashs.append(hash)

for h in hashs:
    print(h)
