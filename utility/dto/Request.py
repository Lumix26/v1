from pydantic import BaseModel


class Request(BaseModel):

    encoded_file: str #Base64 encoded
    file_name: str
    mime_type: str

    intestazione: str #Header del paragrafo
    descrizione: str|None #Eventuale descrizione annessa a quel paragrafo