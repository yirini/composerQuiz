Project: Generating Random Classical Composers Quiz Files.

I took the Generating Random Quiz Files project as a reference from the book "Automate the Boring Stuff with Python"
by Al Sweigart.

Hypothetical context: A music history teacher with 15 students in his/her class, wants to give a quiz on
Classical Composers year of birth, randomizing the order of questions so that each quiz is unique.


Here is what the program does:

- Creates 15 different quizzes.
- Creates 25 multiple-choice questions for each quiz, in random order.
- Provides the correct answer and three random wrong answers for each question, in random order.
- Writes the quizzes to 15 text files.
- Writes the answer keys to 15 text files.

This means the code will need to do the following:

- Store the composers and their year of birth in a dictionary.
- Call open(), write(), and close() for the quiz and answer key text files.
- Use random.shuffle() to randomize the order of the questions and multiple-choice options.