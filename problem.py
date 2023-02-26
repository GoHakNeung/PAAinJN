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
answer_6 = [
    {'input' : [[10]], 'output' : [10]},
    {'input' : [[0]], 'output' : [0]},
    {'input' : [[-153]], 'output' : [-153]}
]

question_7 = '''문자 입력하면 입력 받은 문자 출력
'''
answer_7 = [
    {'input' : [['p']], 'output' : ['p']},
    {'input' : [['A']], 'output' : ['A']},
    {'input' : [['z']], 'output' : ['z']}
]

question_8 = '''실수 입력하면 입력 받은 실수 출력
'''
answer_8 = [
    {'input' : [[1.414]], 'output' : [1.414]},
    {'input' : [[0.005]], 'output' : [0.005]},
    {'input' : [[-1530.12]], 'output' : [-1530.12]}
]

question_9 = '''두 개의 정수를 입력 받아 두 개의 정수를 공백으로 구분하여 출력
'''
answer_9 = [
    {'input' : [[1],[2]], 'output' : ['1 2']},
    {'input' : [[0],[5]], 'output' : ['0 5']},
    {'input' : [[-5],[6]], 'output' : ['-5 6']}
]

question_10 = '''두 개의 문자를 입력 받아 두 개의 문자를 순서 바꾸어 공백으로 구분하여 출력
'''
answer_10 = [
    {'input' : [['a'],['b']], 'output' : ['b a']},
    {'input' : [['Q'],['l']], 'output' : ['l Q']},
    {'input' : [['t'],['U']], 'output' : ['U t']}, 
    {'input' : [['E'],['O']], 'output' : ['E O']}, 
]

question_11 = '''실수를 한 개를 입력받아 그 값을 소수점 셋째 자리에서 반올림하여 소수점 이하 둘째자리까지 출력
'''
answer_11 = [
    {'input' : [[1.535]], 'output' : [1.54]},
    {'input' : [[-5.1531]], 'output' : [-5.15]},
    {'input' : [[-5.1571]], 'output' : [-5.16]}, 
]

question_12 = '''정수 한 개를 입력받아 공백을 사이에 두고 3번 출력하기
'''
answer_12 = [
    {'input' : [[42]], 'output' : ['42 42 42']},
    {'input' : [[-536]], 'output' : ['-536 536 536']},
    {'input' : [[0]], 'output' : ['0 0 0']}, 
]

question_13 = '''두 정수가 :으로 구분하여 입력되거 정수:정수로 출력하기
'''
answer_13 = [
    {'input' : [['4:3']], 'output' : ['4:3']},
    {'input' : [['12:3']], 'output' : ['12:3']},
    {'input' : [['5:59']], 'output' : ['5:59']}, 
]

question_14 = '''세 정수가 .으로 구분하여 입력되고 yyyy.mm.dd로 출력하기
mm, dd에서 한 자리 수 앞에 0 붙이기
'''
answer_14 = [
    {'input' : [['2020.4.2']], 'output' : ['2020.04.02']},
    {'input' : [['1534.12.5']], 'output' : ['1534.12.05']},
    {'input' : [['5436.5.15']], 'output' : ['5436.05.15']}, 
    {'input' : [['5436.11.15']], 'output' : ['5436.11.15']},     
]

question_15 = '''실수 한 개를 입력받아 정수 부분과 실수 부분으로 나누어 출력하기
'''
answer_15 = [
    {'input' : [[1.414213]], 'output' : [1, 414213]},
    {'input' : [[453.15]], 'output' : [453, 15]},
    {'input' : [[1.0]], 'output' : [1, 0]}, 
    {'input' : [[-4531.153]], 'output' : [-4531, 153]},     
]

question_16 = '''정수 두 개를 변수로 입력받아 첫번째 숫자에서 두 번째 숫자로 나눈 몫을 출력
'''
answer_16 = [
    {'input' : [[10], [3]], 'output' : [3]},
    {'input' : [[4], [7]], 'output' : [0]},
    {'input' : [[123], [30]], 'output' : [4]},  
]

question_17 = '''정수 세 개가 공백을 두고 입력된다. 합과 평균을 줄 바꾸어 출력한다. 평균은 소수점 이하 둘째 자리에서 반올림하여 소수점 이하 첫째 자리까지 출력한다.
'''
answer_17 = [
    {'input' : [['1 2 3']], 'output' : [6, 2.0]},
    {'input' : [['3 6 9']], 'output' : [12, 6.0]},
    {'input' : [['-4 -9 0']], 'output' : [-13, -13/3]},  
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
]
