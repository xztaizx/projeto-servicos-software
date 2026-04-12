from transformers import pipeline
 
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)
 
def dividir_texto(texto, tamanho=1000):
    return [texto[i:i+tamanho] for i in range(0, len(texto), tamanho)]
 
def resumir_texto(texto):
 
    partes = dividir_texto(texto)
 
    resumos = []
 
    for parte in partes:
        resumo = summarizer(parte, max_length=150, min_length=40)
        resumos.append(resumo[0]["summary_text"])
 
    return " ".join(resumos)