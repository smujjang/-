#시작화면
import random ## random 함수 쓰려면 모듈이 필요하므로 

while True:
    game = int(input(' 행맨게임(1)과 베팅게임(2) 종료(3)중 하나를 선택하시오. :'))

    if game == 1 :
            print('행맨게임')
            print('행맨게임을 시작합니다.')
            print('[게임 룰 설명]')
            print('"운동 종목"을 주제로 한 영단어 5개 중 랜덤으로 하나의 단어가 출제 됩니다.')
            print('기회는 총 세 번이 주어집니다. 그럼 시작~!')

            eng_words = ["swimming", "soccer", "baseball", "running"]
            answer = random.choice(eng_words)
            guess_letters = list("_" * len(answer))
            life = 3
            game_over = False
            
            while not game_over:
                print(f"남은 기회: {'❤' * life}번")
                user_guess = input("한 글자씩 추측해 보세요   >>>   ").lower()
                if len(user_guess) == 1 and user_guess.isalpha():
                    for i in range(len(answer)):
                        if answer[i] == user_guess:
                            guess_letters[i] = user_guess
                    print(guess_letters)
                    print()
                
                    if "_" not in guess_letters:
                        game_over = True
            
                        print("성공!!")
                    if user_guess not in answer:
                        life -= 1
                        if life == 0:
                            game_over = True
                            print(f" 실패!! 정답은 {answer} 입니다.")
                    else:
                        print("영어로 한 글자씩 입력해 주세요")
         
    elif game == 2 :
            print('베팅게임')
            print('베팅게임을 시작합니다.')
            print("배팅 게임에 오신 것을 환영합니다.")
            print("한 레벨을 통과하실 때마다 배팅 금액의 2배를 상금으로 받으실 수 있습니다.")
            print("레벨 통과에 실패하시면 모든 배팅 금액을 잃게 됩니다.")
            print("=" * 50)
            print()
            bet = int(input("배팅 금액을 입력하세요. 단위: $>>> "))
            print(f"총 ${bet}배팅하셨습니다.")


 
            door = ''' 

      @@@@@@@@@@@@   $$$$$$$$$$$$$   ***************
      @@        @@   $$         $$   **           **
      @@        @@   $$         $$   **           **
      @@  door  @@   $$   door  $$   **   door    **
      @@   1    @@   $$    2    $$   **     3     **
      @@        @@   $$         $$   **           **
      @@        @@   $$         $$   **           **
      @@@@@@@@@@@@   $$$$$$$$$$$$$   ***************

                '''

            road = '''


      a          a   b           b   c           c
       a   1     a   b    2     b    c    3     c
       a         a    b         b    c         c
        a        a    b        b    c         c
         a       a    b        b    c        c
          a      a     b      b    c        c
           a     a     b      b   c       c
             a     a  b      b   c       c 
                '''

           
            while True:
                
                winning_num = random.randint(1,3)
                #print(winning_num)
                num = random.randint(1,2)
                if num == 1:
                    print(road)
                    user_choice = int(input("3갈래의 길로 나뉘어 있습니다. 어느 길을 선택하시겠습니까? 1,2,3 >>>"))
                else:
                    print(door)
                    user_choice= int(input("총 3개의 문이 있습니다. 하나를 선택해주세요. 1,2,3 >>> "))
                
                if user_choice == winning_num:
                    print(f"축하합니다! 2배 획득!! 총 금액은 ${bet *2}가 되었습니다.")
                    bet = bet * 2
                    next_level = input("다음 단계로 이동하시겠습니까? 성공시 2배. 실패시 $0 y or n >>>").lower()

                    if next_level == 'y':
                        print("다음 단계로 이동합니다.")
                    elif next_level == 'n':
                        print(f"총 금액 ${bet}을 마지막으로 게임이 종료되었습니다.")
                        break
                    else:
                        print("잘못된 입력값입니다.\n")

                else:
                    print("아쉽네요. 모든 배팅 금액을 잃었습니다.")
                    break
            
    elif game == 3:
            print('프로그램 종료\n')
            break
    else:
        print('잘못 입력된 값입니다\n')
