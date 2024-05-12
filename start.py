import time
import tkinter as tk

def name_scene():
    name_window = tk.Tk()
    name_window.title("게임 시작")
    name_window.geometry("300x150")


    def start_game():
        name_window.destroy()
        prologuescene(user_name_entry.get())

    def exit_game():
        name_window.destroy()
    
    user_name_label = tk.Label(name_window, text="당신의 이름을 입력하세요:")
    user_name_label.pack()

    user_name_entry = tk.Entry(name_window)
    user_name_entry.pack()

    start_button = tk.Button(name_window, text="게임 시작", command=start_game)
    start_button.pack()

    exit_button = tk.Button(name_window, text="종료", command=exit_game)
    exit_button.pack()

    name_window.mainloop()

def prologuescene(user_name):
    print("_____________________________________________________________________________________")
    print("")
    print("")
    print("")
    print("2022년 3월 3일 뉴스")
    time.sleep(0.75)
    print("블라디미르 푸틴 서기장이 지난 2월 24일 11시 50분경 우크라이나 지역에 \'특별 군사 작전\'을 시행 했습니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("키이우 북쪽에서 전략 거점에서 우크라이나군과 러시아군의 교전이 일어났고,")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("어제부로 러시아 군이 확실한 우위를 점하고 끝났습니다. 현재 키이우는 러시아군의 통제하에 있습니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("세계 각국의 외교관들은 전세계에서의 확전을 두려워 하고 있습니다. ")
    time.sleep(0.75)
    print("")
    print("")
    print("2023년 2월 9일 뉴스")
    time.sleep(0.75)
    print("모스크바에서 우크라이나의 미래를 논의하기 위한 회담이 진행되었습니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("우크라이나 지역을 러시아로 합병 시키기 위한 주민 투표가 시행되었습니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("우크라이나 저항군들은 그들의 절망적인 상황에도 불구하고, 그들의 영토를 포기하길 거부하고 있습니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("러시아 쇼이구 국방장관은, \"더이상 이들을 지구상에 남겨두지 않을것\"이라는 기자회견을 했습니다.")
    time.sleep(0.75)
    print("")
    print("")
    print("")
    print("2024년 6월 15일 뉴스")
    time.sleep(0.75)
    print("중국은 대만의 독립 선언에 분개하여 하늘아래 두 정부는 있을수 없다는 사실을 공표했습니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("중국 외교부는 \"대만은 중국의 합법적인 영토이며 대만의 독립시도는 명박한 주권 침해\" 라고 .")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("이제 중국은 대만섬이 24시간 내에 독립 선언을 철회하고 국가 지도부 사퇴를 요구하고 있으며,")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("이를 따르지 않을 경우 힘든 대가를 치르게 할것 이라고 했습니다.")
    print("")
    time.sleep(0.75)
    print("미국 외교부 대변인은.\"세계 민주주의와 자유를 보존하는 것은 우리의 역할\"")
    print("")
    time.sleep(0.75)
    print("이라며 강한 대만 수호 의지를 나타냈습니다.")
    time.sleep(0.75)
    print("")
    print("")
    print("2024년 6월 17일 뉴스")
    time.sleep(0.75)
    print("중국은 전쟁 준비로 진먼섬 인근에 군대를 배치했습니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("대만 위기를 평화적으로 협상해 끝내고자 베이징에서 중국, 미국, 대만간의 회담이 열렸습니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("긴 회담 끝에 회담은 결렬되었습니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("중국-대만 해상국경에 중국 함대가 자리를 잡았고, 인근 해역을 지나는 모든 상선은 항로를 변경했습니다.")
    print("")
    time.sleep(0.75)
    print("\"박하늘 대위 입니다. 대통령실에서 해외 파병을 준비하라는 지시입니다!\"")
    print("")
    time.sleep(0.75)
    print("\"해병대 0.75사단, 육군 수기사단, 저희 0.75함대가 파병부대로 선정되었습니다!\"")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print(f"{user_name} : 알겠다. 총원 작전 준비! ")
    time.sleep(0.75)
    print("")
    print("")
    print("2024년 6월 30일")
    time.sleep(0.75)
    print("ROKN 독도함에서 사령부에게 전달! 우린 공격을 받고있다!")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("어제부터 본함을 추적하고 있던 미확인 잠수함의 공격으로 보이는 어뢰에 피격된것으로 보인다!")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("중국 해군 함정들이 본 함으로 항주해오고 있다! 기관부가 피격당해서 전투를 회피할수 없다!")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("제발 저들을 어떻게든지 못오게 해주십시오!........제발!")
    print("")
    time.sleep(0.75)
    print("(무선 잡음).................(폭발음이 들린다.))")
    print("")
    time.sleep(0.75)
    print("손원일함 오정훈 대령입니다!")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print(f"{user_name} : 오정훈 대령. 전투를 준비하게 하지만 아주 힘든 전투가 될거야! ")
    time.sleep(0.75)
    print("")
    print("2024년 7월 2일")
    time.sleep(0.75)
    print("전투 보고 드리겠습니다.... 파병부대 22척중 5척 침몰, 7척 중파, 2척 반파.... 본함도 반파 상태입니다..")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("오정훈 대령 : 지금 대통령실은 난리가 났습니다.. 본국으로 퇴각하라는 지시입니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print(f"{user_name} : 우리에게 선전포고도 없이 왜 공격한것이지? ")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("오정훈 대령 : 저희만 그런것이 아닙니다. 미국 함대와 자위대도 박살이 났습니다.")
    print("")
    time.sleep(0.75)
    print("너무 많은 인명이 하루아침에 희생됐다는 여론이 형성되며 엄청난수의 반전 시위대가 광화문을 뒤덮었다.")
    print("")
    time.sleep(0.75)
    print("시위대는 더이상 해외에 개입하지 않을 것을 요구하고 있습니다.")
    time.sleep(0.75)
    print("")
    print("")
    print("")
    print("2025년 4월 4일 뉴스")
    time.sleep(0.75)
    print("영국, 호주, 캐나다, 뉴질랜드 등 파이브 아이즈 국가들이 NATO 탈퇴를 선언했습니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("최근 몇년간 미국의 힘이 시들해져감에 따라서 미국 중심의 세계는 더이상 지속될수 없다고 했습니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("추가적으로 유럽내 NATO 회원국도 탈퇴를 고려중입니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("독일을 비롯한 유럽 국가는 내년부터 징병제를 실시하고 국방 예산을 대폭 증대한다고 발표 했습니다.")
    print("")
    print("")
    print("")
    print("2026년 1월 9일 뉴스")
    time.sleep(0.75)
    print("한때 같은 적을 두고 승리한 두 국가, 중국과 러시아에 새로운 군사 동맹이 체결되었습니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("이런 성장을 맞받아 치기 위해, 마지막 남은 서방세계 국가들이 힘을 합쳐야 하지만")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("미국이 없는 서방세계의 힘은 미미한 상태 입니다.")
    time.sleep(0.75)
    print("")
    print("")
    print("")
    print("2027년 9월 1일 뉴스")
    time.sleep(0.75)
    print("오늘 대통령실은 \"민주주의의 최전선에 있는 국가로써 핵개발과 항공모함 건조를 시작하겠다.\"라고 발표 했습니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("새로운 국방력 증대 계획은 2029년까지 완료될 계획입니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("최근 여론조사에 따르면 핵무장에 찬성하는 여론이 압도적으로 높았습니다.")
    time.sleep(0.75)
    print("")
    print("")
    print("")
    print("2028년 2월 17일 뉴스")
    time.sleep(0.75)
    print("")
    print("중국과 러시아로 구성된 국가동맹에 북한이 가입했다는 소식입니다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("새로운 아시아 동맹에 대한 증표로써 \'대가\'를 증정 했는지 의혹에 쌓여 있습니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("최근 비무장지대 근처에 물자와 인력 이동이 다수 포착되었습니다. 군은 항상 고도의 경계 상태를 유지 중입니다.")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("항공모함 건조는 절차를 가속하여 빠르면 올해 말 실전 배치에 투입할 예정입니다.")
    print("")
    print("")
    print("")
    print("2029년 2월 15일 D-DAY")
    time.sleep(0.75)
    print("")
    print("\"16수색의 민경록 소령입니다. 위성상으로 북괴군 이동을 포착했다지만 비무장지대에서 보기엔 특별한 사항은 없습니다!\"")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("\"소령, 거짓말 하진 않겠네. 북한군이 작전을 개시했어. 당신 부대는 생존 확률이 매우 희박하네,\"")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("\"그래도 방어 태세를 유지하게, 우리가 반격하는데 필요한 시간을 벌어줄거야\"")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("\"대규모 증원 병력이 올때까지 시간을 버는게 주요 임무일세\"")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    time.sleep(0.75)
    print("\"차준영 대위 입니다. 사령관님 동해로 초계 작전이 할당되었습니다.\"")
    print("")
    time.sleep(0.75)
    print(f"{user_name} : 알겠네!")
    print("")
    time.sleep(0.75)
    print("")
    print("")
    print("2030년 3월 1일 D+380일째")
    time.sleep(0.75)
    print("")
    print("양측 모두 큰 사상자를 냈지만 끝내, 마지막 방어선이 무너졌다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("\"미안하지만... 사령부와 연락이 안된다. 전선과의 통신망이 모두 끊겼어.\"")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("\"아.... 잠깐... 61연대의 초소와 연락이 된것같다.. 지금 연결해주지. \"")
    time.sleep(0.75)
    print("")
    time.sleep(0.75)
    print("\"제 61연대, 일병 박조하 입니다... 여긴 완전히 당했습니다. \"")
    print("")
    time.sleep(0.75)
    print("\"놈들이 포로를 잡을 생각도 하지 않고 그쪽으로 냅다 진격하고 있습니다!\"")
    print("")
    time.sleep(0.75)
    print("\"방금 저희 사단 본부가 통째로 날아갔습니다. 이제 저희 병력도 얼마 남지 않았습니다...\"")
    print("")
    time.sleep(0.75)
    print("\"...교신이 끊겼다. 계속 연락을 시도해보지.\"")
    print("")
    time.sleep(0.75)
    print("")
    print("")
    print("2030년 3월 6일 D+411일째")
    time.sleep(0.75)
    print("")
    print("\"방금 미군 본부와 연락이 됐다. 3일안에 미군이 우리를 도와주러 온다는군\"")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("\"현재 육군본부 30km 앞까지 진격해 왔다고 하네. 행운을 비네! 안수형 소령.\"")
    time.sleep(0.75)
    print("")
    print("")
    print("2030년 5월 23일 D+411일째")
    time.sleep(0.75)
    print("")
    print("미군의 인천 상륙작전은 또 다시 큰 사상자를 내며 처참히 실패했다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("또한, 대통령을 비롯한 정부 인사들은 미사일 공격을 받고 벙커와 함께 소멸한다.")
    time.sleep(0.75)
    print("") 
    time.sleep(0.75)
    print(" 북한군은 이 기세에 힘입어 부대를 재정비해 부산에 총 공세를 가했고")
    print("") 
    time.sleep(0.75)
    print("전세계 전쟁사에 길이남을 치열한 공방전 끝에 부산은 함락된다.")
    print("") 
    time.sleep(0.75)
    print(f"가까스로 탈출한 항공모함 \"상명함\"은 대한민국 최후의 영토 제주도로 출발한다")
    print("")
    print("")
    print("2031년 5월 6일")
    time.sleep(0.75)
    print("")
    print(f"{user_name} : 아 통영마저 북괴놈들에게 빼앗겼단 말인가...")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("오정훈 중장 : 이제 통영마저 뚫렸으니 바로 이곳으로 쳐들어 올것입니다. 어서 대책을 세워야 합니다!")
    time.sleep(0.75)
    print("") 
    time.sleep(0.75)
    print("오정훈 중장의 신들린 전술로 북한의 제주도 상륙을 막는데 가까스로 성공했지만")
    print("") 
    time.sleep(0.75)
    print("제주도는 잿더미가 되어 군사적, 경제적 손실이 엄청났다.")
    print("") 
    time.sleep(0.75)
    print(f"대한민국의 비상 행정부 수장 {user_name}은 기필코 북한에게 이 일을 복수하겠다고 다짐하고,")
    print("") 
    time.sleep(0.75)
    print("언젠가는 자신이 꼭 한반도를 되찾겠다고 결심한다.")
    print("") 
    time.sleep(0.75)
    print(f"{user_name}은 과연 이 결심을 현실로 이루어 낼수 있을것인가?")
    print("")
    print("")
    print("2032년 1월 1일")
    time.sleep(0.75)
    print("")
    print("한반도가 공산화 된지 6개월이 넘었지만 북한은 여전히 전국에서 각지에서 일어나는 시위, 테러를 진압하지 못하고 있다.")
    time.sleep(0.75)
    print("")                                    
    time.sleep(0.75)
    print("중국과 러시아는 진작 유럽으로 눈을 돌린 상태이고, 잿더미가 된 남한 지역을 재건하려면,")
    print("")                                    
    time.sleep(0.75)
    print("북한 자체 역량으로 족히 어림잡아 수십년은 걸릴것이다.")
    time.sleep(0.75)
    print("") 
    time.sleep(0.75)
    print(f"{user_name}은 지금이 한반도를 재통일할 기회라고 생각하여")
    print("") 
    time.sleep(0.75)
    print("\"한반도 재 수복 작전\"을 계획한다.")
    print("")
    print("_____________________________________________________________________________________")
    main(money,population,economy,research,power,attack)


def main(money,population,economy,research,power,attack):
    print("_____________________________________________________________________________________")
    print("게임 시작 : 1, 종료 : 2")
    print("_____________________________________________________________________________________")
    print(f"예산 : {money}")
    print(f"인구 : {population}")
    print(f"경제력 : {economy}")
    print(f"연구력 : {research}")
    print(f"예산 : {money}")
    print(f"군사력 : {power}")
    print(f"전투력 : {attack}")
    print(f"지역 수 : {region}")
    print("_____________________________________________________________________________________")
    main_choice=int(input("번호를 선택하십시오."))
    if main_choice == 2:
        exit()
    
    
    
money=1000
population=10000
economy=0
research=0
power=100
attack= 100 // 0.1
region = 2


name_scene()