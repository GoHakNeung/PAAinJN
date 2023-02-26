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

question_3 ='''Hello\n 
World 출력 
'''
test_set_3 = [
    {'input' : [], 'output' : ['Hello', 'World']},
]

question_4 ='''"C:\Download\hello.cpp" 출력 
'''
test_set_4 = [
    {'input' : [], 'output' : ['"C:\Downlad\Hello.cpp"']},
]

question_5 ='''#include<studio.h>
main()
{
    print("Hello World\n")
    
}출력 
'''
test_set_5 = [
    {'input' : [], 'output' : ['#include<studio.h>', 'main()', '{', '    print("Hello World\n")', '}']},
]



meta_data = [
    {'test_file' : '_0.py', 'answer' : test_set_0, 'question' : question_0},    
    {'test_file' : '_1.py', 'answer' : test_set_1, 'question' : question_1},
    {'test_file' : '_2.py', 'answer' : test_set_2, 'question' : question_2},
    {'test_file' : '_3.py', 'answer' : test_set_3, 'question' : question_3},
    {'test_file' : '_4.py', 'answer' : test_set_4, 'question' : question_4},
    {'test_file' : '_5.py', 'answer' : test_set_5, 'question' : question_5},
]
