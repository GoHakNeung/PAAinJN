question_0 ='''<h2 style = "background-color:yellow; ">Description</h2>
<p>Let's create a program to print out whether <span style = "background-color : #E0E0E0">one number</span> you inputted is obtuse, right, or acute.</p>
<HR>
<h2> input
</h2>
<p>A integer between 1 and 179 is inputted</p>
<p>Units(&#176;) are omitted.</p>
<h2> output
</h2>
<p>Outputs one of acute, right, or obtuse.</p>
<HR>
<div style = "float:left;width:50%">
<h2> example input </h2>
<p>56</p>
</div>
<div style = "float:right;width:50%">
<h2> output example </h2>
<p>acute</p>
</div>
'''
test_set_0 = [
    {'input' : [[1]], 'output' : ['acute']},
    {'input' : [[89]], 'output' : ['acute']},
    {'input' : [[90]], 'output' : ['right']},
    {'input' : [[91]], 'output' : ['obtuse']},
    {'input' : [[179]], 'output' : ['obtuse']}
]

## 출력

question_1 ='''Hello 출력 
'''
test_set_1 = [
    {'input' : [], 'output' : ['Hello']},
]

question_2 ='''Hello World 출력 
'''
test_set_2 = [
    {'input' : [], 'output' : ['Hello World']},
]

question_3 ='''<p>Hello</p>
<p>World 출력 </p>
'''
test_set_3 = [
    {'input' : [], 'output' : ['Hello', 'World']},
]

question_4 ='''"C:\Download\Hello.cpp" 출력 
'''
test_set_4 = [
    {'input' : [], 'output' : ['"C:\\Download\\Hello.cpp"']},
]

question_5 ='''<p>#include<studio.h></p>
<p>main()</p>
<p>{</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;print("Hello World\n")</p>
<p>}</p>
<p>출력 </p>
'''
test_set_5 = [
    {'input' : [], 'output' : ['#include<studio.h>', 'main()', '{', '    print("Hello World\\n")', '}']},
]

#입력과 출력
question_6 = '''정수 입력하면 입력 받은 정수 출력
'''
test_set_6 = [
    {'input' : [[10]], 'output' : [10]},
    {'input' : [[0]], 'output' : [0]},
    {'input' : [[-153]], 'output' : [-153]}
]

question_7 = '''문자 입력하면 입력 받은 문자 출력
'''
test_set_7 = [
    {'input' : [['p']], 'output' : ['p']},
    {'input' : [['A']], 'output' : ['A']},
    {'input' : [['z']], 'output' : ['z']}
]

question_8 = '''실수 입력하면 입력 받은 실수 출력
'''
test_set_8 = [
    {'input' : [[1.414]], 'output' : [1.414]},
    {'input' : [[0.005]], 'output' : [0.005]},
    {'input' : [[-1530.12]], 'output' : [-1530.12]}
]

question_9 = '''두 개의 정수가 줄바꿈하여 입력 받아 두 개의 정수를 공백으로 구분하여 출력
'''
test_set_9 = [
    {'input' : [[1],[2]], 'output' : ['1 2']},
    {'input' : [[0],[5]], 'output' : ['0 5']},
    {'input' : [[-5],[6]], 'output' : ['-5 6']}
]

question_10 = '''두 개의 문자를 줄바꿈하여 입력 받아 두 개의 문자를 순서 바꾸어 공백으로 구분하여 출력
'''
test_set_10 = [
    {'input' : [['a'],['b']], 'output' : ['b a']},
    {'input' : [['Q'],['l']], 'output' : ['l Q']},
    {'input' : [['t'],['U']], 'output' : ['U t']}, 
    {'input' : [['E'],['O']], 'output' : ['O E']}, 
]

question_11 = '''실수를 한 개를 입력받아 그 값을 소수점 셋째 자리에서 반올림하여 소수점 이하 둘째자리까지 출력
'''
test_set_11 = [
    {'input' : [[1.535]], 'output' : [round(1.535,2)]},
    {'input' : [[-5.1531]], 'output' : [round(-5.1531,2)]},
    {'input' : [[-5.1571]], 'output' : [round(-5.1571,2)]}, 
]

question_12 = '''정수 한 개를 입력받아 공백을 사이에 두고 3번 출력하기
'''
test_set_12 = [
    {'input' : [[42]], 'output' : ['42 42 42']},
    {'input' : [[-536]], 'output' : ['-536 -536 -536']},
    {'input' : [[0]], 'output' : ['0 0 0']}, 
]

question_13 = '''두 정수가 :으로 구분하여 입력되거 정수:정수로 출력하기
'''
test_set_13 = [
    {'input' : [['4:3']], 'output' : ['4:3']},
    {'input' : [['12:3']], 'output' : ['12:3']},
    {'input' : [['5:59']], 'output' : ['5:59']}, 
]

