from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import io
 
from pdf_utils import extrair_texto_pdf
from summarizer import resumir_texto
 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.post("/summarize")
 
async def summarize(file: UploadFile = File(...)):
 
    conteudo = await file.read()
 
    pdf_file = io.BytesIO(conteudo)
 
    texto = extrair_texto_pdf(pdf_file)
 
    resumo = resumir_texto(texto)
 
    return {
        "filename": file.filename,
        "summary": resumo
    }