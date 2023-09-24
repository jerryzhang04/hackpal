import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download the "punkt" data
nltk.download('punkt')

# Download stopwords (if not already downloaded)
nltk.download('stopwords')

# Open and read the contents of the text file
with open('message.txt', 'r') as file:
    file_contents = file.read()

# Get user input
user_response = input("what is your idea? ")

# Tokenize and preprocess the text (remove punctuation and stopwords)
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(filtered_tokens)

file_contents = preprocess_text(file_contents)
user_response = preprocess_text(user_response)

# Calculate TF-IDF vectors for the file and user response
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([file_contents, user_response])

# Calculate the cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

# Cosine similarity ranges from 0 (completely dissimilar) to 1 (identical)
print(f"Similarity percentage to previous hackathon: {cosine_sim[0][0]*100}%")
