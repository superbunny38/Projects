import random
from tkinter import*
from collections import deque

#mbti 리스트
mbti_list = ['INFP', 'ENFP', 'INFJ', 'ENFJ', 'INTJ', 'ENTJ', 'INTP', 'ENTP'
            ,'ISFP', 'ESFP', 'ISTP', 'ESTP', 'ISFJ', 'ESFJ', 'ISTJ', 'ESTJ']

# 궁합표 순서에 의한 MBTI 궁합 점수 2차원 배열에 저장
mbti_chemistry = [
        [4,4,4,5,4,5,4,4,1,1,1,1,1,1,1,1],
        [4,4,5,4,5,4,4,4,1,1,1,1,1,1,1,1],
        [4,5,4,4,4,4,4,5,1,1,1,1,1,1,1,1],
        [5,4,4,4,4,4,4,4,5,1,1,1,1,1,1,1],
        [4,5,4,4,4,4,4,5,3,3,3,3,2,2,2,2],
        [5,4,4,4,4,4,5,4,3,3,3,3,2,2,2,2],
        [4,4,4,4,4,5,4,4,3,3,3,3,2,2,2,5],
        [4,4,5,4,5,4,4,4,3,3,3,3,2,2,2,2],
        
        [1,1,1,5,3,3,3,3,2,2,2,2,3,5,3,5],
        [1,1,1,1,3,3,3,3,2,2,2,2,5,3,5,3],
        [1,1,1,1,3,3,3,3,2,2,2,2,3,5,3,5],
        [1,1,1,1,3,3,3,3,2,2,2,2,5,3,3,3],
        [1,1,1,1,2,3,2,2,3,5,3,5,4,4,4,4],
        [1,1,1,1,2,3,2,2,5,3,5,3,4,4,4,4],
        [1,1,1,1,2,3,2,2,3,5,3,3,4,4,4,4],
        [1,1,1,1,2,3,5,2,5,3,5,3,4,4,4,4]
       ]

# 그래프 노드 클레스
class Node:
    def __init__(self, std_ID, mbti, age, real_name):
        self.std_ID = std_ID#학번
        self.mbti = mbti#MBTI
        self.age = age#나이
        self.real_name = real_name#이름
    
