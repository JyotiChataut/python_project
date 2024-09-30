# -*- coding: utf-8 -*-
import random

words = [
    {"spanish":"el","english": "the"},
    {"spanish":"de","english": "of"},
    {"spanish":"que","english": "that"},
    {"spanish":"y","english": "and"},
    {"spanish":"a","english": "to"},
    {"spanish":"en","english": "in"},
    {"spanish":"un","english": "a"},
    {"spanish":"ser","english": "to be"},
    {"spanish":"se","english": "oneself"},
    {"spanish":"no","english": "no"},
    {"spanish":"haber","english": "to have"},
    {"spanish":"por","english": "for"},
    {"spanish":"con","english": "with"},
    {"spanish":"su","english": "his/her/their"},
    {"spanish":"para","english": "for"},
    {"spanish":"está","english": "is"},
    {"spanish":"como","english": "as"},
    {"spanish":"pero","english": "but"},
    {"spanish":"más","english": "more"},
    {"spanish":"hacer","english": "to do"},
    {"spanish":"o","english": "or"},
    {"spanish":"este","english": "this"},
    {"spanish":"sí","english": "yes"},
    {"spanish":"sus","english": "his/her/their"},
    {"spanish":"mi","english": "my"},
    {"spanish":"ya","english": "already"},
    {"spanish":"ver","english": "to see"},
    {"spanish":"porque","english": "because"},
    {"spanish":"dar","english": "to give"},
    {"spanish":"cuando","english": "when"},
    {"spanish":"todo","english": "all"},
    {"spanish":"nos","english": "us"},
    {"spanish":"muy","english": "very"},
    {"spanish":"sin","english": "without"},
    {"spanish":"vez","english": "time"},
    {"spanish":"mucho","english": "much"},
    {"spanish":"quien","english": "who"},
    {"spanish":"desde","english": "from"},
    {"spanish":"todo","english": "everything"},
    {"spanish":"nosotros","english": "we"},
    {"spanish":"hablar","english": "to speak"},
    {"spanish":"algo","english": "something"},
    {"spanish":"tener","english": "to have"},
    {"spanish":"sí","english": "yes"},
    {"spanish":"cada","english": "each"},
    {"spanish":"tanto","english": "so much"},
    {"spanish":"él","english": "he"},
    {"spanish":"ella","english": "she"},
    {"spanish":"su","english": "your"},
    {"spanish":"tiempo","english": "time"},
    {"spanish":"poder","english": "to be able to"},
    {"spanish":"cosa","english": "thing"},
    {"spanish":"otro","english": "other"},
    {"spanish":"mismo","english": "same"},
    {"spanish":"venir","english": "to come"},
    {"spanish":"hacer","english": "to make"},
    {"spanish":"ver","english": "to see"},
    {"spanish":"saber","english": "to know"},
    {"spanish":"pasar","english": "to happen"},
    {"spanish":"deber","english": "should"},
    {"spanish":"poner","english": "to put"},
    {"spanish":"había","english": "there was"},
    {"spanish":"muchas","english": "many"},
    {"spanish":"nuevo","english": "new"},
    {"spanish":"al","english": "to the"},
    {"spanish":"bajo","english": "under"},
    {"spanish":"mientras","english": "while"},
    {"spanish":"nada","english": "nothing"},
    {"spanish":"uno","english": "one"},
    {"spanish":"bien","english": "well"},
    {"spanish":"parte","english": "part"},
    {"spanish":"cualquier","english": "any"},
    {"spanish":"volver","english": "to return"},
    {"spanish":"grande","english": "big"},
    {"spanish":"tan","english": "so"},
    {"spanish":"algo","english": "something"},
    {"spanish":"lugar","english": "place"},
    {"spanish":"pensar","english": "to think"},
    {"spanish":"así","english": "so"},
    {"spanish":"hasta","english": "until"},
    {"spanish":"cada","english": "each"},
    {"spanish":"mundo","english": "world"},
    {"spanish":"nuevo","english": "new"},
    {"spanish":"solo","english": "only"},
    {"spanish":"quedar","english": "to remain"},
    {"spanish":"trabajar","english": "to work"},
    {"spanish":"mismo","english": "same"},
    {"spanish":"donde","english": "where"},
    {"spanish":"nueva","english": "new"},
    {"spanish":"hombre","english": "man"},
    {"spanish":"mujer","english": "woman"},
    {"spanish":"si","english": "if"},
    {"spanish":"ver","english": "to see"},
    {"spanish":"hacer","english": "to do"},
    {"spanish":"casa","english": "house"}
]

def quiz_user(words):
    random.shuffle(words)
    score = 0
    
    for word in words:
        print(f"What is the english translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()
        
        if user_answer == correct_answer:
            print("Correct!!!\n")
            score += 1
        else:
            print(f"Wrong, The correct answer is '{word['english']}'.\n")
           
    print(f"Quiz complete! Your score: {score}/{len(words)}")
        

def main():
    print("Welcome to the language learning Flashcards App")
    input("Press Enter to start the quiz...")
    quiz_user(words)
    
    
if __name__ == "__main__":
    main()
