import json
import os
import csv


def read_test_results(file_path):
  with open(file_path, 'r') as file:
    pages = file.readlines()
  # remove the new line character from the end of each line
  pages = [page.strip() for page in pages]
  return pages

def read_data(path):
  with  open(path, 'r') as file:
    data = {}
    for line in file:
      item = json.loads(line)
      data[item['page']] = item['category']
  return data

if __name__ == "__main__":
  # Read the data from the data.jsonnl file
  data_path = 'data/data.jsonnl'
  data = read_data(data_path)

  # Read the test results from the test_result.txt file
  test_path = 'data/test_result.txt'
  pages = read_test_results(test_path)
  
  # for each page in the test results match the category from the data and then make a csv each row should have the page number and the category
  test_result = []
  for page in pages:
    category = data[int(page)]
    test_result.append({'page': page, 'category': category})

  # Save the test results to a csv file
  output_path = 'data/output.csv'
  os.makedirs(os.path.dirname(output_path), exist_ok=True)

  with open(output_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['page', 'category'])
    writer.writeheader()
    for item in test_result:
      writer.writerow(item)
  
  