# 그래프 생성        
class Graph:
    def __init__(self, std_dict, std_info): #그래프 생성
        self.std_dict = std_dict #edge & vertex
        self.std_info = std_info #node info
        
    def existName(self, std_ID):#학번이 이미 데이터베이스에 저장되어 있는지 확인
        for std in self.std_info:
            if std.std_ID == std_ID:
                return True
        return False
    
    def addStudent(self, std_ID, mbti, age, aquaintance, real_name):#학생 노드 생성       
        std = Node(std_ID, mbti, age, real_name)#노드 저장
        self.std_info.append(std)
        
        self.std_dict[std_ID] = aquaintance#간선 저장
        for aq in aquaintance:
            self.std_dict[aq].append(std_ID)
        
        return std

    def deleteStudent(self, std_ID):#학생 노드 삭제
        text = ""
        if self.existName(std_ID) == False:
            text += "존재하지 않는 학생입니다."
            return text
        
        for idx, node in enumerate(self.std_info):
            if node.std_ID == std_ID:
                pop_idx = idx

        self.std_info.pop(pop_idx)
        aquaintance = self.std_dict[std_ID]
        
        del self.std_dict[std_ID]
        for aq in aquaintance:
            if std_ID in self.std_dict[aq]:
                self.std_dict[aq].remove(std_ID)
        text += "삭제되었습니다."
        return text

    
    def searchName(self, std_ID):#학번으로 학생 노드 검색
        text = ""
        if self.existName(std_ID) == False:
            text += "존재하지 않는 학생입니다."
            print("t")
            return text
        else:
            for std in self.std_info:
                if std.std_ID == std_ID:
                    #print(self.std_dict[std_ID])
                    return std#노드 반환
                
    def updateStudent(self,std_ID,update_what,update_to):#학생 노드 수정
        std_node = self.searchName(std_ID)#수정할 학생 노드 학번으로 검색
        idx = self.std_info.index(std_node)
        aquaintance=self.std_dict[std_ID]
        
        if update_what == 0:#이름 수정
            std_node.real_name = update_to
            return std_node
        
        elif update_what == 1:#학번 수정
            std_node.std_ID = update_to
            self.std_dict[update_to] = self.std_dict[std_ID]
            del self.std_dict[std_ID]
            for aq in aquaintance:
                self.std_dict[aq].remove(std_ID)
                self.std_dict[aq].append(update_to)
            self.std_info.pop(idx)
            self.std_info.append(std_node)
            return std_node
            
        elif update_what == 2:#mbti 수정
            std_node.mbti = update_to
            self.std_info.pop(idx)
            self.std_info.append(std_node)
            return std_node
            
        elif update_what == 3:#나이 수정
            std_node.age=update_to
            self.std_info.pop(idx)
            self.std_info.append(std_node)
            return std_node

        
    def display(self):#저장된 학생 모두 출력 (Print)
        text = ""
        text += "<학번 순서로 출력>"
        for idx,std_ID in enumerate(sorted(self.std_dict.keys())):
            std = graph.searchName(std_ID)
            #text += f"\n학생{idx+1} : {std.real_name} ({std.std_ID})  [나이] {std.age}  [MBTI] {std.mbti}"
            text += "\n학생{0:>3} : {1: >5} ({2: >10})  [나이] {3: >3}  [MBTI] {4: >6}".format(idx+1, std.real_name, std.std_ID, std.age, std.mbti)
        return text



    #추가 기능 구현을 위한 함수들

    #나이차이에 따른 가산점 부여
    def ageScore(self, me, friend):
        ageS = abs(me - friend)
        if ageS == 0:
            return 5
        elif ageS >= 1 and ageS <=2:
            return 4
        elif ageS >=3 and ageS <=5:
            return 3
        elif ageS >=6 and ageS <=8:
            return 2
        else:
            return 1
        
    #겹치는 지인 수를 계산해주는 함수
    def countSameFriend(self, me, friend):
        my_friend = self.std_dict[me.std_ID]
        friend_friend = self.std_dict[friend.std_ID]
        my_friend = list(set(my_friend))
        friend_friend = list(set(friend_friend))
        set_my_friend = set(my_friend)
        set_friend_friend = set(friend_friend)
        count = len(set_my_friend&set_friend_friend)
        return count
        
        
    #me와 friend 인스턴스를 인자로 받아 int형 궁합점수를 리턴하는 함수 생성
    def chemistryScore(self, me, friend):
        text = ""
        text += "나와 친구의 궁합점수는: "
        mymbtiIdx = mbti_list.index(me.mbti)
        friendmbtiIdx = mbti_list.index(friend.mbti)
        score = self.ageScore(me.age, friend.age) + mbti_chemistry[mymbtiIdx][friendmbtiIdx] + self.countSameFriend(me,friend)
        text += str(score)
        return text

    #나와 간선으로 도달할 수 있는 친구를 찾기 위해 BFS 알고리즘 사용
    #탐색 완료된 노드를 리스트에 담아 리턴
    def bfs(self, graph, start):
        visited_nodes = []
        adjacency_nodes = deque([start])

        while adjacency_nodes:
            node = adjacency_nodes.popleft()
            if node not in visited_nodes:
                visited_nodes.append(node)
                adjacency_nodes.extend(graph[node])

        return visited_nodes

    #나와 간선으로 연결되지만 나와 이미 친구사이가 아닌 학생들을 대상으로 궁합점수 기반 친구추천을 해주는 함수
    def friendRecommendation(self, me):
        text = ""
        text += "다른 추천친구와의 궁합점수를 보여드립니다."
        text += "\n"
       
        #나와 간선으로 연결되어 있는 친구에 한해 친구 추천
        connected_friends = self.bfs(self.std_dict, me.std_ID)
        #그 중에서도 이미 나와 친구인 학생은 제외(친구 추천 기능이므로)
        myFreinds = self.std_dict[me.std_ID]
        complement = list(set(connected_friends) - set(myFreinds))
        #print(complement)

        #궁합점수를 확인할 친구들만을 대상으로 궁합점수를 매겨 딕셔너리에 삽입
        friendsScoreDict = {}
        for std in complement:
            if std == me.std_ID:
                continue
            score = self.chemistryScore(me, self.searchName(std))
            friendsScoreDict[std] = score
            
        # value 값으로 내림차순 정렬  
        d = dict(sorted(friendsScoreDict.items(), key=lambda x: x[1], reverse=True))
        count = 0
        for k, v in d.items():
            if count > 2:
                break    
            text += "\n" + "추천친구 이름: " + str(self.searchName(k).real_name)
            text += ', ' + str(v)
            count+=1
        return text
        

