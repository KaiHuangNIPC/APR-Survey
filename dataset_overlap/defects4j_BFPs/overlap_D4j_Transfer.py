
import os
import re
import json
import pickle


def read_pkl_file(file_path):
    with open(file_path, 'rb') as f:
        file_lines = pickle.load(f)
    return file_lines

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

def save_overlap_data(D4j_id, CoCo_id, D4j_bug, D4j_fix, D4j_rem, D4j_add, CoCo_rem, CoCo_add, CoCo_ctx):
    with open ('/SS970evo/datasets/dataset_overlap/overlap_D4j_CoCoNut/overlap2006_info.txt', 'a') as f:
        overlap_info = ['D4j_id: '+D4j_id, 'CoCo_id: '+CoCo_id, 'D4j_bug: '+D4j_bug, 'D4j_fix: '+D4j_fix, 'D4j_rem: '+D4j_rem, 'D4j_add: '+D4j_add, 'CoCo_rem: '+CoCo_rem, 'CoCo_add: '+CoCo_add, 'CoCo_ctx: '+CoCo_ctx]
        f.write(str(overlap_info)+ '\n')

def check_overlop(CoCo_id, CoCo_bug_line, CoCo_rem, CoCo_add, CoCo_ctx, D4j_BFPs):
     
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
        
        
        if D4j_bug_hunk == 1:
            # print(D4j_rems, D4j_adds)
            # print(CoCo_rem, CoCo_add)
            
            # if D4j_bug.strip() in CoCo_bug_line and (CoCo_rem in D4j_rem and CoCo_add in D4j_add):
            # if (D4j_rem.strip() == CoCo_rem.strip() and D4j_add.strip() == CoCo_add.strip() and len(D4j_rem)+len(D4j_add)>10) or (D4j_rem.strip() == CoCo_add.strip() and D4j_add.strip() == CoCo_rem.strip() and len(D4j_rem)+len(D4j_add)>10):
            if D4j_adds[0].replace(' ','') == CoCo_add.replace(' ','') and D4j_rems[0].replace(' ','') == CoCo_rem.replace(' ','') and D4j_bugs[0].replace(' ','') in CoCo_ctx.replace(' ',''):
                # print('Overlap example: ' + D4j_id + ' ; ' + CoCo_id)
                # print('------'+D4j_rem+'+++++++')
                # print('------'+CoCo_rem+'+++++++')
                # print(D4j_fixs)
                save_overlap_data(D4j_id, CoCo_id, str(D4j_bugs), str(D4j_fixs), str(D4j_rems), str(D4j_adds), CoCo_rem, CoCo_add, CoCo_ctx)
                break
    return overlap_num        

def overlap_Transfer(root_path, D4j_BFPs, Transfer_ID):
    
    Transfer_data = read_pkl_file(root_path)
    print(len(Transfer_data))
    print(type(Transfer_data))
    for index in Transfer_data:
        print(index)
        print(len(Transfer_data[index]))
        
        for one_data in Transfer_data[index]:
            print(one_data)
            break
        
    return
    

    # Transfer_ID

    for CoCo_bug_loc, CoCo_fix_loc, CoCo_bug_line in zip(CoCoNut_bug_locs,CoCoNut_fix_locs,CoCoNut_bug_lines):
        CoCo_id += 1
        # if CoCo_id == 2: break
        if CoCo_id % 10000 == 0: 
            print(CoCo_id, CoCo_id/len(CoCoNut_bug_locs)*100)
        CoCo_bug_line = re.sub('\t', ' ', CoCo_bug_line)
        CoCo_bug_line = re.sub(' +', ' ', CoCo_bug_line)
        CoCo_bug_line = CoCo_bug_line.strip()
        CoCo_bug_loc = re.sub(' +', ' ', CoCo_bug_loc)
        CoCo_bug_loc = CoCo_bug_loc.strip()
        CoCo_fix_loc = re.sub(' +', ' ', CoCo_fix_loc)
        CoCo_fix_loc = CoCo_fix_loc.strip()
        
        CoCo_ctx = CoCo_bug_line
        CoCo_rem = CoCo_bug_loc
        CoCo_add = CoCo_fix_loc
        
        
        
        if CoCo_bug_loc == CoCo_fix_loc or CoCo_rem not in CoCo_ctx:
            bad_data_num += 1
            # with open('/SS970evo/datasets/dataset_overlap/overlap_D4j_CoCoNut/bad_dataset2010_info.txt', 'a') as bad_f:
            #     bad_f.write('CoCo_id: '+ str(CoCo_id) + '  ;  ' + 'CoCo_ctx: ' + CoCo_bug_line + '  ;  ' + 'CoCo_rem: ' + CoCo_rem + '  ;  ' + 'CoCo_add: ' + CoCo_add + '\n')
                
                
                
        else:
            check_overlop(str(CoCo_id), CoCo_bug_line, CoCo_rem, CoCo_add, CoCo_ctx, D4j_BFPs)
        
        
    print('all bad dataset example: ' + str(bad_data_num))
        
        
        
        
        
    return
    
    
    
    






if __name__ == '__main__':
    D4j_BFPs = read_jsonfile('defects4j_bfps.json')
    # print(D4j_BFPs)
    
    overlap_Transfer('/SS970evo/datasets/Transfer_dataset/dataset_pr.pkl', D4j_BFPs, Transfer_ID = 'dataset_pr.pkl')
   
    
    # all bad dataset example: 671497