# JasnikSite
# JasnikSite

Tento projekt je jednoduchá webová aplikace postavená na Flask frameworku, která umožňuje správu uživatelů.

## Požadavky

  requirements.txt

## Instalace

1. Naklonujte repozitář:
    ```sh
    git clone https://github.com/vase-uzivatelske-jmeno/jasnikSite.git
    ```
2. Přejděte do adresáře projektu:
    ```sh
    cd jasnikSite/JasnikSite
    ```
3. Vytvořte a aktivujte virtuální prostředí:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Na Windows použijte `venv\Scripts\activate`
    ```
4. Nainstalujte požadované balíčky:
    ```sh
    pip install -r requirements.txt
    ```

## Spuštění aplikace

1. Spusťte aplikaci:
    ```sh
    python app.py
    ```
2. Otevřete webový prohlížeč a přejděte na adresu:
    ```
    http://127.0.0.1:5000/
    ```

## Použití

- Na hlavní stránce se zobrazí seznam uživatelů.
- Přidání nového uživatele je možné přes formulář na `/add`.
- Smazání uživatele je možné kliknutím na odkaz "Smazat" vedle uživatele.