#학생 학번과 관계
graph_elements = {
   "2005000000" : ["2007000000", "2016000001", "1970000000", "2016000000", "2019310368"],
   "2007000000" : ["2005000000", "2011000000", "2021310809"],
   "2011000000" : ["2007000000", "2012000000"],
   "2012000000" : ["2011000000"],
   "2016000000" : ["2005000000", "2018312824", "2019310368", "1970000000"],
   "2016000001" : ["2005000000", "1550000000"],
   "2018312824" : ["2016000000"],
   "2019310368" : ["2005000000", "2016000000", "2021310809"],
   "2021310809" : ["2007000000", "2019310368"],
   "1550000000": ["2016000001"],
   "1970000000": ["2005000000", "2016000000"]
}


#기존 학생 저장할 배열
info_list = []

#기존 학생 11명 생성 후 저
std1 = Node("2005000000", mbti_list[9], 38, "송중기")
info_list.append(std1)
std2 = Node("2007000000", mbti_list[11], 37, "스윙스")
info_list.append(std2)
std3 = Node("2011000000", mbti_list[4], 39, "구혜선")
info_list.append(std3)
std4 = Node("2012000000", mbti_list[1], 32, "조보아")
info_list.append(std4)
std5 = Node("2016000000", mbti_list[2], 25, "차은우")
info_list.append(std5)
std6 = Node("2016000001", mbti_list[4], 24, "신예은")
info_list.append(std6)
std7 = Node("2018312824", mbti_list[15], 24, "류채은")
info_list.append(std7)
std8 = Node("2019310368", mbti_list[12], 25, "배병찬")
info_list.append(std8)
std9 = Node("2021310809", mbti_list[3], 21, "김기성")
info_list.append(std9)
std10 = Node("1550000000", mbti_list[3], 49, "율곡이이")
info_list.append(std10)
std11 = Node("1970000000",mbti_list[6], 66,"신동렬")
info_list.append(std11)


#그래프 객체 생성
graph = Graph(graph_elements, info_list)


# tkinter 구현

