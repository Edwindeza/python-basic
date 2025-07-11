from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import time

# Configurar el driver
driver = webdriver.Chrome()

try:
    url = 'https://www.alkosto.com/search?text=neveras'
    driver.get(url)
    
    # Esperar a que la página cargue completamente
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ais-InfiniteHits-item')))
    
    # Usar find_elements (plural) para obtener todos los elementos
    li_elements = driver.find_elements(By.CLASS_NAME, 'ais-InfiniteHits-item')
    data = []
    
    print(f"Encontrados {len(li_elements)} elementos")
    
    for element in li_elements:
        try:
            titulo_element = element.find_element(By.TAG_NAME, 'h3')
            precio_element = element.find_element(By.CLASS_NAME, 'price')
            imagen_element = element.find_element(By.TAG_NAME, 'img').get_attribute('src')
            
            data.append({
                'Titulo': titulo_element.text,
                'Precio': precio_element.text,
                'Imagen': imagen_element
            })
        except NoSuchElementException as e:
            print(f"Error al extraer datos de un elemento: {e}")
            continue
    
    # Crear DataFrame y guardar datos
    if data:
        df = pd.DataFrame(data)
        print(f"Se extrajeron {len(data)} productos")
        print(df.head())
        
        # Guardar en CSV
        df.to_csv('productos_alkosto.csv', index=False, encoding='utf-8')
        print("Datos guardados en 'productos_alkosto.csv'")
    else:
        print("No se encontraron datos para extraer")

except TimeoutException:
    print("Error: La página tardó demasiado en cargar")
except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    # Cerrar el navegador
    driver.quit()
    print("Navegador cerrado")