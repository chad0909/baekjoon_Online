# 몇 개의 괄호 세트를 받을지 변수 선언
num = int(input())

for _ in range(num): # 괄호 세트의 개수 만큼 반복
	bracket = list(input()) # 한 세트를 리스트로 하나씩 받는다
	if bracket[0] == ")": # 만약 처음 괄호부터 괄호를 닫아버리면 VPS가 안되니 바로 NO를 출력한다
		print("NO")
	else: # 괄호가 안닫혔다면
		count = 0 # 괄호의 개수가 같은지 확인하는 변수
		for i in bracket: # 괄호를 하나씩 넣어본다
			if i == "(": # ( 이면 count 에 1을 추가하고 만약 아니라면 -1를 추가해서 개수가 같은지 판단한다. 0이면 개수가 같음)
				count += 1
			else:
				count -= 1
# 괄호 개수가 같아도 VPS가 안될 수도 있다. 이는 먼저 ")"가 많아지면 VPS가 아니라는 의미이다. 그렇기에 바로 break를 시켜준다
			if count < 0:
				break

		if count == 0: # 괄호의 개수가 같으면 YES, VPS이다 (예외는 위의 if-else구문에서 처리해줌)
			print("YES")
		else: # count가 0이 아니면 VPS가 아니기에 NO 출력
			print("NO")
		
