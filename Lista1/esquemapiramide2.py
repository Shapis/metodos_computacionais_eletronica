input_n = int(input())

minhaLinha = ""


for i in range(input_n):
    minhaLinha += "  "*(input_n-i-1)
    minhaLinha += f"{i+1}"*(i*2+1)
    print(minhaLinha)
    minhaLinha = ""

for i in range(input_n-2, -1, -1):
    minhaLinha += "  "*(input_n-i-1)
    minhaLinha += f'{i+1}'*(i*2+1)
    print(minhaLinha)
    minhaLinha = ""