class SampleApp(Tk):
    def __init__(self): #초기 프레임 함수
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(Frame): #시작 화면
    def __init__(self, master):
        Frame.__init__(self, master)
        
        la0=Label(self, text="친구 추천 프로그램", font=('Helvetica', 16, "bold"))
        la1=Label(self,text='[MENU]',  font=('나눔고딕', 12), bg='yellow2', width=18)
        btn0=Button(self,text='1. 궁합 계산',font=('나눔고딕', 12), width=18,
               height=3, bg='OliveDrab1', command=lambda: master.switch_frame(chemistryScorePage))
        btn1=Button(self,text='2. 학생 추가',font=('나눔고딕', 12), width=18,
               height=3, bg='OliveDrab3', command=lambda: master.switch_frame(addStudentPage))
        btn2=Button(self,text='3. 학생 정보 삭제',font=('나눔고딕', 12), width=18,
               height=3, bg='OliveDrab3', command=lambda: master.switch_frame(deleteStudentPage))
        btn3=Button(self,text='4. 학생 정보 수정',font=('나눔고딕', 12), width=18,
               height=3, bg='OliveDrab3', command=lambda: master.switch_frame(updataInfoPage))
        btn4=Button(self,text='5. 모든 학생 조회',font=('나눔고딕', 12), width=18,
               height=3, bg='OliveDrab3', command=lambda: master.switch_frame(displayPage))
        btn5=Button(self,text='6. 특정 학생 조회',font=('나눔고딕', 12), width=18,
               height=3, bg='OliveDrab3', command=lambda: master.switch_frame(printOneStudentPage))
        btn6=Button(self,text='0. 종료',font=('나눔고딕', 12), width=18,
               height=3, bg='Gray', command=quit)
        
        la0.grid(row=0,column=1,pady=20)
        la1.grid(row=1,column=1)
        btn0.grid(row=2,column=0,padx=5,pady=10)
        btn1.grid(row=2,column=1,padx=5,pady=10)
        btn2.grid(row=2,column=2,padx=5,pady=10)
        btn3.grid(row=3,column=0,padx=5,pady=10)
        btn4.grid(row=3,column=1,padx=5,pady=10)
        btn5.grid(row=3,column=2,padx=5,pady=10)
        btn6.grid(row=4,column=0,padx=5,pady=10)

class chemistryScorePage(Frame): #1. 궁합 계산 페이지
    def __init__(self, master):
        def chemistryScorePageP():
            my_Id = en1.get()
            
            if graph.existName(my_Id) == True:
                me = graph.searchName(my_Id)
            else:
                tt1.set("존재하지 않는 학생입니다.\n본인의 정보를 입력해 주세요.")
                name = en2.get()
                age = int(en3.get())
                mbti = en4.get()
                mbti = mbti.upper()
                while mbti not in mbti_list:
                    tt1.set("MBTI 잘못 입력. 다시 입력해주세요.")
                    return
                aquaintance = [item for item in en5.get().split()]
                me = graph.addStudent(my_Id,mbti,age, aquaintance,name)
                tt1.set("추가되었습니다.")

            friend_name = en6.get()
            if graph.existName(friend_name) == False:
                tt1.set(f"{friend_name}님은 존재하지 않는 학생입니다.")
                return
            friend = graph.searchName(friend_name)
            ##궁합 점수 계산##
            tt1.set(f"<궁합 점수 계산 결과>")
            tt2.set(graph.chemistryScore(me, friend))
            
            rec_Friend_Dict = graph.friendRecommendation(me)
            tt3.set(rec_Friend_Dict)
            
            #for k, v in rec_Friend_Dict.items():
               # print('추천친구 이름: ', k, ' ', '궁합점수: ',v)
                    
        Frame.__init__(self, master)
        tt1 = StringVar() # 가변 출력 문자 tkinter에서는 이거 써야함
        tt2 = StringVar()
        tt3 = StringVar()
        
        la0=Label(self, text="1. 궁합 계산", font=('Helvetica', 16, "bold"))

        la1=Label(self,text="내 학번 (등록자라면 학번만 입력)",  font=('나눔고딕', 12), width=30, anchor = "w")
        la2=Label(self,text="내 이름",  font=('나눔고딕', 12), width=30, anchor = "w")
        la3=Label(self,text="내 나이",  font=('나눔고딕', 12), width=30, anchor = "w")
        la4=Label(self,text="내 MBTI",  font=('나눔고딕', 12), width=30, anchor = "w")
        la5=Label(self,text="친구 학번 입력 (띄어쓰기로 구분)",  font=('나눔고딕', 12), width=30, anchor = "w")
        en1=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #내 학번
        en2=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #이름  
        en3=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #나이
        en4=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #MBTI
        en5=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #내 친구 학번
        
        la6=Label(self,text="나와 궁합 확인 할 친구 학번",  font=('나눔고딕', 12), width=30, anchor = "w")
        en6=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #나와 궁합 확인 할 친구
        
        la7=Label(self,text="친구와의 궁합 점수",  font=('나눔고딕', 12), width=30, anchor = "w")
        la8=Label(self,text="다른 추천 친구",  font=('나눔고딕', 12), width=30, anchor = "w")
        

        btn0=Button(self,text='궁합 확인하기',font=('나눔고딕', 12), width=16,
               height=3, bg='pink', command=chemistryScorePageP)
        btn1=Button(self,text="뒤로가기",font=('나눔고딕', 12), width=10,
               height=2, bg='lightgrey', command=lambda: master.switch_frame(StartPage))
        
        la9=Label(self,textvariable= tt1, font=('나눔고딕', 12),
                  width=40, height=2,fg='black',relief='solid',borderwidth=1)
        la10=Label(self,textvariable= tt2, font=('나눔고딕', 12),
                  width=40, height=2,fg='black',relief='solid',borderwidth=1)
        la11=Label(self,textvariable= tt3, font=('나눔고딕', 12),
                  width=40, height=6,fg='black',relief='solid',borderwidth=1)
                
        la0.grid(row=0,column=0,pady=20)
        btn0.grid(row=7,column=1,padx=5,pady=10)
        btn1.grid(row=0,column=1)
        la1.grid(row=1,column=0)
        la2.grid(row=2,column=0)
        la3.grid(row=3,column=0)
        la4.grid(row=4,column=0)
        la5.grid(row=5,column=0)
        la6.grid(row=6, column=0,pady=5)
        en1.grid(row=1,column=1)
        en2.grid(row=2,column=1)
        en3.grid(row=3,column=1)
        en4.grid(row=4,column=1)
        en5.grid(row=5,column=1)
        en6.grid(row=6,column=1,pady=5)
  
        
        la7.grid(row=10, column=0)
        la8.grid(row=11, column=0)
        la9.grid(row=9, column=1)
        la10.grid(row=10, column=1)
        la11.grid(row=11, column=1)

