import pdfplumber
 
def extrair_texto_pdf(file):
 
    texto = ""
 
    with pdfplumber.open(file) as pdf:
        for pagina in pdf.pages:
            conteudo = pagina.extract_text()
            if conteudo:
                texto += conteudo + "\n"
 
    return texto