
import os
import re
import json
import lzma


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
            
            if D4j_bug.strip() in BigFix_bug and D4j_fix in BigFix_fix:
                print('Overlap example: ' + D4j_id + ' ; ' + BigFix_bugfile_path.replace('/SS970evo/datasets/CPatMiner_dataset/',''))
                print('------'+D4j_fix+'+++++++')
                # print(D4j_fixs)
                save_overlap_data(D4j_id, BigFix_bugfile_path, BigFix_fixfile_path, D4j_bug, D4j_fix)
                break
    return overlap_num        

def overlap_code_MegaDiff(root_path, D4j_BFPs):
    # file_number: 1-41
    for i in range(1, 41):
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
 
def overlap_filename_MegaDiff(root_path, D4j_BFPs):
    # file_number: 1-40
    for i in range(10, 41):

        print(i)
        project_path = root_path + str(i)
        try:
            diff_files_name = os.listdir(project_path)
        except:
            continue
        
        print(len(diff_files_name))
        
        
        
        
        for index,diff_file_name in enumerate(diff_files_name):
            if index % 1000 == 0:
                print(index, len(diff_files_name))
            # if index == 10: break
            with lzma.open(project_path+'/'+diff_file_name, 'r') as f:
                diff_file = f.readlines()
            # print(diff_file)
            
            Mega_file_name = str(diff_file[2][6:-1])[1:]
            # print(Mega_file_name)
            
            
            
            Mega_id = str(i) + '/' + diff_file_name
                
                
            for index in D4j_BFPs:
                BFP_list = D4j_BFPs[index]
                D4j_id = BFP_list[0]
                D4j_bug_file_name = BFP_list[9]
                D4j_fix_file_name = BFP_list[10]
                # print(D4j_bug_file_name)
                # print(Mega_file_name[1:-1])
                # print(D4j_bug_file_name[2:])
                # return
                    
                if Mega_file_name[1:-1] == D4j_bug_file_name[2:]:
                        # print('Overlap ID: ' + CPM_id)
                        # print('overlap filename:' + CPM_bug_file_name + D4j_bug_file_name)
                        
                    with open('/SS970evo/datasets/dataset_overlap/overlap_D4j_MegaDiff/overlap_filename_info.txt', 'a') as f:
                        f.write('D4J ID:' + D4j_id+'; Mega ID:' + Mega_id +'; Overlap File:' + Mega_file_name[1:-1] + '\n')
                        
                
                
                   





if __name__ == '__main__':
    D4j_BFPs = read_jsonfile('defects4j_bfps.json')
    # print(D4j_BFPs)
    
    
    overlap_filename_MegaDiff('/SS970evo/datasets/MegaDiff_dataset/megadiff-master/', D4j_BFPs)
    