from email_reader import busca_email_fatura
from pdf_extrair import extrair_dados_faturas

def main():

    pdfs = busca_email_fatura()

    for pdf in pdfs:
        print(f"\nVou processar: {pdf}\n")
        dados_fatura = extrair_dados_faturas(pdf)

if __name__ == "__main__":

    main()


