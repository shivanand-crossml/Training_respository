import pandas as pd
import csv

with open("/home/shivanand/Documents/Training/Task/data.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)

data = pd.read_csv("https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-100.csv")



print(data.groupby(["Organization Id","Name"]).mean())

print(data.to_csv("organization.csv"))


