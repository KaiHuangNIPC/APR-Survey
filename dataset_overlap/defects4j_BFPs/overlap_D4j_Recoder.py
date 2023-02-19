
import os
import re
import json
import pickle


def read_pkl_file(file_path):
    with open(file_path, 'rb') as f:
        file_lines = pickle.load(f)
    return file_lines

def read_jsonfile(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    json_content = json.loads(content)
    
    return json_content
    
def preprocess(file_lines):
    
    file_str = ''
    for line in file_lines.split('\n'):
        file_str = file_str + line.strip() + ' '
    file_str = re.sub(' +', ' ', file_str)
    
    return file_str.strip()

def save_overlap_data(D4j_id, Recoder_id, D4j_rems, D4j_adds, D4j_bugs, D4j_fixs, Recoder_bug_pro, Recoder_fix_pro):
    with open ('/SS970evo/datasets/dataset_overlap/overlap_D4j_Recoder/overlap_code_info.txt', 'a') as f:
        overlap_info = ['D4j_id: '+D4j_id, 'Recoder_id: '+Recoder_id, 'D4j_rem: '+(D4j_rems), 'D4j_add: '+D4j_adds, 'D4j_bug: '+D4j_bugs, 'D4j_fix: '+D4j_fixs, 'Recoder_bug: '+Recoder_bug_pro, 'Recoder_fix: '+Recoder_fix_pro]
        f.write(str(overlap_info)+ '\n')

def check_overlop(Recoder_id, Recoder_bug_pro, Recoder_fix_pro, D4j_BFPs):
     
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
            # if D4j_bugs[0] in Recoder_bug_pro and D4j_fixs[0] in Recoder_fix_pro:
            if D4j_bugs[0].replace(' ','') in Recoder_bug_pro.replace(' ','') and D4j_fixs[0].replace(' ','') in Recoder_fix_pro.replace(' ',''):
            # if D4j_rems[0] in Recoder_bug_pro and D4j_adds[0] in Recoder_fix_pro and len(D4j_rems[0])>15 and len(D4j_adds[0])>15:

                save_overlap_data(D4j_id, Recoder_id, str(D4j_rems), str(D4j_adds), str(D4j_bugs), str(D4j_fixs), Recoder_bug_pro, Recoder_fix_pro)
        else:
            overlap_result = 'no'
            for D4j_bug, D4j_fix in zip(D4j_bugs, D4j_fixs):
                if D4j_bug.replace(' ','') in Recoder_bug_pro.replace(' ','') and D4j_fix.replace(' ','') in Recoder_fix_pro.replace(' ',''):
                    overlap_result = 'yes'
                else:
                    overlap_result = 'no'
                    break
            if overlap_result == 'yes':
                save_overlap_data(D4j_id, Recoder_id, str(D4j_rems), str(D4j_adds), str(D4j_bugs), str(D4j_fixs), Recoder_bug_pro, Recoder_fix_pro)
                   
        
                
    return overlap_num        

def overlap_Recoder(root_path, D4j_BFPs, Recoder_ID):
    
    Recoder_datas = read_pkl_file(root_path)
    # print(len(Recoder_datas))
    # print(type(Recoder_datas))
    # print(Recoder_datas[1])
    # print(Recoder_datas[1]['old'])
    # print(Recoder_datas[1]['new'])
    # return
    
    for index, Recoder_line in enumerate(Recoder_datas):
        Recoder_bug_raw = Recoder_line['old']
        Recoder_fix_raw = Recoder_line['new']
        Recoder_id = Recoder_ID + '/' + str(index)
        # print(Recoder_bug_raw)
        # print(Recoder_fix_raw)
        
        Recoder_bug_pro = preprocess(Recoder_bug_raw)
        Recoder_fix_pro = preprocess(Recoder_fix_raw)
        # print(Recoder_bug_pro)
        # print(Recoder_fix_pro)
        
            
        if index % 100 == 0: print(Recoder_id)
        check_overlop(Recoder_id, Recoder_bug_pro, Recoder_fix_pro, D4j_BFPs)
        
        
        
        
        
        
        
    
    
    
    
    






if __name__ == '__main__':
    D4j_BFPs = read_jsonfile('defects4j_bfps.json')
    # print(D4j_BFPs)
    
    overlap_Recoder('/SS970evo/datasets/Recoder_dataset/data0.pkl', D4j_BFPs, Recoder_ID = 'data0.pkl')
    overlap_Recoder('/SS970evo/datasets/Recoder_dataset/data1.pkl', D4j_BFPs, Recoder_ID = 'data1.pkl')


    
    # all bad dataset example: 671497