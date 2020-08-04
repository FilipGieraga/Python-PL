import pandas as pd
import xlsxwriter

df = pd.read_json("Pracownicy.json")
df = df.T
df = pd.DataFrame(df)
pd.set_option('display.max_columns', None)

df["Stanowisko"] = pd.Categorical(df["Stanowisko"], ["CEO", "President", "Vice-President", "Menadżer", "Supervisor",
                                                     "Kierownik", "Rekrutacja",
                                                     "Zarządzanie świadczeniami i odszkodowaniami",
                                                     "Bezpieczeństwo i zdrowie", "Trening i rozwój",
                                                     "Relacje z pracownikiem", "Zwykły pracownik"])

df = df.sort_values("Stanowisko")

headers = list(df.columns.values)
# print(headers)
id = df.index
imie = df["Imię"]
nazwiska = df["Nazwisko"]
plec = df["Płeć"]
e_mail = df["E-mail"]
data_urodzenia = df["Data urodzenia"]
wiek = df["Wiek"]
data_rozpoczęcia = df["Data rozpoczęcia"]
staz_pracy = df["Staż pracy(w dniach)"]
stanowisko = df["Stanowisko"]
dzial = df["Dział"]
dzial = dzial[1:]
zar_miesieczne = df["Zarobki miesięczne"].map(lambda x: x.strip(" zł"))
zar_miesieczne = pd.to_numeric(zar_miesieczne)
zar_roczne = df["Zarobki roczne"].map(lambda x: x.strip(" zł"))
zar_roczne = pd.to_numeric(zar_roczne)


# print(dzial)
# print(df.head(20))


def srednia_na_stanowsiko(df):
    if df["Zarobki miesięczne"].dtype != "int64":
        df["Zarobki miesięczne"] = df["Zarobki miesięczne"].map(lambda x: x.strip(" zł"))
        df["Zarobki miesięczne"] = pd.to_numeric(df["Zarobki miesięczne"])

    zarobki_grouped = df.groupby("Stanowisko")["Zarobki miesięczne"].mean()
    zarobki_grouped = zarobki_grouped.round(0)
    zarobki_grouped = zarobki_grouped.dropna(how='all')
    zarobki_grouped = zarobki_grouped.astype('int32')
    nazwa1 = "Średnie zarobki miesięczne(w zł):"
    dane1 = []
    etykiety1 = []
    # print(zarobki_grouped)
    for stanowisko in zarobki_grouped:
        dane1.append(stanowisko)
    for index in zarobki_grouped.index:
        etykiety1.append(index)

    return dane1, etykiety1, nazwa1


# dane1,etykiety1,nazwa1=srednia_na_stanowsiko(df)


def mediana_na_stanowsiko(df):
    if df["Zarobki miesięczne"].dtype != "int64":
        df["Zarobki miesięczne"] = df["Zarobki miesięczne"].map(lambda x: x.strip(" zł"))
        df["Zarobki miesięczne"] = pd.to_numeric(df["Zarobki miesięczne"])

    zarobki_grouped = df.groupby("Stanowisko")["Zarobki miesięczne"].median()
    zarobki_grouped = zarobki_grouped.round(0)
    zarobki_grouped = zarobki_grouped.dropna(how='all')
    zarobki_grouped = zarobki_grouped.astype('int32')
    nazwa2 = "Mediana zarobków miesięcznie(w zł):"
    dane2 = []
    etykiety2 = []
    for stanowisko in zarobki_grouped:
        dane2.append(stanowisko)
    for index in zarobki_grouped.index:
        etykiety2.append(index)

    return dane2, nazwa2


# dane2,nazwa2=mediana_na_stanowsiko(df)


def srednia_wieku(df):
    df["Wiek"] = pd.to_numeric(df["Wiek"])
    wiek_grouped = df.groupby("Stanowisko")["Wiek"].mean()
    wiek_grouped = wiek_grouped.round(0)
    wiek_grouped = wiek_grouped.dropna(how='all')
    wiek_grouped = wiek_grouped.astype('int32')
    nazwa3 = "Średnie wiek (w latach):"
    dane3 = []
    etykiety3 = []
    for stanowisko in wiek_grouped:
        dane3.append(stanowisko)
    for index in wiek_grouped.index:
        etykiety3.append(index)
    # print(dane3,etykiety3)
    return dane3, nazwa3


# dane3,nazwa3 = srednia_wieku(df)


def pracownicy_na_stanowisku(df):
    df["Licznik"] = 1
    dzial_grouped = df.groupby(["Stanowisko"]).count()["Licznik"]
    dzial_grouped = dzial_grouped.loc[(dzial_grouped != 0)]
    nazwa4 = "Ilość osób:"
    dane4 = []
    etykiety4 = []
    for stanowisko in dzial_grouped:
        dane4.append(stanowisko)
    for index in dzial_grouped.index:
        etykiety4.append(index)
    return dane4, nazwa4


# dane4,nazwa4 = pracownicy_na_stanowisku(df)


