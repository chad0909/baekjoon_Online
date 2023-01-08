# 몇 문장을 받아줄 지 num_sen으로 받는다
num_sen = int(input())

# 위에서 입력받은 문장의 개수 만큼 반복
for i in range(num_sen):
	#X번째 문장을 받아준다
	sentence = list(input())
	save = [] #단어 내에서만 reverse되고 문장 자체에서의 단어는 reverse가 안되니 " "기준으로 reverse해주기 위해 배열 안에 단어를 저장해준다.
	for j in sentence: #전체 문장을 단어 하나씩 j에 넣고,
		if j != " ": # 빈칸이 안나오면 단어 한개로 간주하고 save에 넣는다
			save.append(j)
		else: #빈칸이 나와서 단어 한개가 완성이 되면, 
			save.reverse() #save를 거꾸로 만들고,
			for k in save: #하나씩 출력한다
				print(k, end="") #이때 Enter가 안쳐지게 end=""를 넣어준다
			print(" ", end="") #그리고 한칸을 띄워줘서 다음 단어를 받을 준비를 한다
			save = [] # save배열도 초기화하여 다은 단어를 준비한다
	save.reverse() #마지막 단어는 뒤에 " "가 없으니 따로 아래와 같이 처리해준다
	for k in save:
		print(k, end="")
	print() # 문장 당 Enter가 필요하니 추가해준 코드이다.