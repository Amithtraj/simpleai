from transformers import pipeline

def load_article_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Load a pre-trained model and tokenizer
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Your text article content
article_content = load_article_content('article_content.txt')

# Function to answer questions using the provided context
def get_answer(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Example usage
while True:
    # Input the question
    user_question = input("What is your question? (Type 'quit' to exit): ")
    if user_question.lower() == 'quit':
        break

    # Get the answer from the model
    answer = get_answer(user_question, article_content)
    print(f"Answer: {answer}")
