import requests
from bs4 import BeautifulSoup


def get_artigo():
    link = "https://pt.wikipedia.org/wiki/Especial:Aleat%C3%B3ria"
    # link = "https://pt.wikipedia.org/wiki/Enzima_conversora_da_angiotensina_2"

    res = requests.get(link)
    soup = BeautifulSoup(res.content, features="html.parser")

    titulo_html = soup.find(id="firstHeading")
    titulo = str(titulo_html.text)

    slug = titulo.replace(" ", "_")
    url = f"https://pt.wikipedia.org/wiki/{slug}"

    paragrafos = soup.find_all("p")
    paragrafos_filtrados = []
    for p in paragrafos:
        if "\t" not in p.text and "Coordenadas" not in p.text and len(p.text) >= 30:
            paragrafos_filtrados.append(str(p.text))

    texto = str(paragrafos_filtrados[0])

    texto = texto.split(". ")[0]

    dados = {"titulo": titulo, "url": url, "texto": texto}

    print(f"{7*'-'} Os dados do artigo são {7*'-'}")
    for dado in dados:
        print(f"\033[32m{dado}\033[0;0m: {dados[dado]}")

    if input("Escolher o artigo? (s/n) ") == "s":
        return dados
    else:
        return "n"


def main():
    continuar = True
    while continuar:
        artigo = get_artigo()
        if artigo == "n":
            print("buscando novo artigo...")
        else:
            print(f"Artigo sobre {artigo['titulo']} escolhido")
            continuar = False
            return artigo


if __name__ == "__main__":
    main()
