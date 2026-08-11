 
import re # For Regular Expressions

import time as t # For time based elements to help the user read edited text

import os # For searching directories and file handling

from random import randint # For random generation

import matplotlib.pyplot as plt # for statistical analysis

import pandas as pd # For transcript creation and csv making

# Statistical Functions

def is_it_ai(text: str):

  text = text.lower()

  text = re.split(r'[^a-zA-Z0-9]', text)

  ai_words = [
    'journey', 'multitude', 'plethora', 'testament', 'accordingly', 'actionable',
    'insights', 'adept', 'adoption', 'rate', 'aforementioned', 'agile',
    'ai-powered', 'aligns', 'ample', 'opportunities', 'amplify', 'arduous',
    'result', 'augment', 'bandwidth', 'based', 'information', 'provided',
    'best', 'practices', 'blockchain-enabled', 'brand', 'awareness', 'broadly',
    'speaking', 'burgeoning', 'cannot', 'overstated', 'capacity', 'building',
    'captivating', 'certainly', 'here’s', 'change', 'management', 'cloud-based',
    'cognizant', 'collaborative', 'commendable', 'competitive', 'complexity',
    'conceptualize', 'conducting', 'consequently', 'considerable', 'continuous',
    'improvement', 'corporate', 'social', 'responsibility', 'cost', 'optimization',
    'craft', 'critical', 'crucial', 'customer', 'loyalty', 'satisfaction',
    'customer-centric', 'cutting-edge', 'data-driven', 'deep', 'dive',
    'understanding', 'deliverables', 'delve', 'delved', 'delving', 'intricacies',
    'demonstrates', 'significant', 'deployment', 'digital', 'transformation',
    'disruptive', 'innovation', 'expertise', 'downtime', 'drive', 'driven',
    'driving', 'dynamic', 'efficiency', 'elevate', 'embark', 'voyage',
    'embarked', 'emerging', 'technologies', 'empower', 'enable', 'encountered',
    'hurdles', 'enhance', 'enhancing', 'enlightening', 'enriches', 'entails',
    'entrenched', 'epicenter', 'essential', 'essentially', 'esteemed', 'ethical',
    'considerations', 'ever-evolving', 'excels', 'exciting', 'exemplary',
    'explore', 'facilitate', 'flourishing', 'foray', 'foster', 'fostering',
    'fresh', 'perspectives', 'inception', 'execution', 'fundamental',
    'fundamentally', 'furthermore', 'future-proof', 'game', 'changer',
    'game-changer', 'generally', 'given', 'glean', 'going', 'forward',
    'golden', 'governance', 'granular', 'granularly', 'grasp', 'groundbreaking',
    'growing', 'recognition', 'hence', 'herein', 'heretofore', 'high-level',
    'hinder', 'holistic', 'holistically', 'however', 'impactful', 'implementation',
    'implications', 'important', 'particular', 'today’s', 'rapidly', 'evolving',
    'industry', 'innovative', 'invaluable', 'issue', 'resolution', 'worth',
    'noting', 'iteration', 'kaleidoscope', 'key', 'takeaways', 'knowledge',
    'transfer', 'kpis', 'performance', 'indicators', 'latency', 'leverage',
    'linchpin', 'low-level', 'manifold', 'penetration', 'share', 'trends',
    'maximize', 'milestone', 'mission-critical', 'moreover', 'moving',
    'multifaceted', 'mvp', 'minimum', 'viable', 'product', 'namely', 'navigating',
    'complexities', 'nevertheless', 'new', 'next-generation', 'notable',
    'notwithstanding', 'nuanced', 'numerous', 'offboarding', 'offer',
    'comprehensive', 'offerings', 'edge', 'onboarding', 'operational',
    'excellence', 'optimize', 'pain', 'point', 'paradigm', 'shift',
    'paramount', 'particularly', 'areas', 'pervasive', 'pivotal', 'poc',
    'proof', 'concept', 'preemptively', 'problem', 'solving', 'process',
    'profitability', 'profound', 'promote', 'pronged', 'quality', 'assurance',
    'control', 'reaching', 'recognize', 'regulatory', 'compliance',
    'relentless', 'remarkable', 'resonate', 'resource', 'allocation',
    'revenue', 'growth', 'risk', 'mitigation', 'roadmap', 'robust',
    'roi', 'return', 'investment', 'root', 'cause', 'analysis', 'scalable',
    'scrum', 'seamless', 'shed', 'showcasing', 'significantly', 'contributes',
    'simply', 'put', 'sla', 'service', 'level', 'agreement', 'solution',
    'development', 'specifically', 'sprint', 'state-of-the-art', 'strategic',
    'alignment', 'streamline', 'strive', 'strong', 'substantial', 'substantially',
    'sustainability', 'synergistically', 'synergy', 'systemic', 'tailor',
    'tapestry', 'tco', 'total', 'cost', 'ownership', 'thereby', 'therefore',
    'therein', 'thereof', 'thought', 'thought-provoking', 'thrive', 'thriving',
    'throughput', 'thus', 'time', 'clarify', 'demonstrate', 'elucidate',
    'emphasize', 'exemplify', 'furnish', 'highlight', 'illustrate', 'provide',
    'reiterate', 'showcase', 'underscore', 'unleash', 'unlock', 'touchpoint',
    'transformative', 'transforming', 'ultimately', 'uncharted', 'undeniable',
    'underscores', 'unique', 'undoubtedly', 'unparalleled', 'uptime',
    'user', 'engagement', 'experience', 'feedback', 'interface', 'utilize',
    'utmost', 'valuable', 'value', 'proposition', 'value-added', 'various',
    'vast', 'vibrant', 'vital', 'well-crafted', 'whilst', 'true', 'widely',
    'recognized', 'keen'
]

  ai_amt = 0

  for word in text:
    if word in ai_words:
      ai_amt += 1

  # Percentage Calculations
  ai_percent = (ai_amt/len(text)) * 100
  human_percent = 100 - ai_percent

  return [ai_percent, human_percent], ai_amt

