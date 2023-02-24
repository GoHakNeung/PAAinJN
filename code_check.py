import sys, random, math, os, traceback
import pandas as pd
from IPython.core.display import display, HTML
from PAAinJN.problem import *

#------------------------------------------------------------------------------#
reset = '\033[0m'
tc_red = '\033[38;2;255;0;0m'
tc_green = '\033[38;2;0;255;0m'
bc_yellow = '\033[48;2;255;255;0m'
bc_green = '\033[48;2;0;255;0m'
bc_red = '\033[48;2;255;0;m'
#------------------------------------------------------------------------------#
def Question(html_content) : 
  display(HTML(html_content))
#------------------------------------------------------------------------------#
def code_arrange(py_name) : 
  global result, code, code_input, code_input_count 
  result= []
  code = []
  code_input_count = 0
  code_input = []

  file_name = '/content/'+py_name

  f = open(file_name, 'r')  # '/content/____.py 
  lines = f.readlines()
  for line in lines : 
    if line != '' : 
      code.append(line)    
      if line.find('input') >= 0 : 
        code_input_count += 1
        code_input.append(code.index(line))
  f.close()

  for i in range(len(code)) : 
    if code[i].find('\n') >= 0 : 
      code[i] = code[i][:-1]
    code[i] = code[i].rstrip()
#------------------------------------------------------------------------------#
def code_convert(answer_input) : 
  global test_py, answer_txt, original

  f = open(test_py, 'w')  
  original = sys.stdout
  sys.stdout = f

  print('import sys')
  print(f"f = open('{answer_txt}', 'w')")
  print('original = sys.stdout')
  print('sys.stdout = f')
  try : 
    order = 0  
    count = 0

    for order in range(len(code)) : 
      if order in code_input : 
        if len(answer_input[test_count]['input'][code_input.index(order)]) == 1 : 
          replace_input =  '"'+str(answer_input[test_count]['input'][code_input.index(order)][0])+'"' 
          print(code[order].replace('input()',replace_input))
       
        else : 
          replace_input =  str(answer_input[test_count]['input'][code_input.index(order)])
          print(code[order].replace('input().split()',replace_input))  

      else : 
        print(code[order])

    print('sys.stdout = original')
    print('f.close()')

    sys.stdout = original   
    f.close()                 
  except :  
    print('sys.stdout = original')
    print('f.close()')
    
    sys.stdout = original   
    f.close()

#------------------------------------------------------------------------------#
def code_test(answer_input) : 
  global user_answer, answer_txt, test_count
  user_answer = []
  answer_filename = '/content/'+answer_txt
  f = open(answer_filename, 'r')
  lines = f.readlines()

  for line in lines :  
    line = line.strip()
    if line != '' : 
      user_answer.append(str(line))
  f.close()

  answer_input[test_count]['output'] = list(map(str, answer_input[test_count]['output']))
  if user_answer == answer_input[test_count]['output'] : 
    result.append(True)
  else : 
    result.append(False) 

#------------------------------------------------------------------------------#
def code_print(py_name) :  
  global code  
  file_name = '/content/'+py_name
  f = open(file_name, 'r')  # '/content/____.py  
  lines = f.readlines()
  error_count = error_line()
  code_count = 1

#   for line in lines[4:-2] : 
  for line in lines[4:4+len(code)] :
    if error_count == code_count : 
      print(tc_red+line[:-1]+reset)
      code_count += 1
    else : 
      print(line[:-1])
      code_count += 1
  f.close()
#------------------------------------------------------------------------------#
def code_print_syntax(py_name) :  
  global code
  file_name = '/content/'+py_name
  f = open(file_name, 'r')  # '/content/____.py  
  lines = f.readlines()

  for line in lines[4:4+len(code)] :
  #for line in lines[4:-2] : 
    print(line[:-1])
  f.close()
#------------------------------------------------------------------------------#
def error_line() : 
  trace = traceback.format_exc()
  error = ''
  line = ''
  for i in trace.split('\n') :  
    if i.find('string') >= 0 : 
      error = i.strip()    
  for i in error.split(',') : 
    if i.find('line') >= 0 : 
      line = i.strip()
  return int(line[line.find('e')+2:])-4
#------------------------------------------------------------------------------#
def name_error(test_py) : 
  print(error_line(), 'line. Check the name of the variable or command, or make sure that the string is quoted.')
  print("="*40)
  code_print(test_py)

def type_error(test_py) : 
  print('Did you type the correct number or letter?')
  print('Or did you input the correct number in ()?')
  print("="*40)
  code_print_syntax(test_py)

def attribute_error(test_py) : 
  print(error_line(), 'line. Did you enter properties or methods for the library?')
  print("="*40)
  code_print(test_py)

def value_error(test_py) : 
  print(error_line(), 'line. Did you enter the correct number, letter, or input?')
  print("="*40)
  code_print(test_py)

def index_error(test_py) : 
  print(error_line(), 'line. Please check the length of the list or tuple.')
  print("="*40)
  code_print(test_py)

def indentation_error(test_py) :   
  print(error_line(), 'line. Please check the spacing.')     
  print("="*40)
  code_print(test_py)  

def zerodivision_error(test_py) :   
  print(error_line(), 'line. You can\'t divide a number by zero.')           
  print("="*40)
  code_print(test_py)

