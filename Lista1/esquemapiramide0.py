input_n = int(input())

minhaLinha = ""


for i in range(input_n):
    minhaLinha += "*"*(i*2+1)
    print(minhaLinha)
    minhaLinha = ""
