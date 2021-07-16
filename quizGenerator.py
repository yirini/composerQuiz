# Step 1: Store the Quiz Data in a Dictionary:
import random

# The quiz data. Keys are composers and values are their year of birth.
years = {'Scott Joplin': '1868', 'Johann Sebastian Bach': '1685', 'Arcangelo Corelli': '1653',
   'Wilhelm Pachelbel': '1686', 'Charles Ives': '1874', 'Domenico Scarlatti': '1685',
   'Georg Philipp Telemann': '1681', 'Pyotr Ilyich Tchaikovsky': '1840', 'John Stainer': '1840',
   'Antonín Dvořák': '1841', 'Beatrice Ohanessian': '1927', 'Eve Beglarian': '1958', 
   'Aziza Mustafa Zadeh':'1969', 'Gustav Mahler': '1860', 'Sergei Prokofiev': '1891', 
   'Dmitri Shostakovich': '1906', 'Igor Stravinsky': '1882', 'Alexander Scriabin': '1872', 
   'Heitor Villa-Lobos ':'1887', 'Alexandra Fol': '1981', 'Inés Medina-Fernández': '1974', 
   'Johannes Brassart':'1400', 'Tomaso Albinoni': '1671', 'Sophia Maria Westenholz': '1759', 
   'Franz Schubert':'1797'}

# Step 2: Create the Quiz File and Shuffle the Question Order:

for quizNum in range(15):
# Create the quiz and answer key files.
    quizFile = open(f'yearsquiz{quizNum + 1}.txt', 'w', encoding='utf-8')
    answerKeyFile = open(f'yearsquiz_answers{quizNum + 1}.txt', 'w', encoding='utf-8')

# Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(('' * 20) + f'Classical Composers year of birth Quiz(Form{quizNum + 1})')
    quizFile.write('\n\n')

# Shuffle the order of composers.
    composers = list(years.keys())
    random.shuffle(composers)

# Step 3: Create the Answer Options:

# Loop through all 25 composers, making a question for each.
    for questionNum in range(25):
    # Get right and wrong answers:
        correctAnswer = years[composers[questionNum]]
    # Duplicates all values in the years dictionary and passing it to a list 
    # of possible wrong answers.
        wrongAnswers = list(years.values())
    # deleting the correct answer from the wrong answer list.
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
    # selecting 3 random values from the wrong answer list.
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

# Step 4: Write Content to the Quiz and Answer Key Files:
     
# Write the question and the answer options to the quiz file:
        quizFile.write(f'{questionNum + 1}. What is the year of birth of {composers[questionNum]}?\n') 
        for i in range(4):
           quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n") 
        quizFile.write('\n')

# Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

# Close files   
    quizFile.close()
    answerKeyFile.close()
