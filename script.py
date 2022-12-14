import requests
from bs4 import BeautifulSoup


def get_artigo():
    link = "https://pt.wikipedia.org/wiki/Especial:Aleat%C3%B3ria"

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

    if len(dados["texto"]) + len(dados["titulo"]) + len(dados["url"]) > 240:
        print(
            "\033[31m(twitter) O tamanho das strings ultrapassa 240 caracteres. É recomendado escolher outro artigo. \033[0;0m"
        )

    artigos = open("artigos.txt", "r")
    if dados["titulo"] in artigos.read():
        print(
            "\033[31m(twitter) O artigo foi encontrado na lista de artigos já escolhidos. Se não quiser repetir, escolha outro artigo. \033[0;0m"
        )
    artigos.close()

    if input("Escolher o artigo? (s/n) ") == "s":
        artigos = open("artigos.txt", "a")
        artigos.write(f"{dados['titulo']}\n{dados['texto']}\n{dados['url']}\n\n")
        print("\033[32mtítulo e url salvos \033[0;0m")
        artigos.close()

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
