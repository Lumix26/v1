import base64
import os
import json


from fastapi import FastAPI
from .utility.dto.Request import Request as DTOrequest
from .utility.fileHandler.utils import fetch_content_in_file


app = FastAPI()


@app.post("/api/fetchContent")
def fetchContent(request: DTOrequest):

    try:

        #Decodifico il contenuto del payload, ovvero il flusso di byte codificato in base64
        decoded = base64.b64decode(request.encoded_file)

        #Verifico che il file non esista già localmente
        if not os.path.exists(f"./files/{request.file_name}.pdf"):

            #Al primo avvio non esisterà neanche la cartella files, di conseguenza
            #il controllo darà false, e dovra essere creata.
            if not os.path.exists("./files"):
                os.mkdir("./files")
            
            with open(f"{request.file_name}.pdf","wb") as fb:
                fb.write(decoded)
            
        #Metodo stub ancora non implementato, discutere su come implementarlo, specificare successivamente
        #il tipo di ritorn str|None
        output = fetch_content_in_file(header=request.intestazione, description=request.descrizione)

        if output:

            json.dumps(
                {"content": output}
            )

        else:
            
            json.dumps(
                {"message" : "fetch failed"}
            )
            
            
    except Exception as e:
        pass



@app.get("/api/companyInfo")
def getCompanyInformation():
    raise NotImplementedError