question_14 = '''세 정수가 .으로 구분하여 입력되고 yyyy.mm.dd로 출력하기
mm, dd에서 한 자리 수 앞에 0 붙이기
'''
test_set_14 = [
    {'input' : [['2020.4.2']], 'output' : ['2020.04.02']},
    {'input' : [['1534.12.5']], 'output' : ['1534.12.05']},
    {'input' : [['5436.5.15']], 'output' : ['5436.05.15']}, 
    {'input' : [['5436.11.15']], 'output' : ['5436.11.15']},     
]

question_15 = '''실수 한 개를 입력받아 정수 부분과 실수 부분으로 나누어 출력하기
'''
test_set_15 = [
    {'input' : [[1.414213]], 'output' : [1, 414213]},
    {'input' : [[453.15]], 'output' : [453, 15]},
    {'input' : [[1.0]], 'output' : [1, 0]}, 
    {'input' : [[-4531.153]], 'output' : [-4531, 153]},     
]

question_16 = '''정수 두 개를 변수로 입력받아 첫번째 숫자에서 두 번째 숫자로 나눈 몫을 출력
'''
test_set_16 = [
    {'input' : [[10], [3]], 'output' : [3]},
    {'input' : [[4], [7]], 'output' : [0]},
    {'input' : [[123], [30]], 'output' : [4]},  
]

question_17 = '''정수 세 개가 공백을 두고 입력된다. 합과 평균을 줄 바꾸어 출력한다. 평균은 소수점 이하 둘째 자리에서 반올림하여 소수점 이하 첫째 자리까지 출력한다.
'''
test_set_17 = [
    {'input' : [['1 2 3']], 'output' : [6, 2.0]},
    {'input' : [['3 6 9']], 'output' : [18, 6.0]},
    {'input' : [['-4 -9 0']], 'output' : [-13, -13/3]},  
]

## 순차, 반복, 조건
question_18 = '''두 정수가 공백을 두고 입력된다. a가 b보다 크면 1 그렇지 않으면 0
'''
test_set_18 = [
    {'input' : [['1 2']], 'output' : [0]},
    {'input' : [['15323 12']], 'output' : [1]},
    {'input' : [['-4561 -456']], 'output' : [0]},  
]

question_19 = '''두 정수가 공백을 두고 입력된다. a와 b가 다른 경우 1, 그렇지 않은 경우 0을 출력한다.
'''
test_set_19 = [
    {'input' : [['1 2']], 'output' : [1]},
    {'input' : [['15323 12']], 'output' : [1]},
    {'input' : [['-4561 -4561']], 'output' : [0]},
    {'input' : [['12 12']], 'output' : [0]},
    {'input' : [['-4561 0']], 'output' : [1]},    
]

question_20 = '''정수 하나가 입력된다. 100~90 A, 89~70 B, 69~40 C, 39~0 D
'''
test_set_20 = [
    {'input' : [[73]], 'output' : ['B']},
    {'input' : [[99]], 'output' : ['A']},
    {'input' : [[53]], 'output' : ['C']},
    {'input' : [[1]], 'output' : ['D']},
    {'input' : [[71]], 'output' : ['B']},    
]

question_21 = '''1~12 입력, 봄-여름-가을-겨울 출력
'''
test_set_21 = [
    {'input' : [[12]], 'output' : ['winter']},
    {'input' : [[2]], 'output' : ['winter']},
    {'input' : [[3]], 'output' : ['spring']},
    {'input' : [[5]], 'output' : ['spring']},
    {'input' : [[6]], 'output' : ['summer']},    
    {'input' : [[8]], 'output' : ['summer']},        
    {'input' : [[9]], 'output' : ['fall']},    
    {'input' : [[11]], 'output' : ['fall']},    
]

question_22 = '''정수 하나 입력, 카운트 다운(정수부터 1까지)
'''
test_set_22 = [
    {'input' : [[12]], 'output' : [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]},
    {'input' : [[5]], 'output' : [5, 4, 3, 2, 1]},
    {'input' : [[3]], 'output' : [3, 2, 1]},
    {'input' : [[1]], 'output' : [1]},
]

question_23 = '''1부터 입력된 수까지의 수 중에서 짝수의 합을 출력한다.
'''
test_set_23 = [
    {'input' : [[6]], 'output' : [12]},
    {'input' : [[80]], 'output' : [1640]},
    {'input' : [[49]], 'output' : [600]},
]

question_24 = '''1,2,3,4,5... 계속 더해가다가 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.
'''
test_set_24 = [
    {'input' : [[55]], 'output' : [10]},
    {'input' : [[68]], 'output' : [11]},
    {'input' : [[25]], 'output' : [6]},
]


question_25 = '''1~10 사이 정수를 입력받으며 1부터 그 숫자까지 공백을 두고 출력하며 3,6,9에는 X(대문자)를 출력한다.
'''
test_set_25 = [
    {'input' : [[9]], 'output' : [1, 2, 'X', 4, 5, 'X', 7, 8, 'X']},
    {'input' : [[5]], 'output' : [1, 2, 'X', 4, 5]},
    {'input' : [[2]], 'output' : [1, 2]},
]

