#install this first 
#!pip install llama-index
#!pip install openai

# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = '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'

# # Loading from a directory
# documents = SimpleDirectoryReader('/content/').load_data()

# # Loading from strings, assuming you saved your data to strings text1, text2, ...
# text_list = ["Homeowner's_Association_Rules_and_Regulations.txt","Parking_Rules_for_Pinebrooke_Condominiums.txt","Pinebrooke_Bylaws_Sub.txt","Policy_Regarding_Violation_Process_Fine.txt","RC_Terms_and_Conditions.txt"]
# documents = [Document(t) for t in text_list]


# Path to directory containing text files
directory_path = '/content/'

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Filter out only the text files
text_files = [file for file in files if file.endswith('.txt')]

# Read the text files into a list of strings
text_list = []
for file in text_files:
    with open(os.path.join(directory_path, file), 'r') as f:
        text_list.append(f.read())

# Create a list of Document objects from the text strings
documents = [Document(t) for t in text_list]

# Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Querying the index
response = index.query("what are the rules and reulations of pinebrooke?")

print(response)
