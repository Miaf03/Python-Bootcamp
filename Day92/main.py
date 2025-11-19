import os
import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def get_page(url):
    """Descarga una página y devuelve su HTML.  
    Devuelve None si la página NO existe (404)."""
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener {url}: {e}")
        return None


def scrape_page(html):
    """Extrae los libros de una página"""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    articles = soup.select("article.product_pod")
    for art in articles:
        title = art.h3.a["title"]
        availability = art.select_one(".instock.availability").text.strip()

        books.append({
            "title": title,
            "availability": availability
        })

    return books


def scrape_all_pages():
    """Recorre todas las páginas hasta que encuentre una 404"""
    all_books = []

    print("Iniciando scraping...\n")

    for page in range(1, 999):
        url = BASE_URL.format(page)
        print(f"Scrapeando: {url}")

        html = get_page(url)

        if html is None:
            print(f"\nFin del scraping")
            break

        books = scrape_page(html)
        all_books.extend(books)

    return all_books


def save_to_csv(books, folder="output", filename="books.csv"):
    """Guarda los datos en un archivo CSV dentro de una carpeta creada automáticamente"""
    
    # Crear carpeta si no existe
    os.makedirs(folder, exist_ok=True)
    
    # Ruta completa
    filepath = os.path.join(folder, filename)

    # Guardar archivo
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "availability"])
        writer.writeheader()
        writer.writerows(books)

    print(f"Archivo CSV generado en: {filepath}")


def main():
    books = scrape_all_pages()
    save_to_csv(books)


if __name__ == "__main__":
    main()