def overflow_error(test_py) :  
  print(error_line(), 'line. A big number can\'t be expressed.')
  print("="*40)
  code_print(test_py)

def keyboard_interrupt(test_py) : 
  print('User stopped working.')

def syntax_error(test_py) : 
  print('It\'s a grammatical error. Check "command", ":", "()"')
  print("="*40)
  code_print_syntax(test_py)

def modulenotfound_error(test_py) :  
  print(error_line(), 'line. Please check the library.')
  print("="*40)
  code_print(test_py)

def else_error(test_py) :  
  print('코드 오류입니다.') 
  print("="*40)
  code_print(test_py)

def error_check(test_py) : 
  global compile_error, original
  compile_error = False
  try : 
    exec(open(test_py).read())
  except NameError : 
    sys.stdout = original 
    name_error(test_py)
    compile_error = True
    return
  except TypeError : 
    sys.stdout = original 
    type_error(test_py)
    compile_error = True
    return
  except AttributeError : 
    sys.stdout = original 
    attribute_error(test_py)
    compile_error = True
    return
  except ValueError : 
    sys.stdout = original 
    value_error(test_py)
    compile_error = True
    return
  except IndexError : 
    sys.stdout = original 
    index_error(test_py)
    compile_error = True
    return
  except IndentationError : 
    sys.stdout = original 
    indentation_error(test_py)
    compile_error = True
    return
  except ZeroDivisionError : 
    sys.stdout = original 
    zerodivision_error(test_py)
    compile_error = True
    return
  except OverflowError : 
    sys.stdout = original 
    overflow_error(test_py)
    compile_error = True
    return
  except KeyboardInterrupt : 
    sys.stdout = original 
    keyboard_interrupt(test_py)
    compile_error = True
    return
  except SyntaxError : 
    sys.stdout = original 
    syntax_error(test_py)
    compile_error = True
    return
  except ModuleNotFoundError : 
    sys.stdout = original 
    modulenotfound_error(test_py)
    compile_error = True
    return
  except : 
    sys.stdout = original 
    else_error(test_py)
    compile_error = True
    return

#------------------------------------------------------------------------------#

def code_check(py) :
  for i in range(len(test_set)) :
    if test_set[i]['test_file'] == py :
      global answer 
      answer = test_set[i]['answer']
      global question
      question = test_set[i]['question']   
  try : 
    code_arrange(py)
  except : 
    print('Generate an assessment code.')
    return
  if code_input_count : 
    if code_input_count != len(answer[0]['input']) :         
      print('Please check the input.')
      return

  Question('<h2 style = "background-color:yellow">Check the results</h2>')  

  global test_count
  for test_count in range(len(answer)) : 
    global test_py, answer_txt
    test_py = 'test'+str(test_count)+'.py'
    answer_txt = 'answer'+str(test_count)+'.txt'
    code_convert(answer)
    error_check(test_py)
    # 코드 실행 시 오류발생하면 확인 종료
    if compile_error == True :
      try : 
        return    
      except : 
        return    

    code_test(answer)        
    #입력이 없는 문제
    if len(answer[0]['input']) == 0 : 
      if result[test_count] == True : 
        Question('<li>Processed Data : </li>') 
        for i in user_answer : 
          if i == user_answer[-1] : 
            print(bc_yellow+str(i)+reset,tc_green+'O'+reset)
          else : 
            print(bc_yellow+str(i)+reset)
      else :
        Question('<li>Processed Data : </li>') 
        for i in user_answer : 
          if i == user_answer[-1] : 
            print(bc_yellow+str(i)+reset, tc_red+'X'+reset)
          else : 
            print(bc_yellow+str(i)+reset)
    else :  
    #입력이 있는 문제
      if result[test_count] == True : 
        Question('<li>Inputted Data : </li>') 
        for i in answer[test_count]['input'] :    
          if len(i) == 1 : 
            print(i[0])
          else : 
            for j in i : 
              if j == i[-1] : 
                print(j, end = '\n')
              else : 
                print(j, end = ' ')              

        # for i in answer[test_count]['input'] : print(i)
        Question('<li>Processed Data : </li>') 
        for i in user_answer : 
          if i == user_answer[-1] : 
            print(bc_yellow+str(i)+reset, tc_green+'O'+reset)
          else : 
            print(bc_yellow+str(i)+reset)
      else : 
        Question('<li>Inputted Data : </li>') 
        for i in answer[test_count]['input'] :    
          if len(i) == 1 : 
            print(i[0])
          else : 
            for j in i : 
              if j == i[-1] : 
                print(j, end = '\n')
              else : 
                print(j, end = ' ')              

        Question('<li>Processed Data : </li>') 
        for i in user_answer : 
          if i == user_answer[-1] : 
            print(bc_yellow+str(i)+reset,tc_red+'X'+reset)
          else : 
            print(bc_yellow+str(i)+reset)
    Question('<HR>')
  if sum(result) == test_count+1 :
    try : 
      print(tc_green+'Right Answer'+reset)
    except : 
      print(tc_green+'Right Answer'+reset)
  else : 
    try : 
      print(tc_red+'Wrong Answer'+reset)
    except : 
      print(tc_red+'Wrong Answer'+reset)
