# Advanced BERT Question Answering System

This repository presents an advanced Python implementation of a question-answering system leveraging the power of the BERT (Bidirectional Encoder Representations from Transformers) model, specifically `bert-large-uncased-whole-word-masking-finetuned-squad`, for providing context-based answers to user queries.

## Key Features

- **BERT Integration**: Harnesses a pre-trained BERT model from Hugging Face's comprehensive `transformers` library.
- **Contextual Understanding**: Employs Whole Word Masking for a nuanced understanding of the context provided by the text.
- **Dynamic Interaction**: Users can interact with the system in real-time by posing questions about the loaded article content.
- **End-of-Session Control**: Implements a user-friendly mechanism to terminate the question-answering loop with a simple 'quit' command.

## How It Works

- The script initializes a question-answering pipeline using the `pipeline` function from the `transformers` library.
- It reads the text content of an article file specified by the user, which serves as the context for answering questions.
- Through a function, it processes user-input questions and retrieves answers from the pre-trained BERT model based on the context of the loaded article.
- The interactive loop allows continuous querying until the user decides to exit.

## Installation & Setup

1. Ensure you have Python 3.x installed.
2. Install the `transformers` library using pip:

   ```sh
   pip install transformers
## Clone this repository to your local machine.
1. Place the text file with the article you want to analyze in the root directory of the project, named article_content.txt.
## Usage
Execute the script from the command line. You will be prompted to enter a question. The script will then display the answer derived from the context of the article content. To end the session, type 'quit' when prompted for a question.
  'python simpleai.py'

## Advanced Configuration
- To use a different model or tokenizer, modify the pipeline instantiation in the script. The transformers library offers a wide array of pre-trained models that can be leveraged for various languages and domains.

## Contributions
- Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.
