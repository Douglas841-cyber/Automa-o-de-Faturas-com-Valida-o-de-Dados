from imap_tools import MailBox,AND
import os 
from dotenv import load_dotenv

load_dotenv()

def busca_email_fatura():
    
    email = os.getenv("EMAIL_USER")
    senha = os.getenv("EMAIL_PASS")
    servidor = os.getenv("EMAIL_SERVER","imap.gmail.com")

    print(f"🔏 Conectando ao e-mail {email} via {servidor}...")

    os.makedirs("anexos",exist_ok=True)
    anexos_pdf = []

    with MailBox(servidor).login(email,senha, initial_folder = 'INBOX') as mailbox: 
        for msg in mailbox.fetch(AND(seen=False),reverse=True, limit=10):
            print(f"📧 e-mail encontrado: {msg.subject}")
            for anexo in msg.attachments:
                print(f"📎anexo encontrados:",{anexo.filename})
                if anexo.filename and anexo.filename.lower().endswith(".pdf"):
                    caminho = f"anexo/{anexo.filename}"
                    with open(caminho, "wb") as f:
                        f.write(anexo.payload)
                        print(f"✅PDF salvo: {caminho}")
                        anexos_pdf.append(caminho)
    print(f"📊 Total de PDFs encontrados: {len(anexos_pdf)}")
    print(f"📊 Total de PDFs na lista: {(anexos_pdf)}")
    return anexos_pdf
    





    
 
