import utils
from pkg.read_csv import read_csv
import charts

def run():
  data = read_csv('d:/CFME_Matplotlib/app/file/data.csv')

  continent = input('Type Continente => ')
  countries, percentages = utils.get_world_porcentaje_population(data, continent)

  charts.generate_pie_chart(continent, countries, percentages)

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()