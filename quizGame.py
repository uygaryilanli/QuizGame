question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Questions:
    def __init__(self, q_text, q_answer): #Bu bölümü aşağıda yer alacak bütün fonksiyonlarda q_text ve q_answer parametrelerini kullanabilelim diye yazdım.
        self.q_text = q_text
        self.q_answer = q_answer
        self.q_number = 0
        self.score = 0
    
    def textAndAnswer(self):
        question_bank = []  # Sadece bu fonksiyon içinde kullanılacak bir liste oluşturdum.
        for data in question_data:
            question = data["text"] #question_data isimli liste içindeki sözlüklerden soruları çeker.
            answer = data["answer"] #question_data isimli liste içindeki sözlüklerden cevapları çeker.
            new_question = Questions(q_text=question, q_answer=answer) #Artık bu sınıf içindeki q_text question_list içindeki soruları q_answer ise cevapları içerecek.
            question_bank.append(new_question) #Soru ve cevapları question_bank isimli boş listeye ekliyoruz.
        return question_bank
    
    def next_question(self, question_list): #Buraya question_list parametresi atadık ki aşağıdaki işlemleri dışarıda bulunan question_data ya uygulayabilelim.
        current_question = question_list[self.q_number] #question_list dışardaki soru listesini, self.q_number ise index numarasını temsil ediyor.
        self.q_number += 1 #Soru numarasını 0 değil 1 den başlatmak için bunu son işlem olarak değil 2.ci işlem olarak ekledim.
        user_answer = input(f"Question {self.q_number}: {current_question.q_text} (True/False): ")
        self.check_answer(user_answer=user_answer, correct_answer=current_question.q_answer) #Cevapları kontrol ettiğimiz fonksiyonu burada kullandık.
    
    def check_answer(self, user_answer, correct_answer): #Yukarıdaki fonksiyon sonunda soru değiştirirken cevabın kontrolünü sağladığımız fonksiyon. 
        if user_answer.lower() == correct_answer.lower():
            print("That's True!")
            self.score += 1
        else:
            print("That's Wrong!")
            print(f"Correct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.q_number}")
    
    def still_has_questions(self, question_list):
        return self.q_number < len(question_list) #Eğer datadaki soruların sayısı, soru sayısından büyükse True değilse Flase döndürür.

# Soru listesini oluşturalım ve soruları soralım
quiz = Questions("", "") #Questions sınıfını quiz isimli değişkene atıyoruz.
question_bank = quiz.textAndAnswer() #question_bank isimli değişkene çekilecek bütün soruları aktarıyoruz.

# Kullanıcıya soruları gösterelim
while quiz.still_has_questions(question_bank): #question_bank isimli değişkeni soru sayılarını ele almak için ekledik.
    quiz.next_question(question_bank) #hangi listeden ilerliyceğimizi belirtmek için question_bank değişkenini ekledik.

# Tüm soruları sorduktan sonra sonucu gösterelim
print("Tüm sorular tamamlandı!")
print(f"Toplam skorunuz: {quiz.score}/{len(question_bank)}")