class addStudentPage(Frame): #2. 학생 추가 페이지
    def __init__(self, master):
        def addStudentP():
            std_ID = en1.get()
            name= en2.get()
            mbti = en3.get()
            mbti = mbti.upper() #mbti 소문자 입력에 대한 예외처리
            while mbti not in mbti_list:
                tt1.set("MBTI 잘못 입력. 다시 입력해주세요.")
                return
            age = int(en4.get())
            while age < 1:
                tt1.set("나이 잘못 입력. 다시 입력해주세요.")
                return
            aquaintance = [item for item in en5.get().split()]
            new_std = graph.addStudent(std_ID,mbti,age,aquaintance,name)
            tt1.set("추가되었습니다.")
                
        Frame.__init__(self, master)
        tt1 = StringVar()
        
        la0=Label(self, text="2. 학생 추가", font=('Helvetica', 16, "bold"))
        
        la1=Label(self,text="추가할 친구 학번",  font=('나눔고딕', 12), width=30, anchor = "w")
        la2=Label(self,text="추가할 친구 이름",  font=('나눔고딕', 12), width=30, anchor = "w")
        la3=Label(self,text="추가할 친구 MBTI",  font=('나눔고딕', 12), width=30, anchor = "w")
        la4=Label(self,text="추가할 친구 나이",  font=('나눔고딕', 12), width=30, anchor = "w")
        la5=Label(self,text="친구 학번 입력 (띄어쓰기로 구분)",  font=('나눔고딕', 12), width=30, anchor = "w")

        en1=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #학번
        en2=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #이름
        en3=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #MBTI    
        en4=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #나이
        en5=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black') #친구

        btn0=Button(self,text='추가하기',font=('나눔고딕', 12), width=16,
               height=3, bg='pink', command=addStudentP)
        btn1=Button(self,text="뒤로가기",font=('나눔고딕', 12), width=10,
               height=2, bg='lightgrey', command=lambda: master.switch_frame(StartPage))
        
        la6=Label(self,textvariable= tt1, font=('나눔고딕', 12),
                  width=40, height=5,fg='black',relief='solid',borderwidth=1)
                
        la0.grid(row=0,column=0,pady=20)
        btn1.grid(row=0,column=1)
        la1.grid(row=1,column=0)
        la2.grid(row=2,column=0)
        la3.grid(row=3,column=0)
        la4.grid(row=4,column=0)
        la5.grid(row=5,column=0)
        en1.grid(row=1,column=1)
        en2.grid(row=2,column=1)
        en3.grid(row=3,column=1)
        en4.grid(row=4,column=1)
        en5.grid(row=5,column=1)
        btn0.grid(row=6,column=1,padx=5,pady=10)
        la6.grid(row=7, column=1)

