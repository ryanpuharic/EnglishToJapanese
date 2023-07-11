import deepl, csv
translator = deepl.Translator("2eaf9b4b-9fc6-ea77-a048-e99cebe3aaf6:fx") #api key

#translation function using DeepL
def translate(input):
  return(translator.translate_text(input, target_lang="JA"))

#import glossary from language department
translations = {}
with open('./glossary.csv', 'r', encoding='utf-8') as glossary:
  reader = csv.DictReader(glossary)
  for row in reader:
    translations[row['eng']] = row['jpn']

#reading input
data = []
with open('./input.csv', 'r') as src:
  reader = csv.reader(src)
  for row in reader:
    data.append(row)

#translate each field
for row in data[1:]:
  for i, field in enumerate(row):
    if field in translations: #first use translation dictionary
      row[i] = translations[field]
    elif(row[i] != "" and i !=0): #if not in dictionary, use DeepL
      row[i] = str(translator.translate_text(str(field), target_lang="JA"))

#write to output file
with open('./output.csv', 'w', encoding='utf-8') as dest:
  writer = csv.writer(dest, lineterminator="")
  for row in data:
    row_str = ','.join(str("\"" + value + "\"") for value in row) 
    dest.write(row_str + '\n') 
  
  #truncate extra whitespace
  dest.seek(0,2)
  dest.seek(dest.tell() - 2,0)
  dest.truncate()