def pracownicy_w_dziale(df):
    df["Licznik"] = 1
    dzial_grouped = df.groupby(["Dział"]).count()["Licznik"]
    dzial_grouped = dzial_grouped.loc[(dzial_grouped != 0)]
    nazwa5 = "Ilość osób w poszczególnych działach:"
    dane5 = []
    etykiety5 = []
    for stanowisko in dzial_grouped:
        dane5.append(stanowisko)
    for index in dzial_grouped.index:
        etykiety5.append(index)
    return dane5, etykiety5, nazwa5


# dane5,etykiety5,nazwa5=pracownicy_w_dziale(df)


def k_i_m_licznik(df):
    df["Licznik"] = 1
    k_i_m = df.groupby(["Płeć"]).count()["Licznik"]
    dane6 = []
    etykiety6 = []
    nazwa6 = "Ilość kobiet i mężczyzn w firmie:"
    for osoba in k_i_m:
        dane6.append(osoba)
    for index in k_i_m.index:
        etykiety6.append(index)
    return dane6, etykiety6, nazwa6


# dane6,etykiety6,nazwa6 = k_i_m_licznik(df)


def zarobki_zw_pracowników(df):
    if df["Zarobki roczne"].dtype != "int64":
        df["Zarobki roczne"] = df["Zarobki roczne"].map(lambda x: x.strip(" zł"))
        df["Zarobki roczne"] = pd.to_numeric(df["Zarobki roczne"])
    zwykli_p = df.loc[df["Stanowisko"].str.contains("Zwykły")]
    zwykli_p = zwykli_p.groupby(["Płeć"])["Zarobki roczne"].mean()
    zwykli_p = zwykli_p.round(0)
    nazwa7 = "Średnia zarobków kobiet i mężczyzn na najniższych stanowiskach:"
    dane7 = []
    etykiety7 = []
    for osoba in zwykli_p:
        dane7.append(osoba)
    for index in zwykli_p.index:
        etykiety7.append(index)
    return dane7, nazwa7


# dane7,nazwa7=zarobki_zw_pracowników(df)


# def zarobki_supervisorow(df):
#     if df["Zarobki roczne"].dtype!="int64":
#         df["Zarobki roczne"] = df["Zarobki roczne"].map(lambda x: x.strip(" zł"))
#         df["Zarobki roczne"]= pd.to_numeric(df["Zarobki roczne"])
#     zwykli_p=df.loc[df["Stanowisko"].str.contains("Superv")]
#     zwykli_p=zwykli_p.groupby(["Płeć"])["Zarobki roczne"].mean()
#     zwykli_p=zwykli_p.round(0)
#     print(zwykli_p)


