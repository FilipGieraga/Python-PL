# Program zgadnij liczbę pozwala wprowadzić, bądź losowo wybrać liczbę, a następnie próbuje ją odgadnąć z domyślnego bądź wybranego przedziału.

Wymagania: Python 3, random module

# Program:
- pozwala na wybranie swojej szczęśliwej liczby albo wylosowanie jej przez komputer
- pozwala na wybranie dolnego i górnego zakresu albo pozostanie przy domyślnym zakresie <1,1000>
- po określeniu zakresów i liczb program sprawdza czy liczba jest w zakresie
- program losuje liczbe z danego mu zakresu i sprawdza czy jest ona szczęśliwą liczbą
- jeśli liczba wylosowana jest mniejsza niż szczęśliwa liczba, to dolny zakres zwiększa się
  do wylosowanej liczby+1 Przykład: wylosowano 10, szczęśliwa liczba 100, dolny zakres zwiększony do 11
- jeśli liczba wylosowana jest większa niż szczęśliwa liczba, to górny zakres zmniejsza się
  do wylosowanej liczby-1
- przy trafieniu w szczęśliwą liczbę program drukuje ile podejść mu to zajęło oraz zakres z jakiego
losował

