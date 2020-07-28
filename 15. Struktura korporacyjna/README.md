# Program Struktura korporacji:

Wymagania: Python 3, random module, json module, pandas module, datetime module

## Dokumentacja:
W moim programie starałem się stworzyć fikcyjnych pracowników w firmie, zachowując przy tym strukturę podobną do tej, która może występować w korporacji.<br>
Głównymi trzonami całego programu są dwie funkcje tj. **pracownicy** oraz **firma_struktura**.<br>
Pierwsza funkcja pracownicy() pobiera dwie informacje, które są zdefiniowane na końcu programu.
Są nimi liczba_pracowników oraz nazwa_firmy. Liczba pracowników powinna być nie mniejsza niż 100 i nie większa niż 699. Dlaczego tak jest wytłumaczę w dalszej
części tej dokumentacji. Zmienna nazwa_firmy zostaje tutaj użyta przy generowaniu e-maili dla wszystkich pracowników i powinna być podana w cudzysłowie jako
string np. nazwa_firmy = "Google". Na podstawie tych dwóch informacji funkcja zaczyna nam generować podstawowe dane tj. :<br>
- **Id_pracownika** - jest to unikalny pięciocyfrowy identyfikator pracownika, który zostaje losowo wybrany z przedziału <10000,99999><br>
- **Pleć** - losowo wybrana Kobieta bądź Mężczyzna<br>
- **Imię** – na podstawie płci losowane jest imię pracownika z grupy imion żeńskich bądź męskich<br>
- **Nazwisko** – losowane ze zmiennej nazwiska, przy czym jeśli płeć to Kobieta program dodatkowo sprawdza czy ostatnia litera nazwiska to „i” i jeśli tak jest to zamienia ją na „a”. Dzięki temu mamy
np. „Marta Kowalska” zamiast „Marta Kowalski”<br>
- **E-mail**- na podstawie zmiennych imię, nazwisko oraz nazwa firmy zostaje wygenerowany e-mail,
w przykładowej postaci 'przemysław.wiśniewski@google.com'. Wszystko jest tutaj pisane małą literą, ponieważ w e-mailu wielkość liter nie ma znaczenia.<br>
- **Data urodzenia**- korzysta z mniejszej funkcji zdefiniowanej jako losowy_wiek(), która generuje datę
z przedziału od początku 1975 do początku 1992. Przedział ten jest ściśle powiązany z inną zmienną
o nazwie data rozpoczęcia.<br>
- **Wiek**- na podstawie wylosowanej daty urodzenia funkcja licz_wiek() liczy nam wiek każdego pracownika.<br>
- **Data rozpoczęcia** – korzysta z funkcji losowa data(), która generuje nam datę z przedziału od początku 2010 roku do dnia dzisiejszego. Najstarszy stażem pracownik w firmie może mieć datę
rozpoczęcia nie mniejszą niż początek 2010 roku. Z tego też względu chciałem, aby data urodzenia była nie większa niż rok 1992, ponieważ wtedy nasz teoretycznie najmłodszy pracownik
z najdłuższym stażem, musiałby mieć ukończone 18 lat aby móc zacząć pracę. <br>
- **Staż pracy** – podawany w dniach jest liczony poprzez odjęcie od dzisiejszej daty daty rozpoczęcia.
Pracownik, który rozpocząłby pracę 27-01-2014 posiadałby staż pracy  2357 dni na dzień 11-07-2020.<br>
Funkcja pracownicy() po wygenerowaniu danych ww. dla każdego pracownika zwraca je w postaci słownika o nazwie firma, który zostaje przechwycony przez drugą główną funkcję o nazwie firma_struktura().<br>



