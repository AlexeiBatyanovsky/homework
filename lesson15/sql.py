from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from lesson15.models import Tarif, Usluga, db_add_new_data


sqlite_database = "sqlite:///database.db"
engine = create_engine(sqlite_database, echo=False)

# Session = sessionmaker(autoflush=False, bind=engine) # как один из вариантов создания сессии

with Session(autoflush=False, bind=engine) as db:
    db_add_new_data(engine, db)

    qs = db.query(Tarif).all()
    print(1, qs)
    
    for q in qs:
        print(2, q)
    
    for usluga in qs[1].usluga:
        print(3, usluga)
    qs = db.query(Usluga).all()
    print(qs)
    
    # q = db.query(Quiz).get(2)
    # print(2, q, q.question[1])
    
    # quests = db.query(Question).all()
    # for q in quests:
    #     print(q, q.quiz)
     
    # quests = db.query(Question).filter_by(id=1).one()
    # print(1111, quests)
    
    # quests = db.query(Question).filter(Question.id>6).all()
    # for q in quests:
    #     print(222, q, q.quiz)
    
    
    # from sqlalchemy import or_
    # db.users.filter(or_(db.users.name=='Ryan', db.users.country=='England'))
    
    
           
        
    # quests = db.query(Question).filter(Question.question.like('%море%')).all()
    # for q in quests:
    #     print(222, q, q.quiz)


    # ОБНОВЛЕНИЕ 
    # quiz = db.query(Quiz).get(1) # устарело - использовалось до 2.0
    # quiz = db.get(Quiz, 1)
    # quiz.name = "Новое название Квиза"
    # quiz.question[1].answer = 'Новый правильный ответ'    
    # db.commit()
    
    # quiz = db.query(Quiz).all()[0]
    # print(quiz.name)
    # print(*[f'{q.question} - {q.answer} \n' for q in quiz.question ]) # проверяем - все ок - обновилось
    
    
    # # УДАЛЕНИЕ    
    # quiz = db.get(Quiz, 1)
    # db.delete(quiz)
    # db.commit()
    # quizes = db.query(Quiz).all()
    # print(quizes)
    
    
    
    