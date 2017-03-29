from jinja_test import Environment, PackageLoader
from jinja_test import select_autoescape
import csv

colors = [
    '#EEA2AD',
    '#B0171F',
    '#7A67EE',
    '#C6E2FF',
    '#00868B',
    '#00EE76',
    '#483D8B',
    '#8B8386',
    '#FF8C00',
    '#CD4F39',
    '#006400',
    '#800080'
]

summary_labels = [
    'Nazwa jednostki', 'Głosy ważne', 'Dariusz Maciej GRABOWSKI', 'Piotr IKONOWICZ',
    'Jarosław KALINOWSKI', 'Janusz KORWIN-MIKKE', 'Marian KRZAKLEWSKI', 'Aleksander KWAŚNIEWSKI',
    'Andrzej LEPPER', 'Jan ŁOPUSZAŃSKI', 'Andrzej Marian OLECHOWSKI', 'Bogdan PAWŁOWSKI', 'Lech WAŁĘSA',
    'Tadeusz Adam WILECKI'
]


def generate_all():
    with open('pkw2000.csv', newline='') as csvfile:
        results = csv.reader(csvfile, delimiter=',')
        labels_csv = next(results)
        candidates = labels_csv[11:23]

        prev = []
        results_country = []
        results_province = []
        results_circuit = []

        print(candidates)

        for row in results:
            process_row(row, prev, results_circuit, results_province, results_country, candidates)
            prev = row

    generate_main_webpage(results_country, candidates)


# results = [nazwa_jednostki, uprawnionych, kart_waznych, glosow_waznych, glosow_niewaznych, grabowski..wilecki]


def generate_main_webpage(results_country, candidates):
    uprawnionych = 0
    kart_waznych = 0
    glosow_waznych = 0
    glosow_niewaznych = 0

    candidate_results_summary = [0] * 12

    for result in results_country:
        uprawnionych += float(result[1])
        kart_waznych += float(result[2])
        glosow_waznych += float(result[3])
        glosow_niewaznych += float(result[4])
        for i in range(0, 12):
            candidate_results_summary[i] += float(result[i + 5])

    kandydaci = []

    for i in range(0, 12):
        kandydat = [
            candidates[i],
            candidate_results_summary[i],
            candidate_results_summary[i] / glosow_waznych,
            colors[i]
        ]
        kandydaci.append(kandydat)

    env = Environment(
        loader=PackageLoader('app', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template("general_template.html")
    with open("app/templates/main.html", "w") as out:
        out.write(template.render(
            uprawnionych=uprawnionych,
            kart_waznych=kart_waznych,
            glosow_waznych=glosow_waznych,
            glosow_niewaznych=glosow_niewaznych,
            kandydaci=kandydaci,
            wyniki=results_country
        ))


def create_webpage(results_country, candidates):
    uprawnionych = 0
    kart_waznych = 0
    glosow_waznych = 0
    glosow_niewaznych = 0

    candidate_results_summary = [0] * 12

    for result in results_country:
        uprawnionych += float(result[1])
        kart_waznych += float(result[2])
        glosow_waznych += float(result[3])
        glosow_niewaznych += float(result[4])
        for i in range(0, 12):
            candidate_results_summary[i] += float(result[i + 5])

    kandydaci = []

    for i in range(0, 12):
        kandydat = [
            candidates[i],
            candidate_results_summary[i],
            candidate_results_summary[i] / glosow_waznych,
            colors[i]
        ]
        kandydaci.append(kandydat)

    env = Environment(
        loader=PackageLoader('app', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template("general_template.html")
    with open("app/templates/main.html", "w") as out:
        out.write(template.render(
            uprawnionych=uprawnionych,
            kart_waznych=kart_waznych,
            glosow_waznych=glosow_waznych,
            glosow_niewaznych=glosow_niewaznych,
            kandydaci=kandydaci,
            wyniki=results_country
        ))

    return [uprawnionych, kart_waznych, glosow_waznych, glosow_niewaznych] + candidate_results_summary


def process_row(row, prev, results_circuit, results_province, results_country, candidates):
    if prev != [] and row[0] != prev[0]:
        circuit_summary = create_webpage(results_circuit, candidates)
        circuit_row = ['Okreg ' + prev[1]] + circuit_summary
        results_province.append(circuit_row)

        province_summary = create_webpage(results_province, candidates)
        province_row = [row[0].lower()] + province_summary
        results_country.append(province_row)
        results_circuit = []
        results_province = []
        print("nowe wojewodztwo " + row[0])
    elif prev != [] and row[1] != prev[1]:
        circuit_summary = create_webpage(results_circuit, candidates)
        circuit_row = ['Okreg ' + prev[1]] + circuit_summary
        results_province.append(circuit_row)
        results_circuit = []
        print("nowy okrag" + row[1])

    # results=[nazwa_jednostki, uprawnionych, kart_waznych, glosow_waznych, glosow_niewaznych, grabowski..wilecki]

    result = [row[3], row[6], row[7], row[10], row[9]] + row[11:23]
    results_circuit.append(result)


generate_all()