def character_analysis(text):

  word_amt, number_amt, special_character_amt = 0, 0, 0

  for char in text.split(" "):
    if char.isalpha():
      word_amt += 1
    elif char.isdigit():
      number_amt += 1
    else:
      special_character_amt += 1

  return [word_amt, number_amt, special_character_amt], word_amt


# Ciphering

letter_number = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
    'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15',
    'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
    'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25',
    'Z': '26'
}

number_letter = {values: keys for keys, values in letter_number.items()}

 # Associative Array for Numeric Cipher

letter_pattern = r'[A-Za-z]' # Regular Expression Pattern

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
] # Associative Array for Caesar Cipher

# Instructions

user_txt = None

split_pattern = r'["\'.]' # Regular Expression Pattern

command_regex = [r'\A[Yy]$', r'\A[Aa]$', r'\A[Dd]$', r'\A[Rr]$', r'\A[Ss]$', r'\A[Ff]$', r'\A[Cc]$', r'(?i)\Acaesar\Z', r'(?i)\Anumeric\Z', r'(?i)\Aencode\Z', r'(?i)\Adecode\Z', r'(?i)\Arng\Z', r'(?i)\Astats\Z', r'\A[Ee]$', r'\A[Qq]$']

try:

  user_command = input("Do you want to insert a file? 🗂 (y/n): ") # Command Line Interface/User Input

  if re.match(command_regex[0], user_command):

    user_txt = input("\nInsert file: ") ## File Insertion

    file_var = re.split(split_pattern, user_txt)

    found_path = ""

    for path, dirs, files in os.walk(os.getcwd()): ## Finds File
          if user_txt in files:
              found_path = os.path.join(path, user_txt)
              print(f"\n{found_path} is the file you inserted")

    if "txt" in file_var : # If file is .txt

      try:

        with open(found_path) as f:

          user_txt = f.read()
          print(f'\n{user_txt}')

      except FileNotFoundError:

          print("No file found 🗂")

    else:

          print("Unsupported File Type.")

  else:

    user_txt = input("\nWrite ✏️: ")

    print(f'\n{user_txt}')


  while True:

    print("\nControls ⚙️:")

    print("\nA - Add ➕")

    print("\nD - Delete ➖")

    print("\nR - Replace 🔄")

    print("\nS - Search 🔎")

    print("\nF - Flip 🔄")

    print("\nC - Cipher 🕵️‍♀️")

    print("\nRNG - Random ❓")

    print("\nStats - Statistics on Text 📊")

    print("\nE - Erase All 🗑️")

    print("\nQ - Quit Application 🛑")

  # Commands

    user_command = input("\nCommand: ")

    if re.match(command_regex[1], user_command): # Adding Text

      user_add = input("\nAdd: ")
      user_txt = user_txt + user_add
      print(f'\n{user_txt}')

      t.sleep(2)

    elif re.match(command_regex[2], user_command): # Deleting Text

      user_delete = input("\nDelete: ")

      replace_count = input(f"\nHow many {user_delete}s do you want to delete? : ")

      user_txt = re.sub(user_delete, "", user_txt, int(replace_count) - 1, re.I)

      print(f'\n{user_txt}')

      t.sleep(2)

    elif re.match(command_regex[3], user_command): # Replacing Text

        user_replaced = input("\nWhich text to Replace?: ")
        user_replacement = input("\nReplace with: ")
        replace_count = input(f"\nHow many {user_replaced}s to replace? : ")

        user_txt = re.sub(user_replaced, user_replacement, user_txt, int(replace_count) - 1, re.I)

        print(f'\n{user_txt}')

        t.sleep(2)

    elif re.match(command_regex[4], user_command): ## Searching Software

      user_search = input("\nSearch: ")

      times_occur = re.findall(user_search,user_txt, re.I)

      if not times_occur:

        print(f'\n0 results found for {user_search}.')

      else :

        print(f'\nThere has been {len(times_occur)} results found for {user_search}.')
        print(f'\n{user_txt}')

    elif re.match(command_regex[5], user_command): # Flipping Text

        flip_txt = list(user_txt)
        print("\nFlipped Text:")
        print(f'\n{"".join(flip_txt[::-1])}')
        t.sleep(2)

    elif re.match(command_regex[6], user_command): # Cryptographic Algorithms

        user_cipher = input("\nPick Cipher (Numeric/Caesar): ")

        if re.match(command_regex[8], user_cipher):

          user_command = input("\nEncode or Decode?: ")

          if re.match(command_regex[9], user_command): # Encoding for Numeric Cipher

            if re.search(letter_pattern, user_txt):

              cipher_txt = ""

              for letter in list(user_txt):

                 if letter.isalpha():

                    cipher_txt += letter_number[letter.upper()] + " "

                 else:

                     cipher_txt += letter

              user_txt = cipher_txt

              print("\nHere is the encoded text!")

              print(f'\n{user_txt}')

              t.sleep(2)

            else:

              print("\n🔠 There has been no letters in the text to encode 🔠.")


          elif re.match(command_regex[10], user_command): # Decoding for Numeric Cipher

            if re.search(r'[0-9]', user_txt):

              cipher_txt = ""

              for num in user_txt.split(" "):

                  if num.isdigit():

                      cipher_txt += number_letter[num]

                  else:
                    cipher_txt += num

              user_txt = cipher_txt

              print("\nHere is the decoded text!")

              print(f'\n{user_txt}')

              t.sleep(2)

            else:

              print("\n🔢 There has been no numbers in the text to decode 🔢.")


        if re.match(command_regex[7], user_cipher):

          user_command = input("\nEncode or Decode?: ")

          if re.match(command_regex[9], user_command):

            try:

              user_amt = int(input("\nBy how much forward?: ")) # Encoding for Caesar Cipher

            except ValueError:

              print("\nNot a number, please enter a number.")

            if re.search(letter_pattern, user_txt):

              list_txt = list(user_txt)

              shift_txt = []

              for character in list_txt:
                if character.upper() in letters :
                  index_var = letters.index(character.upper())
                  shift_txt.append(letters[(index_var + int(user_amt)) % 26].lower() if character.islower() else letters[(index_var + int(user_amt)) % 26])
                else:
                  shift_txt.append(character)

              user_txt = "".join(shift_txt)

              print("\nHere is the encoded text!")

              print(f'\n{user_txt}')

              t.sleep(2)

            else:

                print("\n🔠 There has been no letters in the text to encode 🔠.")

          elif re.match(command_regex[10], user_command):

            try:

              user_amt = int(input("\nBy how much back?: ")) # Decoding for Caesar Cipher

            except ValueError:

              print("\nNot a number, please enter a number.")

            if re.search(letter_pattern, user_txt):

              list_txt = list(user_txt)

              shift_txt = []

              for character in list_txt:
                if character.upper() in letters :
                  index_var = letters.index(character.upper())
                  shift_txt.append(letters[(index_var - int(user_amt)) % 26].lower() if character.islower() else letters[(index_var - int(user_amt)) % 26])
                else:
                  shift_txt.append(character)

              user_txt = "".join(shift_txt)

              print("\nHere is the decoded text!")

              print(f'\n{user_txt}')

              t.sleep(2)

            else:

              print("\n🔠 There has been no letters in the text to decode 🔠.")

    elif re.match(command_regex[11], user_command): # Random Text Generator

      try:

        user_length = int(input("\nHow many characters long should the text be?: "))
        user_range = int(input("\nHow random? (Type 100, for 1%, Type 100000 for 0.001%): "))

      except ValueError:

        print("\nNot a number, please type a number.")

      rand_txt = ""

      for i in range(0, user_length):
        rand_txt += chr(randint(0, user_range))

      user_txt = user_txt + rand_txt

      print(f"\n{user_txt}")

      print("\nNote: Some Text may not show due to the environment this code is running in.")

    elif re.match(command_regex[12], user_command): # Stats on Text

        # AI Scanning

        scanner_percentages, ai_generated_words = is_it_ai(user_txt)

        scanner_labels = ["A.I", "Human"]

        scanner_colours = ["red", "blue"]

        myexplode = [0.2, 0]

        plt.pie(scanner_percentages, labels = scanner_labels, explode = myexplode, colors = scanner_colours)

        print(f"\nYour text is {round(scanner_percentages[0], 1)}% AI-generated and {round(scanner_percentages[1], 1)}% human.")

        print(f"\n{ai_generated_words} words in your text have been detected as AI.")

        plt.show()
        
        t.sleep(1.0)

        # Character Statistics (amt of words, numbers, special characters)
         
        [char_words, char_numbers, char_special], words = character_analysis(user_txt)

        char_labels = ["Words", "Numbers", "Special Characters"]

        char_colours = ["blue", "green", "yellow"]

        plt.pie([char_words, char_numbers, char_special], labels = char_labels, colors = char_colours)
        
        plt.show()

        print(f"\nThere are {words} words in your text")

        user_transcript = input("Do you want a transcript for your text (y/n)?: ")
        
        if re.match(command_regex[0], user_transcript): # Creating Dataframe (Text Transcript)
             
             print("\nText Transcript")

             transcript_df = pd.DataFrame({
                 
                  "Transcript": user_txt.split(" ")
             })

             print(f"\n{transcript_df}")

             user_csv = input("\nDo you want a .csv file to save the transcript? (y/n)?: ")

             if re.match(command_regex[0], user_csv): # Saving transcript as .csv

                  user_csv = input("\nMake a name for the file (Don't worry the .csv is automatically done for you!): ")

                  transcript_df.to_csv(f'{user_csv}.csv')

                  print("\nDone!")

    elif re.match(command_regex[13], user_command): # Erasing Text

       user_txt = ""

    elif re.match(command_regex[14], user_command): # Quitting Text
      

      user_create = input("Do you want a saved file for your text (y/n)?: ") #Saving file as .txt

      if re.match(command_regex[0], user_create):

          user_filename = input("Write name for file (Don't worry the .txt is automatically done for you!): ")

          with open(f'{user_filename}.txt', 'x') as f:

            f.write(user_txt)

      print("\nClosing Application...")

      t.sleep(2)

      print("\nApplication CLosed")

      break

except KeyboardInterrupt:
      
      user_create = input("Do you want a saved file for your text (y/n)?: ") #Saving file as .txt

      if re.match(command_regex[0], user_create):

          user_filename = input("Write name for file (Don't worry the .txt is automatically done for you!): ")

          with open(f'{user_filename}.txt', 'x') as f:

            f.write(user_txt)

      print("\nClosing Application...")

      t.sleep(2)

      print("\nApplication Closed")