def excel_firma(headers, id, imie, nazwiska, plec, e_mail, data_urodzenia, wiek, data_rozpoczęcia, staz_pracy,
                stanowisko, dzial, zar_miesieczne, zar_roczne):
    workbook = xlsxwriter.Workbook('Struktura_Korporacyjna.xlsx')
    worksheet = workbook.add_worksheet(name="Pracownicy")
    cell_format = workbook.add_format({'bold': True})
    worksheet.freeze_panes(1, 0)
    row = 0
    col = 1
    worksheet.write(0, 0, "ID", cell_format)
    for cell in headers:
        worksheet.write(row, col, cell, cell_format)
        col += 1

    row = 1
    col = 0

    for cell1, cell2, cell3, cell4, cell5, cell6 in zip(id, imie, nazwiska, plec, e_mail, data_urodzenia):
        worksheet.write(row, col, cell1)
        worksheet.write(row, col + 1, cell2)
        worksheet.write(row, col + 2, cell3)
        worksheet.write(row, col + 3, cell4)
        worksheet.write(row, col + 4, cell5)
        worksheet.write(row, col + 5, cell6)
        row += 1

    K = workbook.add_format({'color': 'blue'})
    M = workbook.add_format({'color': 'red'})

    worksheet.conditional_format('D2:D' + str(row) + '', {'type': 'text',
                                                          'criteria': 'containing',
                                                          'value': "Kobieta",
                                                          'format': K})

    worksheet.conditional_format('D2:D' + str(row) + '', {'type': 'text',
                                                          'criteria': 'containing',
                                                          'value': "Mężczyzna",
                                                          'format': M})

    # cell_format.set_font_color('red')

    row = 1
    col = 6

    for cell1, cell2, cell3, cell4 in zip(wiek, data_rozpoczęcia, staz_pracy, stanowisko):
        worksheet.write(row, col, cell1)
        worksheet.write(row, col + 1, cell2)
        worksheet.write(row, col + 2, cell3)
        worksheet.write(row, col + 3, cell4)
        row += 1

    worksheet.conditional_format('I2:I' + str(row) + '', {'type': 'data_bar'})

    row = 2
    col = 10

    for cell1 in dzial:
        worksheet.write(row, col, cell1)
        row += 1

    row = 1
    col = 11
    money = workbook.add_format({'num_format': '#,##0.00 [$zł-415]'})
    for cell1, cell2 in zip(zar_roczne, zar_miesieczne):
        worksheet.write(row, col, cell1, money)
        worksheet.write(row, col + 1, cell2, money)
        row += 1

    worksheet.conditional_format('M2:M' + str(row) + '', {'type': 'data_bar', 'bar_color': '#FAF200'})
    worksheet.conditional_format('L2:L' + str(row) + '', {'type': 'data_bar', 'bar_color': '#F07C78'})

    worksheet.set_column('A:A', 5.22)
    worksheet.set_column('B:B', 10.33)
    worksheet.set_column('C:C', 12.56)
    worksheet.set_column('D:D', 9)
    worksheet.set_column('E:E', 32)
    worksheet.set_column('F:F', 13)
    worksheet.set_column('G:G', 4.5)
    worksheet.set_column('H:H', 14.5)
    worksheet.set_column('I:I', 17.9)
    worksheet.set_column('J:J', 38.78)
    worksheet.set_column('K:K', 17.33)
    worksheet.set_column('L:L', 12.67)
    worksheet.set_column('M:M', 16.22)

    worksheet1 = workbook.add_worksheet(name="Statystyki")
    dane1, etykiety1, nazwa1 = srednia_na_stanowsiko(df)
    dane2, nazwa2 = mediana_na_stanowsiko(df)
    dane3, nazwa3 = srednia_wieku(df)
    dane4, nazwa4 = pracownicy_na_stanowisku(df)
    worksheet1.write(0, 0, "Stanowisko:", cell_format)
    worksheet1.write(0, 1, nazwa1, cell_format)
    worksheet1.write(0, 2, nazwa2, cell_format)
    worksheet1.write(0, 3, nazwa3, cell_format)
    worksheet1.write(0, 4, nazwa4, cell_format)

    row = 1
    col = 0

    for cell in etykiety1:
        worksheet1.write(row, col, cell)
        row += 1

    row = 1
    col = 1

    for cell1, cell2, cell3, cell4 in zip(dane1, dane2, dane3, dane4):
        worksheet1.write(row, col, cell1, money)
        worksheet1.write(row, col + 1, cell2, money)
        worksheet1.write(row, col + 2, cell3)
        worksheet1.write(row, col + 3, cell4)
        row += 1

    chart = workbook.add_chart({'type': 'column'})

    chart.add_series({
        'name': 'Średnia',
        'categories': '=Statystyki!A2:A' + str(row) + '',
        'values': '=Statystyki!B2:B' + str(row) + '',
    })
    chart.add_series({
        'name': 'Mediana',
        'categories': '=Statystyki!A2:A' + str(row) + '',
        'values': '=Statystyki!C2:C' + str(row) + '',
    })

    chart.set_x_axis({'name': 'Stanowiska'})
    chart.set_y_axis({'name': 'Zarobki(zł)'})

    chart.set_style(5)

    worksheet1.insert_chart('E19', chart, {'x_offset': 25, 'y_offset': 10})

    row += 3
    col = 0

    dane5, etykiety5, nazwa5 = pracownicy_w_dziale(df)
    worksheet1.write(row, col, "Dział:", cell_format)
    worksheet1.write(row, col + 1, nazwa5, cell_format)

    row += 1

    for cell1, cell2 in zip(etykiety5, dane5):
        worksheet1.write(row, col, cell1)
        worksheet1.write(row, col + 1, cell2)
        row += 1

    row += 3
    col = 0

    dane6, etykiety6, nazwa6 = k_i_m_licznik(df)
    worksheet1.write(row, col, "Płeć:", cell_format)
    worksheet1.write(row, col + 1, nazwa6, cell_format)

    row += 1

    for cell1, cell2 in zip(etykiety6, dane6):
        worksheet1.write(row, col, cell1)
        worksheet1.write(row, col + 1, cell2)
        row += 1

    row += 3
    col = 0

    dane7, nazwa7 = zarobki_zw_pracowników(df)
    worksheet1.write(row, col, "Płeć:", cell_format)
    worksheet1.write(row, col + 1, nazwa7, cell_format)

    row += 1

    for cell1, cell2 in zip(etykiety6, dane7):
        worksheet1.write(row, col, cell1)
        worksheet1.write(row, col + 1, cell2)
        row += 1

    worksheet1.set_column('A:A', 38.78)
    worksheet1.set_column('B:B', 28.44)
    worksheet1.set_column('C:C', 32)
    worksheet1.set_column('D:D', 21)
    worksheet1.set_column('E:E', 10.33)

    workbook.close()
    print("Dokument został poprawnie zapisany w pliku Struktura_Korporacyjna.xlsx")
    print("W dokumencie znajdują się 2 arkusze tj. Pracownicy oraz Statystyki.")


excel_firma(headers, id, imie, nazwiska, plec, e_mail, data_urodzenia, wiek, data_rozpoczęcia, staz_pracy,
            stanowisko, dzial, zar_miesieczne, zar_roczne)

"""
srednia_na_stanowsiko(df)
mediana_na_stanowsiko(df)
srednia_wieku(df)
pracownicy_na_stanowisku(df)
pracownicy_w_dziale(df)
k_i_m_licznik(df)
zarobki_zw_pracowników(df)
zarobki_supervisorow(df)

"""
