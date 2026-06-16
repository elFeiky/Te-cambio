import requests
import sys

def tasa_cambio(moneda_origen, moneda_destino):
    url = f"https://api.frankfurter.app/latest?from={moneda_origen.upper()}&to={moneda_destino.upper()}"
    response = requests.get(url)
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        datos = response.json()
        tasa = datos["rates"][moneda_destino.upper()]
        return tasa
    
    except requests.exceptions.HTTPError:
        print("Error: No se pudo obtener la tasa de cambio. Verifique las monedas ingresadas.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar al servicio de tasas de cambio. Verifique su conexión a Internet.")
        return None
    except requests.exceptions.Timeout:
        print("Error: La solicitud al servicio de tasas de cambio ha excedido el tiempo de espera.")
        return None
    except Exception as e:
        print("Error inesperado")
        return None

def main():
    print("Cambia tu moneda capo")

    origen = input("Ingrese la moneda de origen (ejemplo: USD): ").strip()
    destino = input("Ingrese la moneda de destino (ejemplo: EUR): ").strip()
    
    try:
        cantidad = float(input("Cuanto quieres cambiar? "))
    except ValueError:
        print("Error: Ingresa un valor valido.")
        sys.exit(1)

    print(f"\n Obteniendo tasa de cambio...")
    tasa = tasa_cambio(origen, destino)

    if tasa:
        cambio = cantidad * tasa
        print(f"\n {cantidad} {origen.upper()} son aproximadamente {cambio:.2f} {destino.upper()} (Tasa: {tasa})")
    else:
        print("No se pudo calcular el cambio debido a un error en la obtención de la tasa.")
if __name__ == "__main__":    main()