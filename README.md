# Quadruped RL — Nauka lokomocji czworonożnego robota

## Opis projektu

Projekt badawczo-inżynierski dotyczący opracowania czworonożnego robota oraz wykorzystania **uczenia ze wzmocnieniem (Reinforcement Learning)** do nauki stabilnej lokomocji.

Projekt zakłada opracowanie modelu robota w środowisku symulacyjnym, przeprowadzenie treningu agenta z wykorzystaniem realistycznej fizyki, a następnie przeniesienie wyuczonego sterowania na rzeczywisty prototyp robota.

Głównym elementem projektu jest zbadanie, **w jakim stopniu sterowanie wyuczone w symulacji może zostać wykorzystane na rzeczywistym urządzeniu**.

---

## Problem badawczy

Sterowanie robotem czworonożnym wymaga odpowiedniej koordynacji wielu napędów oraz utrzymania stabilności podczas ruchu.

Tradycyjne programowanie ruchów polega na ręcznym określaniu trajektorii każdej kończyny. W projekcie zostanie sprawdzone, czy agent wykorzystujący uczenie ze wzmocnieniem może samodzielnie nauczyć się odpowiedniego sterowania na podstawie informacji o stanie robota i otrzymywanej funkcji nagrody.

### Pytanie badawcze

> Czy robot czworonożny może nauczyć się stabilnej lokomocji za pomocą uczenia ze wzmocnieniem w środowisku symulacyjnym oraz w jakim stopniu wyuczone sterowanie można przenieść na rzeczywisty prototyp?

---

## Hipoteza

> Zastosowanie uczenia ze wzmocnieniem w środowisku z realistyczną symulacją fizyki oraz randomizacją parametrów środowiska pozwoli uzyskać stabilną lokomocję robota i zwiększy odporność wyuczonego sterowania na różnice pomiędzy symulacją a rzeczywistym środowiskiem.

---

## Cele projektu

### Cel główny

Opracowanie systemu umożliwiającego nauczenie czworonożnego robota stabilnego poruszania się z wykorzystaniem uczenia ze wzmocnieniem oraz sprawdzenie możliwości transferu wyuczonego sterowania z symulacji do rzeczywistego robota.

### Cele szczegółowe

- zaprojektowanie konstrukcji czworonożnego robota,
- stworzenie modelu robota 3D,
- stworzenie realistycznego środowiska fizycznego w Unity,
- implementacja układu napędowego robota,
- umożliwienie ręcznego sterowania robotem w symulacji,
- stworzenie środowiska treningowego dla agenta RL,
- opracowanie funkcji nagrody,
- nauczenie agenta utrzymywania stabilnej pozycji,
- nauczenie agenta chodzenia,
- przeprowadzenie eksperymentów z różnymi parametrami fizycznymi,
- zastosowanie randomizacji parametrów symulacji,
- zbudowanie rzeczywistego prototypu,
- przeniesienie wyuczonego modelu na rzeczywiste urządzenie,
- porównanie zachowania robota w symulacji i rzeczywistości,
- analiza wyników oraz ograniczeń zastosowanej metody.

---

## Konstrukcja robota

Pierwsza wersja prototypu zakłada:

- 4 kończyny,
- 2 stopnie swobody na każdą kończynę,
- łącznie 8 serwomechanizmów,
- serwomechanizmy MG996R,
- własną konstrukcję mechaniczną,
- sterowanie elektroniczne oparte na mikrokontrolerze,
- możliwość późniejszej rozbudowy do większej liczby stopni swobody.

### Wersja V0

Pierwsza wersja projektu nie będzie jeszcze wykorzystywać sztucznej inteligencji.

Celem V0 jest stworzenie poprawnie działającej symulacji fizycznej robota.

Zakres V0:

- model 3D,
- Rigidbody,
- collidery,
- połączenia mechaniczne,
- ograniczenia ruchu stawów,
- masa elementów,
- grawitacja,
- tarcie,
- sterowanie serwomechanizmami,
- ręczne sterowanie robotem,
- test stabilności.

---

## Rozwój projektu

```text
V0 — Symulacja fizyczna
 │
 ├── Model 3D
 ├── Mechanika
 ├── Fizyka
 └── Sterowanie ręczne
        │
        ▼
V1 — Nauka stabilności
 │
 ├── Reinforcement Learning
 ├── Funkcja nagrody
 └── Nauka utrzymywania pozycji
        │
        ▼
V2 — Nauka chodzenia
 │
 ├── Lokomocja
 ├── Koordynacja nóg
 └── Pomiar skuteczności
        │
        ▼
V3 — Odporność
 │
 ├── Randomizacja fizyki
 ├── Szum sensorów
 ├── Różne powierzchnie
 └── Przeszkody
        │
        ▼
V4 — Robot rzeczywisty
 │
 ├── Konstrukcja
 ├── Elektronika
 └── Firmware
        │
        ▼
V5 — Sim-to-Real
 │
 ├── Transfer modelu
 ├── Testy rzeczywiste
 ├── Porównanie z symulacją
 └── Analiza wyników
```

---

## Technologie

### Symulacja

- Unity
- C#
- Unity Physics
- Rigidbody
- Joint / Configurable Joint
- Unity ML-Agents

### AI

- Reinforcement Learning
- Python
- PyTorch
- ML-Agents

### Robot

- MG996R
- mikrokontroler
- serwokontroler
- czujniki
- zasilanie własne

### Projektowanie

- CAD
- modelowanie 3D
- druk 3D

---

## Metodyka

Projekt będzie realizowany zgodnie z następującym schematem:

**Problem → Hipoteza → Model → Eksperyment → Wyniki → Analiza → Wniosek**

Każdy istotny etap będzie dokumentowany w repozytorium.

Wyniki eksperymentów będą zapisywane w sposób umożliwiający ich późniejsze porównanie.

Przykładowe mierzone parametry:

- czas utrzymania stabilności,
- prędkość poruszania się,
- przebyta odległość,
- liczba upadków,
- zużycie energii,
- stabilność podczas pokonywania przeszkód,
- różnica pomiędzy symulacją a rzeczywistym prototypem.

---

## Struktura projektu

```text
quadruped-rl/
│
├── README.md
│
├── docs/
│   ├── cele.md
│   ├── koncepcja.md
│   ├── metodologia.md
│   └── eksperymenty.md
│
├── simulation/
│   └── unity/
│
├── robot/
│   ├── cad/
│   ├── electronics/
│   └── firmware/
│
├── ai/
│   ├── training/
│   └── models/
│
├── experiments/
│
└── results/
```

---

## Status projektu

**Aktualna wersja: V0 — planowanie projektu**

Następny etap:

> Utworzenie pierwszej symulacji fizycznej pojedynczej kończyny, a następnie całego robota.

---

## Zastosowanie

Projekt jest rozwijany jako projekt badawczo-inżynierski związany z:

- robotyką,
- mechatroniką,
- automatyką,
- sztuczną inteligencją,
- uczeniem ze wzmocnieniem,
- symulacją fizyczną,
- projektowaniem urządzeń,
- transferem rozwiązań z symulacji do rzeczywistości.

Projekt jest planowany również jako materiał do udziału w konkursach i olimpiadach związanych z techniką, mechatroniką i innowacjami.
