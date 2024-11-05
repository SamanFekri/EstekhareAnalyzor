import json
import csv


def load_categories(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
  
  result = {}
  for key, value in data.items():
    result[value['name']] = {
      'category': value['value'],
      'label': key,
      'result_text': value['name'],
    }
  
  return result

# Load the categories from the category.json file
categories_path = './data/category.json'
print("📂 Loading categories from:", categories_path)
categories = load_categories(categories_path)
print("✅ Categories loaded successfully")

# Read the src.jsonnl file as a list of dictionaries
data_path = './data/src.jsonnl'
output_path_json = './data/data.jsonnl'
output_path_csv = './data/data.csv'

print("📂 Reading data from:", data_path)
data = []
with open(data_path, 'r', encoding='utf-8') as file:
  for line in file:
    data.append(json.loads(line))
print("✅ Data read successfully")

# Add the category to each item in the data
print("🔄 Adding categories to data items")
for item in data:
  result = item.get('result')
  if result:
    category = categories.get(result)
    if category:
      item['category'] = category['category']
      item['label'] = category['label']
print("✅ Categories added successfully")

# Save the data with the category as jsonnl
print("💾 Saving data to JSONNL file:", output_path_json)
with open(output_path_json, 'w', encoding='utf-8') as f:
  for item in data:
    f.write(json.dumps(item, ensure_ascii=False) + '\n')
print("✅ Data saved to JSONNL file successfully")

# Save the data with the category as csv
print("💾 Saving data to CSV file:", output_path_csv)
with open(output_path_csv, 'w', encoding='utf-8', newline='') as f:
  writer = csv.DictWriter(f, fieldnames=['page', 'result', 'result_text', 'general_result', 'marriage_result', 'trade_result', 'category', 'label'])
  writer.writeheader()
  for item in data:
    writer.writerow(item)
print("✅ Data saved to CSV file successfully")

# Load the csv file and make sure it is saved correctly
print("🔍 Verifying CSV file:", output_path_csv)
with open(output_path_csv, 'r', encoding='utf-8') as f:
  reader = csv.DictReader(f)
  for row in reader:
    if row['page'] == '' or row['result'] == '' or row['general_result'] == '' or row['marriage_result'] == '' or row['trade_result'] == '' or row['category'] == '' or row['label'] == '':
      print('❌ Verification failed')
      break
  else:
    print('✅ Verification successful')
