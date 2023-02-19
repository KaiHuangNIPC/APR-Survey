
import os
import re
import json


def read_file(file_path):
    with open(file_path, 'r') as f:
        file_lines = f.readlines()
    return file_lines

def read_jsonfile(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    json_content = json.loads(content)
    
    return json_content
    
def preprocess(file_lines):
    
    file_str = ''
    for line in file_lines:
        file_str = file_str + line.strip() + ' '
    file_str = re.sub(' +', ' ', file_str)
    
    return file_str.strip()

def save_overlap_data(D4j_id, CodRep_id, D4j_bug, D4j_fix):
    with open ('/SS970evo/datasets/dataset_overlap/overlap_D4j_CodRep/overlap_code_info.txt', 'a') as f:
        overlap_info = ['D4j_id: '+D4j_id, 'CodRep_id: '+CodRep_id, 'D4j_bug: '+D4j_bug, 'D4j_fix: '+D4j_fix]
        f.write(str(overlap_info)+ '\n')

def check_overlop(CodRep_id, bug_file, D4j_BFPs):
     
    overlap_num = 0
    
    for index in D4j_BFPs:
        BFP_list = D4j_BFPs[index]
        D4j_id = BFP_list[0]
        D4j_bug_hunk = BFP_list[1]
        D4j_bugs = BFP_list[5]
        D4j_fixs = BFP_list[6]
        D4j_rems= BFP_list[7]
        D4j_adds = BFP_list[8]
        # print(D4j_id, len(D4j_bugs), len(D4j_fixs))
        
                
        
        
        for D4j_bug, D4j_fix, D4j_rem, D4j_add in zip(D4j_bugs, D4j_fixs, D4j_rems, D4j_adds):
            # print(D4j_fix)
            
            if D4j_fix.strip() in bug_file and len(D4j_fix)>5:
                save_overlap_data(D4j_id, CodRep_id, D4j_bug.strip(), D4j_fix.strip())
                break
    return overlap_num        

def overlap_CodRep(root_path, D4j_BFPs, max_file_number):
    # file_number: 1:3858 2:10088 3:15326 4:10431 5:18366
    for i in range(1, max_file_number+1):
        if i%1000 == 0: print(i)
        CodRep_id = root_path.split('/')[-3]+'-'+str(i)
        
        try:
            CodRep_file_path = root_path + str(i) + '.txt'
        except:
            continue
        
        bug_file = read_file(CodRep_file_path)
        bug_file = preprocess(bug_file)
        check_overlop(CodRep_id, bug_file, D4j_BFPs)
        





if __name__ == '__main__':
    D4j_BFPs = read_jsonfile('defects4j_bfps.json')
    # print(D4j_BFPs)
    
     # file_number: 1:3858 2:10088 3:15326 4:10431 5:18366
    overlap_CodRep('/SS970evo/datasets/CodRep/CodRep-competition-master/Datasets/Dataset1/Tasks/', D4j_BFPs, 3858)
    overlap_CodRep('/SS970evo/datasets/CodRep/CodRep-competition-master/Datasets/Dataset2/Tasks/', D4j_BFPs, 10088)
    overlap_CodRep('/SS970evo/datasets/CodRep/CodRep-competition-master/Datasets/Dataset3/Tasks/', D4j_BFPs, 15326)
    overlap_CodRep('/SS970evo/datasets/CodRep/CodRep-competition-master/Datasets/Dataset4/Tasks/', D4j_BFPs, 10431)
    overlap_CodRep('/SS970evo/datasets/CodRep/CodRep-competition-master/Datasets/Dataset5/Tasks/', D4j_BFPs, 18366)
    
    