'''
<야구게임 만들기>

---규칙정리---
(참고: https://www.youtube.com/watch?v=i5fvsBGUz6Q)
9회까지 경기
play : Team_A, Team_B로 나뉘어 경기
누가 먼저 공격할지 우선순위 랜덤으로 정하기

hitter 타자가 안타인지 홈런인지에 따라서 
안타 1. hits (0점, 1점, 2점, 3점)
홈런 2. homerun(0점, 1점, 2점, 3점 혹은 4점 만루홈런 grandslam)
스트라이크 3. s 3번이면 아웃
볼넷 4. b 출루주자수3인경우 볼넷이 나오면 1점 득점
아웃 5. o 타자아웃, 주자아웃 세개면 공격수비 바뀜

'''
import random

runner = [0,0,0]
hitter = ["hit", "homerun", "ball", "strike", "strike", "strike", "strike","strike","strike"]
s=0
b=0
out = 0
runnerout = 0

score = 0
scoreA = 0
scoreB = 0

Teams = ["Team_A", "Team_B"]
playTeam = " "

#공격팀 정하기
playTeam = random.choice(Teams)

#inning 9회까지 반복 
inning = 0
for inning in range(1,10):

    #inning 초 시작
    print("=====")
    print(inning, "inning: ", "초")
    out = 0
    s = 0
    b = 0
    runnerout = 0
    score = 0

    #현재팀
    print("현재공격팀: ", playTeam)

    while out < 3:
        score = 0
        #주자 상황 
        runner[0] = random.randint(0,1)
        runner[1] = random.randint(0,1)
        runner[2] = random.randint(0,1)
        print("주자상황: ", runner)

        runnersum=sum(runner)

        #투수가 던지고, 타자가 침 
        playnow = random.choice(hitter)

        #안타, 홈런, 볼, 스트라이크 상황에 따라 점수

        if playnow == "hit":
            print("안타")
            if runner[2]==1:
                inhome = random.randint(0,1)
                if inhome == 1:
                    score = 1
            if runner[1] ==1:
                inhome = random.randint(0,1)
                if inhome == 1:
                    score = 1
                
        elif playnow == "homerun":
            print("홈런")
            if runnersum == 0:
                score = 1
            elif runnersum == 1:
                score = 2
            elif runnersum ==2:
                score =3
            elif runnersum ==3:
                score = 4

        elif playnow == "ball":
            if runnersum ==3:
                if b==4:
                    score = 1
                elif b<4:
                    b = b+1
            print("볼 : ",b)
                
        elif playnow == "strike":
            if s==3:
                out = out+1
                print("아웃: ", out)
            elif s<3:
                s = s+1
            print("스트라이크 : ",s)


        #주자아웃 아웃 수에 추가하기 
        runnerout = random.randint(0,1)
        if runnerout==1:
            out = out+1
            print("주자아웃")

        #득점상황 현재 플레이팀에 반영하기
        if playTeam == "Team_A":
            scoreA = scoreA + score    
        elif playTeam == "Team_B":
            scoreB = scoreB + score
        print("A:B =", scoreA,":", scoreB)
        print("S:",s, "B:",b, "Out:", out)
        print("---")


        #아웃 3번이면 공격팀 교체    
        if out == 3:
            if playTeam == "Team_A":
                playTeam = "Team_B"
               
            elif playTeam == "Team_B":
                playTeam = "Team_A"

            print("아웃: ", out)
            print("=====")
            print("공격팀 교체: ", playTeam)



    #inning 말 시작
    print( inning,"inning: ", "말")
    out = 0
    s = 0
    b = 0
    runnerout = 0
    score = 0

    #현재팀
    print("현재공격팀: ", playTeam)

    while out < 3:
        score = 0
        #주자 상황 
        runner[0] = random.randint(0,1)
        runner[1] = random.randint(0,1)
        runner[2] = random.randint(0,1)
        print("주자상황: ", runner)

        runnersum=sum(runner)

        #투수가 던지고, 타자가 침 
        playnow = random.choice(hitter)

        #안타, 홈런, 볼, 스트라이크 상황에 따라 점수

        if playnow == "hit":
            print("안타")
            if runner[2]==1:
                inhome = random.randint(0,1)
                if inhome == 1:
                    score = 1
            if runner[1] ==1:
                inhome = random.randint(0,1)
                if inhome == 1:
                    score = 1
            if runner[0] ==1:
                inhome = random.randint(0,1)
                if inhome == 1:
                    score = 1
                
        elif playnow == "homerun":
            print("홈런")
            if runnersum == 1:
                score = 2
            elif runnersum ==2:
                score = 3
            elif runnersum ==3:
                score = 4

        elif playnow == "ball":
            if runnersum ==3:
                if b==4:
                    score = 1
                elif b<4:
                    b = b+1
            print("볼 : ",b)
                
        elif playnow == "strike":
            if s==3:
                out = out+1
                print("아웃: ", out)
            elif s<3:
                s = s+1
            print("스트라이크 : ",s)


        #주자아웃 아웃 수에 추가하기 
        runnerout = random.randint(0,1)
        if runnerout==1:
            out = out+1
            print("주자아웃")

        #득점상황 현재 플레이팀에 반영하기
        if playTeam == "Team_A":
            scoreA = scoreA + score    
        elif playTeam == "Team_B":
            scoreB = scoreB + score
        print("A:B =", scoreA,":", scoreB)
        print("S:",s, "B:",b, "Out:", out)
        print("---")


        #아웃 3번이면 공격팀 교체    
        if out == 3:
            if playTeam == "Team_A":
                playTeam = "Team_B"
               
            elif playTeam == "Team_B":
                playTeam = "Team_A"

            print("아웃: ", out)
            #print("공격팀 교체: ", playTeam)
            print(inning, "inning 종료")
            print("=====")

        #inng 결과 출력 
            
