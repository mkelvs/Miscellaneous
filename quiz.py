#! python3
# Random Quiz Generator

import random

#The quiz date - keys are states and values are captials

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

#Adjust range depending of number of Quizes to handout
for quizNum in range(2):
    
    af = open('capitalsquiz_answer{}'.format(quizNum + 1), 'w')
    with open('capitalsquiz{}'.format(quizNum + 1), 'w') as qf:
        qf.write('Name:\n\nDate:\n\nPeriod:\n\n')
        qf.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        qf.write('\n\n')


        states = list(capitals.keys()) #create a duplicate of all keys
        random.shuffle(states) 
        
        #Create 50 questions and answers
        for questionNum in range(50):
            correctAnswer = capitals[states[questionNum]] #capitals['randomkey'[index of random key]]
            wrongAnswers = list(capitals.values()) #creates a duplicate of all answers
            del wrongAnswers[wrongAnswers.index(correctAnswer)] #removes the correct answer located inside the wrongAnswers list. Locate using index
            wrongAnswers = random.sample(wrongAnswers, 3) #update variable containg 3 samples of wrong answers
            answerOptions = wrongAnswers + [correctAnswer] #answersOptions = [wrongAnswer, wrongAnswer, wrongAnwser, correctAnswer]
            random.shuffle(answerOptions)

            qf.write('{}. What is the capital of {}?\n'.format(questionNum + 1, states[questionNum]))
            for i in range(4):
                qf.write('\n{}. {}\n'.format('ABCD'[i], answerOptions[i]))
                qf.write('\n')
                
            #Write the answer key in another text file    
            af.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    af.close()
        


    
    
