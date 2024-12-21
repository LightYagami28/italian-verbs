# Italian Verb Conjugation 🇮🇹

This program is a simple Python implementation that allows you to conjugate Italian verbs in various tenses. It supports both regular and irregular verbs and allows you to get the conjugation based on the desired verb tense.

## Main Features ⚙️

The program allows you to:

- Conjugate Italian verbs in various tenses (present, past, imperfect, future, conditional, etc.).
- Handle both regular and irregular verbs.
- Get a list of available tenses for each verb.
- View conjugations based on the chosen verb and tense.

## Requirements 📜

- Python 3.x
- No external libraries required.

## How It Works 🛠️

### Program Structure

The program is based on a `Verb` class that represents each Italian verb. Each `Verb` object contains information about the verb, such as:

- The name of the verb.
- Its auxiliary verb (if necessary).
- The conjugation in the main tenses (present, past, imperfect, future, etc.).
- Methods to conjugate the verb in different tenses.

### Main Classes and Methods 📚

- **`Verb` Class**: Represents a verb and manages its conjugation in various tenses.
    - `participio()`: Returns the past participle of the verb.
    - `presente()`: Returns the present tense conjugation of the verb.
    - `passato_prossimo()`: Returns the past perfect conjugation of the verb.
    - `imperfetto()`: Returns the imperfect conjugation of the verb.
    - `futuro()`: Returns the future conjugation of the verb.
    - `condizionale_presente()`: Returns the present conditional conjugation.
    - `condizionale_passato()`: Returns the past conditional conjugation.
    - `trapassato_prossimo()`: Returns the pluperfect conjugation.

- **`Ita` Class**: Manages a list of verbs and provides methods to get and conjugate verbs.
    - `get_verbo(nome)`: Returns a `Verb` object given the name of the verb.
    - `coniuga_verbo(verbo_nome, tempo)`: Returns the conjugation of the verb in the specified tense.
    - `lista_tempi(verbo_nome)`: Returns a list of available tenses for a verb.

### Example Usage 💻

```python
from coniugazione import Ita

ita = Ita()

# Display available tenses for the verb "andare"
available_tenses = ita.lista_tempi("andare")
print(f"Tenses available for 'andare': {available_tenses}")

# Conjugate the verb "andare" in the past perfect tense
past_perfect_conjugation = ita.coniuga_verbo("andare", "passato_prossimo")
print(f"Past perfect of 'andare': {past_perfect_conjugation}")
```

### Conjugation Examples 📝

- **Verb "andare" (auxiliary verb 'essere')**:
  - Present: vado, vai, va, andiamo, andate, vanno
  - Past Perfect: sono andato, sei andato, è andato, siamo andati, siete andati, sono andati
  - Imperfect: andavo, andavi, andava, andavamo, andavate, andavano
  - Future: andrò, andrai, andrà, andremo, andrete, andranno
  - Present Conditional: andrei, andresti, andrebbe, andremmo, andreste, andrebbero

- **Verb "essere" (auxiliary verb 'essere')**:
  - Present: sono, sei, è, siamo, siete, sono
  - Past Perfect: sono stato, sei stato, è stato, siamo stati, siete stati, sono stati
  - Imperfect: ero, eri, era, eravamo, eravate, erano
  - Future: sarò, sarai, sarà, saremo, sarete, saranno
  - Present Conditional: sarei, saresti, sarebbe, saremmo, sareste, sarebbero

## Installation ⚡

1. Clone the repository:
    ```bash
    git clone https://github.com/LightYagami28/italian-verbs
    ```

2. Navigate to the project folder:
    ```bash
    cd italian-verbs
    ```

3. Run the program:
    ```bash
    python coniugazione.py
    ```

## License 📝

This program is distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

## Notes 🗒️

The code was originally published in the repository Archived [alxm/italian-verbs](https://github.com/alxm/italian-verbs) and later improved and refactored for better readability and usability.
