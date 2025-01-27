import spacy

gardenpathSentences = ["The Girl told the story cried.",
                       "I convinced her children are noisy.",
                       "Mary gave the child a Band-Aid.",
                       "That Jill is never here hurts.",
                       "The cotton clothing is made of grows in Mississippi."]

# Load the English NLP model
nlp = spacy.load('en_core_web_sm')

# Tokenize each sentence and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)

    # Print the entities in the sentence
    print(f'Entities in the sentence "{sentence}" are:')
    for ent in doc.ents:
        print(f'{ent.text} ({ent.label_})')

# Use spacy to look up entities I don't understand

print(spacy.explain("GPE"))
print(spacy.explain("PERSON"))

# Entities explored:
# GPE: Countries, Cities, States. Yes it makes sense as Mississippi is a state
# in the USA.
# PERSON: People, including fictional. Yes it makes sense as Jill & Mary are 
# names of people and "Girl" is more abstract but still a person.
# NB no entity given for second sentence