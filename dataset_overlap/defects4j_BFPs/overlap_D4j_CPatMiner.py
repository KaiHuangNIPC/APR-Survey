
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

def save_overlap_data(D4j_id, BigFix_bugfile_path, BigFix_fixfile_path, D4j_bug, D4j_fix):
    with open ('/SS970evo/datasets/dataset_overlap/overlap_D4j_CPatMiner/overlap_code_info.txt', 'a') as f:
        overlap_info = [D4j_id, BigFix_bugfile_path, BigFix_fixfile_path, D4j_bug, D4j_fix]
        f.write(str(overlap_info)+ '\n')

def check_overlop(bug_file_path, fix_file_path, bug_file, fix_file, D4j_BFPs):
    BigFix_bugfile_path = bug_file_path
    BigFix_fixfile_path = fix_file_path
    BigFix_bug = bug_file 
    BigFix_fix = fix_file  
    overlap_num = 0
    
    for index in D4j_BFPs:
        BFP_list = D4j_BFPs[index]
        D4j_id = BFP_list[0]
        D4j_bugs = BFP_list[5]
        D4j_fixs = BFP_list[6]
        # print(D4j_id, len(D4j_bugs), len(D4j_fixs))
        
        
        for D4j_bug, D4j_fix in zip(D4j_bugs, D4j_fixs):
            # print(D4j_fix)
            
            if D4j_bug.replace(' ','') in BigFix_bug.replace(' ','') and D4j_fix.replace(' ','') in BigFix_fix.replace(' ',''):
                print('Overlap example: ' + D4j_id + ' ; ' + BigFix_bugfile_path.replace('/SS970evo/datasets/CPatMiner_dataset/',''))
                print('------'+D4j_fix+'+++++++')
                # print(D4j_fixs)
                save_overlap_data(D4j_id, BigFix_bugfile_path.replace('/SS970evo/datasets/CPatMiner_dataset/',''), BigFix_fixfile_path.replace('/SS970evo/datasets/CPatMiner_dataset/',''), D4j_bug, D4j_fix)
                break
    return overlap_num        

def overlap_code_CPatMiner(root_path, D4j_BFPs):
    # file_number: 1-44154
    for i in range(1, 44155):
        print(i)
        project_path = root_path + str(i)
        bugs_path = project_path + '/before'
        fixs_path = project_path + '/after'
        try:
            bug_files_name = os.listdir(bugs_path)
            fix_files_name = os.listdir(fixs_path)
        except:
            continue
        
        
        for bug_file_name, fix_file_name in zip(bug_files_name, fix_files_name):
            if '.java' in bug_file_name:
                bug_file_path = bugs_path + '/' + bug_file_name
                fix_file_path = fixs_path + '/' + fix_file_name
                # print(bug_file_path)
                # print(fix_file_path)
                
                bug_file = read_file(bug_file_path)
                fix_file = read_file(fix_file_path)
                
                bug_file = preprocess(bug_file)
                fix_file = preprocess(fix_file)
                # print(bug_file)
                # print(fix_file)
                # print('   ')
                
                
                check_overlop(bug_file_path, fix_file_path, bug_file, fix_file, D4j_BFPs)
        
        # if i == 500: break
 
def overlap_filename_CPatMiner(root_path, D4j_BFPs):
    # file_number: 1-44154
    for i in range(1, 44155):
        if i % 100 == 0:
            print(i)
        project_path = root_path + str(i)
        bugs_path = project_path + '/before'
        fixs_path = project_path + '/after'
        try:
            bug_files_name = os.listdir(bugs_path)
            fix_files_name = os.listdir(fixs_path)
        except:
            continue
        
        CPM_id = str(i)
        for bug_file_name, fix_file_name in zip(bug_files_name, fix_files_name):
            if '.java' in bug_file_name:
                CPM_bug_file_name = bug_file_name.replace('_','/')
                CPM_fix_file_name = fix_file_name.replace('_','/')
                
                
                for index in D4j_BFPs:
                    BFP_list = D4j_BFPs[index]
                    D4j_id = BFP_list[0]
                    D4j_bug_file_name = BFP_list[9]
                    D4j_fix_file_name = BFP_list[10]
                    # print(D4j_bug_file_name)
                    # print(D4j_fix_file_name)
                    
                    if CPM_bug_file_name in D4j_bug_file_name:
                        # print('Overlap ID: ' + CPM_id)
                        # print('overlap filename:' + CPM_bug_file_name + D4j_bug_file_name)
                        
                        with open('/SS970evo/datasets/dataset_overlap/overlap_D4j_CPatMiner/overlap_filename_info.txt', 'a') as f:
                            f.write('D4J ID: ' + D4j_id+' ; CPM ID: ' + CPM_id + ' ; Overlap CPM_file: ' + CPM_bug_file_name + ' ; Overlap D4j_file: ' + D4j_bug_file_name +'\n')
                        
                
                
                   





if __name__ == '__main__':
    D4j_BFPs = read_jsonfile('defects4j_bfps.json')
    # print(D4j_BFPs)
    
    overlap_code_CPatMiner('/SS970evo/datasets/CPatMiner_dataset/CPatMiner_/', D4j_BFPs)
    overlap_filename_CPatMiner('/SS970evo/datasets/CPatMiner_dataset/CPatMiner_/', D4j_BFPs)
    