class deleteStudentPage(Frame): #3. 학생 정보 삭제
    def __init__(self, master):
        def deleteStudentP():
            std_ID = en0.get()
            if graph.existName(std_ID) == False:
                tt1.set(f"{std_ID}는 존재하지 않는 학생입니다.")
            #graph.deleteStudent(std_ID)
            tt1.set(graph.deleteStudent(std_ID))
            
        Frame.__init__(self, master)
        tt1 = StringVar()
        
        la0=Label(self, text="3. 학생 정보 삭제", font=('Helvetica', 16, "bold"))
        btn0=Button(self,text='삭제하기',font=('나눔고딕', 12), width=16,
               height=3, bg='pink', command=deleteStudentP)
        btn1=Button(self,text="뒤로가기",font=('나눔고딕', 12), width=10,
               height=2, bg='lightgrey', command=lambda: master.switch_frame(StartPage))
        la1=Label(self,text="삭제할 친구 학번",  font=('나눔고딕', 12), width=30, anchor = "w")
        en0=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black')
        la5=Label(self,textvariable= tt1, font=('나눔고딕', 12),
                  width=40, height=10,fg='black',relief='solid',borderwidth=1)
                
        la0.grid(row=0,column=0,pady=20)
        btn0.grid(row=3,column=0,padx=5,pady=10)
        btn1.grid(row=0,column=1)
        la1.grid(row=1,column=0)
        en0.grid(row=2,column=0)
        la5.grid(row=4, column=0)
        
class updataInfoPage(Frame): #4. 학생 정보 수정 페이지
    def __init__(self, master):
        def updataInfoPage():
            std_ID = en0.get()
            if graph.existName(std_ID) == False:
                tt1.set(f"{std_ID}는 존재하지 않는 학생입니다.")
                
            update_what = en1.get()
            if update_what == '': #공백 입력 예외처리
                tt1.set("수정할 내용을 선택해 주세요.")
                return
            else:
                update_what = int(update_what)
                
            update_to = en2.get()
            if update_to == '': #공백 입력 예외처리
                tt1.set("수정할 내용을 입력해 주세요.")
                return
            
            if update_what == 3:
                update_to = int(update_to)
            if update_what == 2:
                update_to = update_to.upper()
                while update_to not in mbti_list:
                    tt1.set("MBTI 잘못 입력. 다시 입력해주세요.")
                    return
           
            std_node = graph.updateStudent(std_ID,update_what,update_to)
            print_str = f"<수정 후>\n{std_node.real_name}({std_node.std_ID})  [나이] {std_node.age}  [MBTI] {std_node.mbti}"
            
            tt1.set(print_str)
        
        Frame.__init__(self, master)
        tt1 = StringVar()
        
        la0=Label(self, text="4. 학생 정보 수정", font=('Helvetica', 16, "bold"))

        btn0=Button(self,text='수정하기',font=('나눔고딕', 12), width=16,
               height=3, bg='pink', command=updataInfoPage)
        btn1=Button(self,text="뒤로가기",font=('나눔고딕', 12), width=10,
               height=2, bg='lightgrey', command=lambda: master.switch_frame(StartPage))
        
        la1=Label(self,text="수정할 친구 학번",  font=('나눔고딕', 12), width=30, anchor = "w")
        la2=Label(self,text="수정할 내용 선택(숫자로 입력)", font=('나눔고딕', 12), width=30, anchor = "w")
        la3=Label(self,text="- 0.이름 1. 학번, 2. mbti, 3. 나이 - ",
                  font=('나눔고딕', 12), width=30, anchor = "w")
        la4=Label(self,text="수정할 내용 입력",  font=('나눔고딕', 12), width=30, anchor = "w")
        en0=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black')
        en1=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black')
        en2=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black')
        
        la5=Label(self,textvariable= tt1, font=('나눔고딕', 12),
                  width=40, height=10,fg='black',relief='solid',borderwidth=1)
                
        la0.grid(row=0,column=0,pady=20)
        btn0.grid(row=5,column=1, pady =10)
        btn1.grid(row=0,column=1)
        la1.grid(row=1,column=0)
        la2.grid(row=2,column=0)
        la3.grid(row=3,column=0)
        la4.grid(row=4,column=0)
        en0.grid(row=1,column=1)
        en1.grid(row=3,column=1)
        en2.grid(row=4,column=1)
        
        la5.grid(row=6, column=1)


