[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Sistem za upravljanje skladištem je REST API aplikacija namijenjena za evidenciju i upravljanje proizvodima i dobavljačima u skladištu. Aplikacija omogućava kreiranje, pregled, ažuriranje i brisanje podataka o proizvodima i dobavljačima, kao i praćenje dostupnosti proizvoda, količine na stanju i povezanosti proizvoda sa odgovarajućim dobavljačima. Svrha aplikacije je olakšati organizaciju skladišnog poslovanja i upravljanje zalihama.

## Tim

- **Student A**: Šejla Valjevac - resurs: `/resursi_a`
- **Student B**: Edna Avdić - resurs: `/resursi_b`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/resursi_a`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/products` | Lista svih resursa (sa query filterom) |
| GET | `/products/{products_id}` | Dohvatanje resursa po ID-u |
| POST | `/products` | Kreiranje novog resursa |
| PUT | `/products/{products_id}` | Potpuna zamjena resursa |
| PATCH | `/products/{products_id}` | Djelimično ažuriranje resursa |
| DELETE | `/products/{products_id}` | Brisanje resursa |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/resursi_a" \
  -H "Content-Type: application/json" \
  -d '{"polje1": "vrijednost", "polje2": 123}'
```

### Resurs B: `/resursi_b`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/suppliers/` | Lista svih resursa |
| POST | `/suppliers/` | Kreiranje novog resursa |
| GET | `/suppliers/{supplier_id}` | Dohvatanje resursa po ID-u |
| PUT | `/suppliers/{supplier_id}` | Potpuna zamjena resursa |
| PATCH | `/suppliers/{supplier_id}` | Djelimično ažuriranje resursa |
| DELETE | `/suppliers/{supplier_id}` | Brisanje resursa |


## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / Google Gemini ...]
**Model:** [GPT-4, Copilot model, Gemini 3 Flash ...]

**Primjer 1:**
- **Prompt:** Kako dodati query filter po kategoriji u GET /products endpoint u FastAPI?
- **Kako je pomoglo:** AI alat mi je pomogao pri implementaciji filtriranja proizvoda po kategoriji u GET /products endpointu i boljem razumijevanju rada query parametara u FastAPI-u.
- **Prilagodbe:** Generisani kod nisam morala prilagoditi.

**Primjer 2:**
- **Prompt:** Možeš li mi predložiti atribute za model Supplier koji su tipa bool i Optional, kako bih poboljšala funkcionalnost baze?
- **Kako je pomoglo:** Dobila sam više konkretnih primjera koji proširuju osnovni model uz objašnjenje kako svaki od njih utiče na funkcionalnost API-ja i validaciju podataka.
- **Prilagodbe:** Odabrala sam atribute is_active i supports_return (bool) te za opciona polja sam dodala last_delivery_date (datetime) i discount_rate (float) jer su najrelevantniji za entitet dobavljača te sam ih integrisala u SupplierCreate i SupplierUpdate klase kako bi bili dostupni i pri kreiranju i pri ažuriranju.

## Napomene

[Dodatne napomene specifične za vašu implementaciju]