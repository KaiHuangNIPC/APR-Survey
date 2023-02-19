import lzma
import shutil
import json
import os

def overlap_set():
    with open('overlap_result.txt') as f:
        overlap_lines = f.readlines()
    print(len(overlap_lines))

    D4j_ID_list = []
    Mega_ID_list = []
    overlap_file_list = []

    for i in overlap_lines:
        i_list = i.split(', ')
        D4j_ID = i_list[0].split(': ')[1][:-1]
        Mega_ID = i_list[1].split(': ')[1][:-1]
        overlap_file = Mega_ID + '.txt'
        # print(overlap_file)
        # print(D4j_ID, Mega_ID, overlap_file)
        
        D4j_ID_list.append(D4j_ID)
        Mega_ID_list.append(Mega_ID)
        overlap_file_list.append(overlap_file)
        
    D4j_ID_list = sorted(set(D4j_ID_list))
    Mega_ID_list = sorted(list(set(Mega_ID_list)))
    overlap_file_list = list(set(overlap_file))



    print(D4j_ID_list)
    print('All Overlap D4j_ID: '+ str(len(D4j_ID_list)))
    print('All Overlap CodRep_ID: '+ str(len(Mega_ID_list)))
    print('All Overlap file: ' + str(len(overlap_file_list)))

def read_jsonfile(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    json_content = json.loads(content)
    
    return json_content
  

def overlap_result(input_line):
    with open('overlap_code_info.txt', 'r') as f2:
        log_file_lines = f2.readlines()

    log_file_line = log_file_lines[input_line-1]
    D4j_project = log_file_line.split(', ')[0]
    D4j_project = D4j_project.split(': ')[1][:-1]
    print(D4j_project)


    D4j_file = '/SS970evo/datasets/defects4j-master/framework/projects/' + D4j_project.split('-')[0] + '/patches/' + D4j_project.split('-')[1] + '.src.patch'
    print(D4j_file)

    with open(D4j_file, 'r') as D4j_f:
        D4j_lines = D4j_f.readlines()

        
    # print(D4j_lines)
    CRP_ID = log_file_line.split(', ')[1].split(': ')[-1]
    Dataset_num = CRP_ID.split('-')[0]
    File_num = CRP_ID.split('-')[1][:-1]
    
    overlap_file = '/SS970evo/datasets/CodRep/CodRep-competition-master/Datasets/'+Dataset_num+'/Tasks/'+File_num+'.txt'
    

    with open(overlap_file, 'r') as f:
        overlap_lines = f.readlines()

    overlap_lines = str(overlap_lines)
        
    # print(D4j_lines)
    # print(overlap_lines)
    
    D4j_BFPs = read_jsonfile('/SS970evo/datasets/dataset_overlap/defects4j_BFPs/defects4j_bfps.json')
    BFP_list = D4j_BFPs[D4j_project]
    D4j_id = BFP_list[0]
    D4j_bugs = BFP_list[5]
    D4j_fixs = BFP_list[6]
    D4j_rems = BFP_list[7]
    D4j_adds = BFP_list[8]
    # print(D4j_bugs)
    # print(D4j_fixs)
    
    fix_action = 0
    for add in D4j_adds:
        # print(add)
        if add in overlap_lines and len(add) > 4:
            print(log_file_line+'存在数据重叠，Mega中出现了D4j的修复行为')
            with open('overlap_result.txt', 'a') as result_f:
                if log_file_line[0] == '-' or log_file_line[0] == '+':
                    result_f.writelines(log_file_line[1:])
                else:
                    result_f.writelines(log_file_line)
            break
            

if __name__ == '__main__':
    
    
    for i in range(1, 304):
        input_line = i
        overlap_result(input_line)
    
    overlap_set()