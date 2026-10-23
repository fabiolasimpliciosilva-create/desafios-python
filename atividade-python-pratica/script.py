# script.py
# Atividade Prática de Python

def converter_dolar_para_real(valor_dolar, cotacao_atual):
    """Função que recebe o valor em dólar e a cotação e retorna o valor em reais."""
    return valor_dolar * cotacao_atual

def main():
    print("--- CONVERSOR DE MOEDAS (USD -> BRL) ---")
    
    try:
        # Entrada de dados do usuário
        dolar = float(input("Digite o valor em Dólares (USD): $ "))
        cotacao = float(input("Digite a cotação atual do Dólar: R$ "))
        
        # Processamento
        resultado = converter_dolar_para_real(dolar, cotacao)
        
        # Saída de dados formatada
        print(f"\n💵 $ {dolar:.2f} USD equivalem a 💵 R$ {resultado:.2f} BRL")
        print("-----------------------------------------")
        
    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos válidos.")

if __name__ == "__main__":
    main()