question_26 = '''rgb, 3 3 3은 r을 0 ~2, g는 0~2, b는 0 ~ 2를 표시할 수 있다. 
입력은 공백을 두고 입력된다. 출력은 공백을 안 둠.
'''
test_set_26 = [
    {'input' : [['2 2 2']], 'output' : ['000', '001', '010', '011', '100', '101', '110', '111']},
    {'input' : [['1 2 1']], 'output' : ['000', '010']},
    {'input' : [['3 2 1']], 'output' : ['000', '010', '100', '110', '200', '210']},
]

question_27 = '''정수 1개를 입력 받는다. 입력받은 숫자까지 출력을 하지만 3의 배수는 출력하지 안흔다. 
'''
test_set_27 = [
    {'input' : [[10]], 'output' : [1, 2, 4, 5, 7, 8, 10]},
    {'input' : [[5]], 'output' : [1, 2, 4, 5]},
    {'input' : [[15]], 'output' : [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]},
]

question_28 = '''등차수열 세 숫자가 공백을 두고 입력된다. 차례대로 시작값, 등차의 값, 몇 번째 수인지
'''
test_set_28 = [
    {'input' : [['1 3 5']], 'output' : [13]},
    {'input' : [['5 3 5']], 'output' : [17]},
    {'input' : [['99 -1 6']], 'output' : [94]},
]

question_29 = '''최대 공약수 두 수는 공백을 두고 입력 됨
'''
test_set_29 = [
    {'input' : [['64 128']], 'output' : [64]},
    {'input' : [['39 26']], 'output' : [13]},
    {'input' : [['2 9']], 'output' : [1]},
]

question_30 = '''정수 1개가 입력됨. n*n 배열에 1씩 커지도록
'''
test_set_30= [
    {'input' : [[4]], 'output' : ['1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16']},
    {'input' : [[3]], 'output' : ['1 2 3', '4 5 6', '7 8 9']},
    {'input' : [[5]], 'output' : ['1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15', '16 17 18 19 20', '21 22 23 24 25']}
]

meta_data = [
    {'test_file' : '_0.py', 'answer' : test_set_0, 'question' : question_0},    
    {'test_file' : '_1.py', 'answer' : test_set_1, 'question' : question_1},
    {'test_file' : '_2.py', 'answer' : test_set_2, 'question' : question_2},
    {'test_file' : '_3.py', 'answer' : test_set_3, 'question' : question_3},
    {'test_file' : '_4.py', 'answer' : test_set_4, 'question' : question_4},
    {'test_file' : '_5.py', 'answer' : test_set_5, 'question' : question_5},
    {'test_file' : '_6.py', 'answer' : test_set_6, 'question' : question_6},
    {'test_file' : '_7.py', 'answer' : test_set_7, 'question' : question_7},
    {'test_file' : '_8.py', 'answer' : test_set_8, 'question' : question_8},
    {'test_file' : '_9.py', 'answer' : test_set_9, 'question' : question_9},
    {'test_file' : '_10.py', 'answer' : test_set_10, 'question' : question_10},
    {'test_file' : '_11.py', 'answer' : test_set_11, 'question' : question_11},
    {'test_file' : '_12.py', 'answer' : test_set_12, 'question' : question_12},
    {'test_file' : '_13.py', 'answer' : test_set_13, 'question' : question_13},
    {'test_file' : '_14.py', 'answer' : test_set_14, 'question' : question_14},
    {'test_file' : '_15.py', 'answer' : test_set_15, 'question' : question_15},
    {'test_file' : '_16.py', 'answer' : test_set_16, 'question' : question_16},
    {'test_file' : '_17.py', 'answer' : test_set_17, 'question' : question_17},  
    {'test_file' : '_18.py', 'answer' : test_set_18, 'question' : question_18},
    {'test_file' : '_19.py', 'answer' : test_set_19, 'question' : question_19},
    {'test_file' : '_20.py', 'answer' : test_set_20, 'question' : question_20},
    {'test_file' : '_21.py', 'answer' : test_set_21, 'question' : question_21},
    {'test_file' : '_22.py', 'answer' : test_set_22, 'question' : question_22},
    {'test_file' : '_23.py', 'answer' : test_set_23, 'question' : question_23},
    {'test_file' : '_24.py', 'answer' : test_set_24, 'question' : question_24},
    {'test_file' : '_25.py', 'answer' : test_set_25, 'question' : question_25},
    {'test_file' : '_26.py', 'answer' : test_set_26, 'question' : question_26},
    {'test_file' : '_27.py', 'answer' : test_set_27, 'question' : question_27},      
    {'test_file' : '_28.py', 'answer' : test_set_28, 'question' : question_28},
    {'test_file' : '_29.py', 'answer' : test_set_29, 'question' : question_29},    
    {'test_file' : '_30.py', 'answer' : test_set_30, 'question' : question_30},        
]
