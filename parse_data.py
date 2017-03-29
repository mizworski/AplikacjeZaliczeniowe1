from jinja_test import Environment, PackageLoader
from jinja_test import select_autoescape
import csv


def generate_all():
    with open('pkw2000.csv', newline='') as csvfile:
        results = csv.reader(csvfile, delimiter=',')
        labels = next(results)

        prev = []
        results_country = []
        results_province = []
        results_circuit = []

        for row in results:
            process_row(row, prev, results_circuit, results_province, results_country, labels)
            prev = row

    generate_main_webpage()


def generate_main_webpage():
    kandydaci = [
        {
            'nazwa': 'Andrzej Dupa',
            'wynik_ilosc': 2137,
            'wynik_procent': 99.7
        }
    ]

    uprawnionych = 2137
    kart_waznych = 997
    glosow_waznych = 1488
    glosow_niewaznych = 4.76

    env = Environment(
        loader=PackageLoader('app', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template("general_template.html")
    with open("output.html", "w") as out:
        out.write(template.render(
            uprawnionych=uprawnionych,
            kart_waznych=kart_waznych,
            glosow_waznych=glosow_waznych,
            glosow_niewaznych=glosow_niewaznych,
            kandydaci=kandydaci
        ))


def create_webpage(results_circuit):
    return []


def process_row(row, prev, results_circuit, results_province, results_country, labels):
    if prev == [] or row[0] != prev[0]:
        result_province = create_webpage(results_circuit)
        results_province.append(result_province)
        result_country = create_webpage(results_province)
        results_country.append(result_country)
        print("nowe wojewodztwo " + row[0])
    elif prev == [] or row[1] != prev[1]:
        result_province = create_webpage(results_circuit)
        results_province.append(result_province)
        print("nowy okrag" + row[1])

    results_circuit.append(row)


generate_all()
