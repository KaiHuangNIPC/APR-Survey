
import os
import json_lines
import json
import gzip
import re

def read_json_file(file_path):
    # with gzip.open(file_path, 'rt') as f: 
    #     data = f.read()
    # json_data = json.loads(data)
    all_file_lines = []
    all_path_lines = []
    
    num = 0
    with gzip.open(file_path, 'rt') as f:
        for line in f:
            num += 1
            data = json.loads(line)
            # print(data)
            

            # print(data['original_string'])
            # break
            code_path = data['path']
            code_func = data['original_string']
            code_str = code_func.replace('\n','').replace('\t','')
            code_str = re.sub(' +', '', code_str)
            # print(num)
            # print(code_str)
            all_file_lines.append(code_str)
            all_path_lines.append(code_path)
            
    
    
    return all_file_lines, all_path_lines

def read_file(path):
    with open(path, 'r') as f:
        f_lines = f.readlines()
    return f_lines

def read_d4j():
    path1 = '/home/huangk/dataset/Defects4J_dataset/all_D4j_bug/'
    id_file = path1 + 'index.txt'
    src_file = path1 + 'src-test.txt'
    tgt_file = path1 + 'tgt-test.txt'
    

    
    id_lines = read_file(id_file)
    src_lines = read_file(src_file)
    tgt_lines = read_file(tgt_file)
    
    # print(len(id_lines))
    fix_list = []

    id_list = [i.split(' ; ')[0].split('/')[0] for i in id_lines]
    # print(id_list)
    # print(len(set(id_list)))
    
    
    src_list, tgt_list = [], []
    
    for src, tgt in zip(src_lines, tgt_lines):
         
        src_split = src.split('<BUG')
        # print(src_split)
        tgt_split = tgt.split('<FIXE>')[:-1]
        tgt_split = [i.replace('<FIXS>', '') for i in tgt_split]
        # print(tgt_split)
        
        fix_str = ''
        index = 0
        for i,src_one in enumerate(src_split):
            if src_one[:3] == 'S> ':
                fix_str += tgt_split[index]
                index += 1
                src_split[i+1] = src_split[i+1][2:]
            else:
                fix_str += src_one
        # print(fix_str)
        
        fix_str = re.sub(' +', '', fix_str)
        # print(fix_str)
        fix_list.append(fix_str.strip())
                
                
    return id_list, fix_list    
        
        # break
        

        
        
    
    
    
    

def read_CSN_data():
    
    D4j_id, D4j_patch = read_d4j()
    
    
    # print(len(D4j_id))
    # print(len(D4j_patch))
    
    
    data_path = 'java/final/jsonl/train/'
    
    data_list = os.listdir(data_path)
    
    
    # print(data_list)
    overlap_list = []
    
    overlap_result_list = []
    
    
    for file_path in data_list:
        file_name = file_path
        file_path = data_path + file_path
        print(file_path)
        
        file_data, file_path = read_json_file(file_path)
        print(len(file_data))
        
        
        
        for code_line, code_path in zip(file_data, file_path):
            
            # if 'isOnlyAssignmentSameScopeAsDeclaration' in code_line.strip():
            #     print(file_data)
                # break
            # print(code_line)
            
            
            for id, D4j_fix in zip(D4j_id,D4j_patch):
                # if code_line.strip() in D4j_fix.strip() or code_line.strip() == D4j_fix.strip():
                if code_line.strip() == D4j_fix.strip():
                    # print(file_data)
                    overlap_list.append(id)
                    overlap_result_list.append(str(['D4j_id: ' + id, ' CodeSearchNet_id: ' + file_name  + ' path:' + code_path]) + '\n')
                
                
    with open('overlap_result.txt', 'w') as f:  
        f.writelines(overlap_result_list)   
            
        
    print(len(overlap_list))
    
    overlap_list_set = list(set(overlap_list))
    print(overlap_list_set)
    
    with open('overlap_id.txt', 'w') as f:
        f.writelines(overlap_list_set)
    


def find_overlap():
    overlap_list = ['Cli_34', 'Jsoup_74', 'Lang_46', 'Time_27', 'Jsoup_86', 'Time_10', 'Cli_22', 'Cli_5', 'Time_15', 'Time_3', 'Lang_34', 'Time_12', 'Gson_4', 'Time_8', 'Cli_33', 'Time_9', 'Jsoup_60', 'Cli_29', 'Mockito_5', 'Jsoup_87', 'Closure_109']

    ppl_list = []
    
    
    print(sorted(overlap_list))

    for one in ppl_list:
        # print(one)
        if one in overlap_list:
            print(one)



read_CSN_data()
# find_overlap()



# 重叠的总数：26
# ['Cli_5', 'Time_12', 'Lang_34', 'Cli_34', 'Time_3', 
#  'Lang_46', 'Jsoup_60', 'Jsoup_87', 'Time_9', 'Time_8', 
#  'Time_27', 'Time_10', 'Jsoup_74', 'Time_15', 'Cli_33', 
#  'Cli_22', 'Closure_109', 'Mockito_5', 'Gson_4', 'Cli_29', 'Jsoup_86']