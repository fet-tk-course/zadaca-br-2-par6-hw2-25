[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Sistem za upravljanje skladištem je REST API aplikacija namijenjena za evidenciju i upravljanje proizvodima i dobavljačima u skladištu. Aplikacija omogućava kreiranje, pregled, ažuriranje i brisanje podataka o proizvodima i dobavljačima, kao i praćenje dostupnosti proizvoda, količine na stanju i povezanosti proizvoda sa odgovarajućim dobavljačima. Svrha aplikacije je olakšati organizaciju skladišnog poslovanja i upravljanje zalihama.

## Tim

- **Student A**: Šejla Valjevac - resurs: `/resursi_a`
- **Student B**: [Ime Prezime] - resurs: `/resursi_b`

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

[Analogno kao za Resurs A]

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** [GPT-4, Copilot model, ...]

**Primjer 1:**
- **Prompt:** Kako dodati query filter po kategoriji u GET /products endpoint u FastAPI?
- **Kako je pomoglo:** AI alat mi je pomogao pri implementaciji filtriranja proizvoda po kategoriji u GET /products endpointu i boljem razumijevanju rada query parametara u FastAPI-u.
- **Prilagodbe:** Generisani kod nisam morala prilagoditi.

**Primjer 2:**
- **Prompt:** [Npr. "Implementiraj PATCH endpoint sa exclude_unset=True"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Opis]

## Napomene

[Dodatne napomene specifične za vašu implementaciju]

## Provjera zadace
-U ProductCreate dodani su Pydantic validatori za provjeru ispravnosti prilikom kreiranja proizvoda. Provjere su: naziv proizvoda ne smije biti prazan string i kolicina proizvoda mora biti veca od nule.
U POST endpoint dodana je provjera duplikata koja sprecava kreiranje proizvoda sa istim nazivom. Ukoliko postoji proizvod sa istim nazivom vraca se HTTP 409 Conflict status.
GET /count endpoint vraca ukupan broj proizvoda u bazi podataka. 
-Zahtjev GET /products/count i vraca ukupan broj proizvoda. Zahtjev POST /products, ukoliko je naziv generise se greska. Zahtjev POST /products, ukoliko je kolicina manja od 0 generise se greska. Zahtjev POST /products, ukoliko postoji proizvod sa tim imenom generise se greska.
-U Products supplier_id predstavlja strani kljuc izmedju products i suppliers.
-Validacijska pravila: naziv proizvoda ne smije biti prazan, kolicina proizvoda ne smije biti manja od 0. Moguce greske su naziv proizvoda ne smije biti prazan i kolicina proizvoda mora biti veca od 0.
