import requests
from bs4 import BeautifulSoup

# URL de la página que quieres scrapear
url = 'https://www.winesofargentina.org/en/wineries'

# Realizar la solicitud HTTP
response = requests.get(url)
link_vino = []

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscar todos los enlaces de las bodegas utilizando la clase 'linkTotal'
    links = soup.find_all('a', class_='linkTotal')
    
    if not links:
        print("No se encontraron bodegas.")
    else:
        # Recoger todos los enlaces completos
        for link in links:
            href = link.get('href')
            if href:  # Verifica que el enlace exista
                # Si el enlace es relativo, añadir el dominio principal
                if href.startswith('/'):
                    href = f'https://www.winesofargentina.org{href}'
                link_vino.append(href)

        # Iterar sobre cada enlace de bodega y extraer la información deseada
        for winery in link_vino:
            wine_response = requests.get(winery)
            
            if wine_response.status_code == 200:
                wine_soup = BeautifulSoup(wine_response.content, 'html.parser')

                # Ajusta los selectores según la estructura HTML de la página de la bodega
                name = wine_soup.find('h1', class_='winery-name').text.strip() if wine_soup.find('h1', class_='winery-name') else "Nombre no encontrado"
                location = wine_soup.find('p', class_='winery-location').text.strip() if wine_soup.find('p', class_='winery-location') else "Ubicación no encontrada"
                description = wine_soup.find('div', class_='winery-description').text.strip() if wine_soup.find('div', class_='winery-description') else "Descripción no encontrada"

                print(f'Nombre: {name}')
                print(f'Ubicación: {location}')
                print(f'Descripción: {description}')
                print('-' * 50)
            else:
                print(f'Error al acceder al vino en: {winery}')
else:
    print(f'Error al acceder a la página: {response.status_code}')
