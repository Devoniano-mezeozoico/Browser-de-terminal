import requests
from bs4 import BeautifulSoup

def clean_text(text):
    return ' '.join(text.strip().split())

def search_duckduckgo(query):
    print(f"\n🔎 Resultados para: '{query}'\n")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://html.duckduckgo.com/html/?q={query}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"[Erro] Falha na busca: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for result in soup.find_all('a', class_='result__a'):
        title = clean_text(result.text)
        href = result.get('href')
        results.append((title, href))

    if not results:
        print("Nenhum resultado encontrado.")
    else:
        for i, (title, href) in enumerate(results, 1):
            print(f"{i:02d}. {title}\n    ↳ {href}")

    return results

def terminal_search_browser():
    print("="*60)
    print("🕸️  Terminal Search Browser")
    print("Digite 'sair' para encerrar.")
    print("="*60)

    while True:
        query = input("\nPesquisar: ").strip()
        if query.lower() == "sair":
            print("Encerrando.")
            break
        elif query:
            search_duckduckgo(query)
        else:
            print("Por favor, digite algo para buscar.")

if __name__ == "__main__":
    terminal_search_browser()
