import deepl
translator = deepl.Translator("2eaf9b4b-9fc6-ea77-a048-e99cebe3aaf6:fx") #api key

#translate using DeepL
def translate(input):
  return(translator.translate_text(input, target_lang="JA"))

#first line of input has a number 1-3:
#1: Contractor/Sales format
#2: PEL format
#3: Standard format
with open('./input.txt', 'r') as src, open('./output.txt', 'w', encoding='utf-8') as dest:
  for line in src:
    line = line.rstrip('\n')
    line = str(translate(line))
    dest.write(line + '\n')