Funkcja **firma_struktura()** pobiera dwie zmienne tj. firma, która została już wcześniej wygenerowana z funkcji pracownicy() oraz nazwa_firmy.
Jej celem jest zdefiniowanie struktury zarówno pionowej jak i poziomej. **Strukturę pionową determinuję staż pracy, natomiast strukturę poziomą definiuje współczynnik.**<br>
**Współczynnik** jest jedną z najważniejszych zmiennych w całym programie i od jego wielkości zależy ilość pracowników na poszczególnych stanowiskach. Aby móc zacząć przypisywanie danych
poszczególnym pracownikom funkcja ta na początku musi wypełnić dwie zmienne, które są listami o nazwach list_staz oraz list_klucze danymi tj. staże poszczególnych pracowników oraz
odpowiadające im identyfikatory. Następnie liczony jest współczynnik, który jest wielkością firmy podzieloną przez 100 i zaokrągloną w dół.<br>
Pierwszy pracownik jakiemu zostaną przypisane dane to CEO, zmienna klucz_1 wyszukuje nam index najdłuższego stażu w liście o nazwie list_staz. Następnie wskazany nr indexu zostaje znaleziony
w liście list_klucze i jego wartość, czyli konkretny id_pracownika zostaje przypisany zmiennej klucz_2.
CEO jako jedyny w firmie pracownik ma unikatowy e-mail, np.  "kuba.szulc-CEO@google.com". Zarobki roczne jego jak i wszystkich innych pracowników są uzależnione od współczynnika.
Zarobki są zawsze losową liczbą z konkretnego przedziału w zależności od tego jaki jest współcznnik. Im wyższy wsp. tym wyższe zarobki każdego. CEO jest również jedynym pracownikiem,
który nie posiada przypisanego działu. Zarobki miesięczne wszystkich pracowników to zarobki roczne podzielone przez 12.<br>
Liczba pracowników na stanowisku President oraz działów jest równa współczynnikowi. Działy są losowo wybierane z następujących: **Badania i rozwój, Finansowo-księgowy, Compliance, IT,
Logistyka, Marketing**. W firmie są też pracownicy **HR**, o których wspomnę później. Wszyscy pracownicy na wyższych stanowiskach, znajdują się tam ze względu na staż pracy. Im jest on dłuższy tym wyższe stanowisko.<br>
Każdemu pracownikowi na stanowisku President przypisany jest jeden Vice-President. Jego zarobki są niższe i z każdym stopniem w strukturze się zmniejszają.<br>
Liczba menadżerów jest zależna od współczynnika i stałej l_menadzerow = 10. Jeśli wsp. to 5, w firmie będzie 50 menadżerów.<br>
Liczba supervisorów w firmie będzie dwukrotnie większa niż liczba menadżerów, tak żeby każdy menadżer posiadał pod sobą dwóch supervisorów.<br>
Następnie przechodzimy do pracowników HR, których w firmie zawsze jest mniej więcej tyle samo, czyli 3 %. Dział HR to jedyny dział, który nie posiada nad sobą Presidenta oraz Vice-Presidenta.
Jest jedynie jeden albo dwóch kierowników w zależności od współczynnika, którzy mają pod sobą pracowników zajmujących się: Rekrutacją, Zarządzaniem świadczeniami i odszkodowaniami,
Bezpieczeństwem i zdrowiem, Treningiem i rozwojem, Relacjami z pracownikiem.<br>
Na końcu mamy zwykłych pracowników, którzy są rozdzieleni na poszczególne działy (poza HR) mniej więcej po równo.<br>
Jeśli chodzi o określoną liczbę pracowników jaka może być stworzona, wynika ona z tego, że przy 700 pracownikach współczynnik wynosiłby 7 i nie byłoby już działu do wylosowania.
Przy liczbie mniejszej niż 100, wsp. wynosiłby 0 i nie losowany byłby żaden dział. Poza tym mniej niż 100 pracowników, to bardziej firma niż korporacja.<br>
Wszyscy pracownicy zostają zapisani w pliku **Pracownicy.json**
Program ten posiada część drugą.

![alt tag](https://github.com/FilipGieraga/Python-PL/blob/master/15.%20Struktura%20korporacyjna/Struktura.png)
