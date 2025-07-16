import pdfplumber
import re

def extrair_dados_faturas(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ''
        for pagina in pdf.pages:
            texto += pagina.extract_text()
            print(f"📄 Texto extraído do PDF:\n{texto}\n")

    # Expressões regulares para extrair dados
    cnpj = re.search(r"CNPJ[:\s]+([\d./-]+)", texto)
    contrato = re.search(r"Contrato[:\s]+(\d+)", texto)
    valor = re.search(r"Valor Total[:\s]*R?\$?\s?([\d.,]+)", texto)
    vencimento = re.search(r"Vencimento[:\s]+(\d{2}/\d{2}/\d{4})", texto)

    print(f"🔍valor do cnpj após pesquisa: {cnpj}")
    print(f"🔍valor do contrato após pesquisa: {contrato}")
    print(f"🔍valor do valor após pesquisa: {valor}")
    print(f"🔍valor do vencimento após pesquisa: {vencimento}")
          
    dados = {
        "cnpj": cnpj.group(1) if cnpj else "não encontrado",
        "contrato": contrato.group(1) if contrato else "não encontrado",
        "valor": float(valor.group(1).replace('.', '').replace(',', '.')) if valor else 0.0,
        "vencimento": vencimento.group(1) if vencimento else "não encontrado"
    }
    print(f"\n📦 Dicionário final:\n{dados}")

    return dados