class displayPage(Frame): #5. 모든 학생 조회 페이지
    def __init__(self, master):
        def displayP():
            tt1.set(graph.display())
        
        Frame.__init__(self, master)
        tt1 = StringVar()
        
        la0=Label(self, text="5. 모든 학생 조회", font=('Helvetica', 16, "bold"))

        btn0=Button(self,text='조회하기',font=('나눔고딕', 12), width=16,
               height=3, bg='pink', command=displayP)
        btn1=Button(self,text="뒤로가기",font=('나눔고딕', 12), width=10,
               height=2, bg='lightgrey', command=lambda: master.switch_frame(StartPage))
        
        la5=Label(self,textvariable= tt1, font=('나눔고딕', 12),
                  width=60, height=20,fg='black',relief='solid',borderwidth=1, justify = LEFT)
                
        la0.grid(row=0,column=0,pady=20)
        btn1.grid(row=0,column=1)
        btn0.grid(row=1,column=0,padx=5,pady=10)
        la5.grid(row=2, column=0)

class printOneStudentPage(Frame): #6. 특정 학생 조회 페이지
    def __init__(self, master):
        def printOneStudentP():
            std_ID = en0.get()
            if graph.existName(std_ID) == False:
                tt1.set(f"{std_ID}는 존재하지 않는 학생입니다.")
            else:
                std = graph.searchName(std_ID)
                tt1.set(f"{std.real_name}({std.std_ID})  [나이] {std.age}  [MBTI] {std.mbti}")
                
        
        Frame.__init__(self, master)
        tt1 = StringVar()
        
        la0=Label(self, text="6. 특정 학생 조회", font=('Helvetica', 16, "bold"))

        btn0=Button(self,text='조회하기',font=('나눔고딕', 12), width=16,
               height=3, bg='pink', command=printOneStudentP)
        btn1=Button(self,text="뒤로가기",font=('나눔고딕', 12), width=10,
               height=2, bg='lightgrey', command=lambda: master.switch_frame(StartPage))
        la1=Label(self,text="검색할 사람의 학번을 입력하세요",  font=('나눔고딕', 12), width=30, anchor = "w")
        en0=Entry(self,width=40, font=('나눔고딕',12), bg='white', fg='black')
       
        la5=Label(self,textvariable= tt1, font=('나눔고딕', 12),
                  width=60, height=10,fg='black',relief='solid',borderwidth=1)
                
        la0.grid(row=0,column=0,pady=20)
        btn1.grid(row=0,column=1)
        btn0.grid(row=3,column=0,padx=5,pady=10)
        la5.grid(row=4, column=0)
        la1.grid(row=1,column=0)
        en0.grid(row=2,column=0)
        
if __name__ == "__main__": #메인 프레임
    startwin = SampleApp()
    startwin.title("친구 추천 프로그램")
    startwin.geometry('700x500')
    startwin.mainloop()
