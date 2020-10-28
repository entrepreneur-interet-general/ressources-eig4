
# Typing

Introduit dans python 3.5 [https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)

## Example

- Sur le snippet ci-dessous, seules les signatures de fonction ont besoin d'être annotées. (Les classes de données, non présentes ici, le sont aussi bien sûr).

```python
from typing import List

def _get_first_match(title: str, prefixes: List[str]) -> int:
    for i, prefix in enumerate(prefixes):
        if title[: len(prefix)] == prefix:
            return i
    return -1

def _detect_inconsistency_in_numbering(
    titles: List[str], parent_title: str, prefixes: List[str]
) -> Optional[TitleInconsistency]:
    first_match = _get_first_match(titles[0], prefixes)
    if first_match == -1:
        return TitleInconsistency(titles, parent_title, f'No prefix found in title "{titles[0]}"')
    for title, prefix in zip(titles, prefixes[first_match:]):
        if title[: len(prefix)] == prefix:
            continue
        return TitleInconsistency(titles, parent_title, f'Title "{title}" is expected to start with prefix "{prefix}"')
    if len(titles) > len(prefixes[first_match:]):
        raise ValueError(f'Missing prefixes in list {prefixes}.')
    return None

def _detect_inconsistency(titles: List[str], parent_title: str) -> Optional[TitleInconsistency]:
    if len(titles) <= 1:
        return None
    pattern_name = _detect_first_pattern(titles)
    if not pattern_name:
        return None
    no_match = [title for title in titles if not re.match(ALL_PATTERNS[pattern_name], title)]
    if no_match:
        no_match_titles = '\n' + '\n'.join(no_match)
        return TitleInconsistency(
            titles, parent_title, f'Some titles do not match pattern {pattern_name}: {no_match_titles}'
        )
    return _detect_inconsistency_in_numbering(titles, parent_title, _PATTERN_NAME_TO_LIST[pattern_name])

def _extract_section_inconsistencies(text: StructuredText) -> List[TitleInconsistency]:
    titles = [section.title.text for section in text.sections]
    inconsistency = _detect_inconsistency(titles, text.title.text)
    result = [inconsistency] if inconsistency else []
    return result + [inc for section in text.sections for inc in _extract_section_inconsistencies(section)]

def extract_inconsistencies(am: ArreteMinisteriel) -> List[TitleInconsistency]:
    return [inc for section in am.sections for inc in _extract_section_inconsistencies(section)]
```

## Les avantages du typage

- Autocomplétion
    - Une fois le setup de l'IDE fait, la déclaration des annotations permet de facilement faire l'autocomplétion et rend parfois inutile la navigation entre plusieurs fichiers.
- Static type checking in IDE
    - Grâce au typage, il est facile de détecter des erreurs en analysant le code. Ca permet notamment d'accélérer grandement les refactos (et de les faire sans hésiter)
    - Il est assez facile d'être couvert à 100% d'annotation, et ça évite de tester les types dans les unit tests. C'est assez complémentaire aux unit tests.
- Améliore la lisibilité du code: la signature de la fonction suffit à décrire ce qu'elle fait, notamment grâce aux types.
- Peut être ajouté à n'importe quel moment dans la vie d'un projet, comme pour typscript (je crois)
- Plutôt facile: seules les signatures des fonctions et les champs des classes doivent être renseignés → pas vraiment de temps perdu dans l'utilisation

## Désavantages

- Coût d'entrée

Plus de pros and cons: [https://realpython.com/python-type-checking/#pros-and-cons](https://realpython.com/python-type-checking/#pros-and-cons)

## Parenthèse: les décorateurs en python

Ils sont partout:

- Flask
- Prefect

Ci dessous, on définit un décorateur qui affiche le temps d'exécution d'une fonction

```python
from typing import Callable, List

def measure_time(func: Callable) -> Callable:
    def output_func(*args, **kwargs):
        import time

        start = time.time()
        res = func(*args, **kwargs)
        print(f'Elapsed: {time.time() - start}s')
        return res

    return output_func

@measure_time
def sum_(ints: List[int]) -> int:
    return sum(ints)
```

Il faut savoir que le décorateur est exécuter au moment de l'import. 

On peut ajouter des variables au décorateur, auquel cas il y a un niveau d'imbrication supplémentaire.

```python
def measure_time_verbose(verbose: bool):
    def dec(func: Callable) -> Callable:
        def output_func(*args, **kwargs):
            import time

            start = time.time()
            res = func(*args, **kwargs)
            duration = time.time() - start
            if not verbose:
                print(f'Elapsed: {duration}s.')
            else:
                print(f'{func.__name__} with args {args} and {kwargs} elapsed in {duration}s.')
            return res

        return output_func

    return dec

@measure_time_verbose(False)
def sum_(ints: List[int]) -> int:
    return sum(ints)
```

## Enigme: Qu'est-ce qui va s'afficher ?

Lorsqu'on exécute le script suivant, que va-t-il s'afficher ?

```python
from typing import Callable, List

def measure_time_verbose(verbose: bool):
    print('A')

    def dec(func: Callable) -> Callable:
        print('B')

        def output_func(*args, **kwargs):
            print('C')
            import time

            start = time.time()
            res = func(*args, **kwargs)
            duration = time.time() - start
            if not verbose:
                print(f'Elapsed: {duration}s.')
            else:
                print(f'{func.__name__} with args {args} and {kwargs} elapsed in {duration}s.')
            return res

        return output_func

    return dec

@measure_time_verbose(True)
def hola() -> None:
    print('holà')
```

Réponse: A et B

Le C ne sera exécuté qu'à l'exécution de la fonction hola

# Decorator + typing =  ?

En python, une fonction est un objet. Elle a donc des attributs, notamment des attributs "magiques" commençant par __.

On peut par exemple récupérer ses annotations.

A partir de là, qu'est-ce qu'on peut faire ? 

- Des Idées?
    - Runtime type check cf [https://typeguard.readthedocs.io/en/latest/userguide.html](https://typeguard.readthedocs.io/en/latest/userguide.html)
    - Fait aussi par pydantic ici [https://pydantic-docs.helpmanual.io/usage/validation_decorator/](https://pydantic-docs.helpmanual.io/usage/validation_decorator/)
    - Automatic unit testing ? On peut imaginer pouvoir définir des tests simples via un decorateur.
    - API rapide à développer: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/) basée notamment sur pydantic
