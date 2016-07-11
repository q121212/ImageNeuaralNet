#neuralnet for transform one image to another


#first ver of transformation alg
def transform(inp_number, des_number, res_number = None, correction = None):
  if inp_number >= des_number:
    if des_number == 0:
      res_number = inp_number
    else:
      res_number = inp_number // des_number
  else:
    if inp_number == 0:
      res_number = inp_number
    else:
      res_number = des_number // inp_number
  if res_number == 0:
    correction = 0
  else:
    correction = inp_number/res_number
  result = [res_number, correction]
  return result
  

# method for adduction the input sequence to the desired sequence
def start_transform(inp_seq, desired_seq):
  result_seq = []
  result_corr_seq = []
  for i in inp_seq:
    result_seq_line = []
    result_corr_seq_line = []
    for j in desired_seq:
      result_seq_line.append(transform(i,j)[0])      
      result_corr_seq_line.append(transform(i,j)[1])
    result_seq.append(result_seq_line)
    result_corr_seq.append(result_corr_seq_line)
  result = [result_seq, result_corr_seq]
  return result

  
def reserve_transform(inp_seq, desired_seq):
  pass


def transform2(inp_number, des_number, res_number = None, correction = 1):
  if inp_number > des_number:
    res_number = inp_number - correction
    expected_times = res_number - des_number
  elif inp_number == des_number:
   res_number = inp_number
   correction = 0
   expected_times = 0
  else:
    res_number = inp_number + correction
    expected_times = des_number - res_number
  result = [res_number, correction, expected_times]
  return result

def start_transform2(inp_seq, desired_seq):
  result_seq = []
  result_corr_seq = []
  expected_times_seq = []
  for i in range(len(inp_seq)):
    result_seq.append(transform2(inp_seq[i], desired_seq[i])[0])
    result_corr_seq.append(transform2(inp_seq[i], desired_seq[i])[1])
    expected_times_seq.append(transform2(inp_seq[i], desired_seq[i])[2])
  result = [result_seq, result_corr_seq, expected_times_seq]
  return result

  
def part_adduction(inp_number, des_number, expected_times, part_adduction):
  result = None
  if expected_times == 0 or expected_times == 1:
    result = 0
  elif inp_number > des_number:
    result = -(inp_number - expected_times)//part_adduction
  else:
    result = -(inp_number + expected_times)//part_adduction
  return result
  

def start_part_adduction(inp_seq, des_seq, expected_times_seq, part):
  result= []
  for i in range(len(inp_seq)):
    result.append(part_adduction(inp_seq[i], des_seq[i], expected_times_seq[i], part))
  return result

  
# assumptions: len(imp_seq)  = len(desired_seq)
def neuron1(inp_seq, desired_seq):
  result_seq = []
  for i in range(len(inp_seq)):
    result_seq.append(abs(inp_seq[i]) - abs(desired_seq[i]))
  return result_seq


def neuron(inp_seq, desired_seq)  :
  result_seq = []
  for i in range(len(inp_seq)):
    values = compare_level_of_numbers(inp_seq[i], desired_seq[i])
    absvalue = abs(values[0]) - abs(values[1])
    if absvalue == 0:
      result_seq.append(1)
    else:
      result_seq.append(0)
  return result_seq


def training_neuron(neuron1, neuron2):
  if sum(neuron1) < sum(neuron2):
    pass
  elif sum(neuron1) == sum(neuron2):
    return neuron1
  else:
    pass
    
    
def compare_level_of_numbers(number1, number2):
  difflen = abs(len(str(number1)) - len(str(number2)))
  if difflen == 0 or difflen == 1:
    return [number1, number2]
  else:
    return [min(number1, number2)*10**difflen, max(number1, number2)]
    

def extract_data_from_file(file):
  with open(file, 'rb') as f:
    data = bytearray(f.read())
  return data
  

def main():
  # definitions of vars
  input_sequence0 = [1,2,0]
  desired_sequence0 = [10,20,0]
  input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, -1, -2, -5]
  desired_sequence1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10, 12, 20, 10, 20, 30, -50]
  desired_sequence2 = [101, 201, 350, 500, 700, 900, 1000, 800, 900, 1000, 10, 12, 20, 10, 20, 30, -50]
  desired_sequence3 = [5500.0, 2750.0, 1833.3333333333333, 1375.0, 1100.0, 916.6666666666666, 785.7142857142858, 687.5, 611.1111111111111, 550.0]
  desired_sequence4 = [3935.0, 1967.5, 1311.6666666666665, 983.75, 787.0, 655.8333333333333, 562.1428571428571, 491.875, 437.2222222222222, 393.5]
  
  print('input_sequence:   ' + str(input_sequence0))
  print('desired_sequence: ' + str(desired_sequence0))
  print('result sequence:')
  print(start_transform(input_sequence0, desired_sequence0)[0])
  print('result correction sequence:')
  
  print(start_transform2(input_sequence0, desired_sequence1))
  # print(start_transform(input_sequence, desired_sequence2))
  # print(start_transform(input_sequence, desired_sequence3))
  # print(start_transform(input_sequence, desired_sequence4))

  print('----')
  print(start_transform2(input_sequence, desired_sequence1))
  print()
  x=start_transform2(input_sequence, desired_sequence1)
  y=start_part_adduction(x[0],x[1], x[2], 3)
  print(y)
  print()
  z=start_part_adduction(y, desired_sequence1, x[2], 3)
  print(z)
  
  print('---------')
  newneuron = neuron1(input_sequence, desired_sequence1)
  print(newneuron)
  print(sum(neuron1(input_sequence, desired_sequence1)))
  for i in range(30):
    newneuron = neuron1(newneuron, desired_sequence1)
    print(newneuron)
    print(sum(neuron1(input_sequence, desired_sequence1)))
    print('----- ' + str(i) + ' -----')
  
  print('*----------------*')
  newneuron = neuron(input_sequence, desired_sequence1)
  print('\n' + str(input_sequence) +  '\n' + str(desired_sequence1) + '\n' + str(newneuron) + '\n' + str(sum(newneuron)))
  newneuron2 = neuron(input_sequence, desired_sequence2)
  print('\n' + str(input_sequence) +  '\n' + str(desired_sequence2) + '\n' + str(newneuron2) + '\n' + str(sum(newneuron2)))
  data = extract_data_from_file('1.bmp')
  print(data)
  x=0
  for i in data:
    print(i, end=' ')
    x+=1
  print(x)
  

if __name__ == '__main__':
  main()
  
  
# sources for reflections
# https://meduza.io/shapito/2015/06/19/hudozhnik-ot-gugla-neyronnye-seti-nauchilis-pisat-kartiny