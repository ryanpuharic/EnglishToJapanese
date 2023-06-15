import deepl, csv
translator = deepl.Translator("2eaf9b4b-9fc6-ea77-a048-e99cebe3aaf6:fx") #api key

#translation function using DeepL
def translate(input):
  return(translator.translate_text(input, target_lang="JA"))

#dictionary of known translations
translations = {
  "Director": "監督",
  "Vice President": "副社長",
  "Data Technologies & Analytic Solutions Intern": "データテクノロジー＆アナリティックソルーション　インターン"
}

data = []

#reading input
#input file uses both formats, first is Contractor/Standard/Sales, second is PEL
with open('./input.csv', 'r') as src:
  reader = csv.reader(src)
  for row in reader:
    data.append(row)

#translate each field
for row in data[1:]:
  for i, field in enumerate(row):
    if field in translations: #first use translation dictionary
      row[i] = translations[field]
    elif(row[i] != ""): #if not in dictionary, use DeepL
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