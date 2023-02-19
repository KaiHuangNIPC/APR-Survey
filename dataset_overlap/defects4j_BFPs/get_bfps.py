# get bug-fix pairs (code piece)

import os
import re
import json





def remove_file(all_projects_path):
    new_projects_path = []
    for i in all_projects_path:
        if '.' not in i and 'lib' not in i:
            new_projects_path.append(i)
    return new_projects_path      

def remove_test(project_patch_path):
    new_projects_path = []
    for i in project_patch_path:
        if 'test.patch' not in i:
            new_projects_path.append(i)
    return new_projects_path 

def read_file(patch):
    file_lines = ''
    with open (patch, 'r', errors='ignore') as f:
        file_lines = f.readlines()
    return file_lines

def split_bug_fix(patch_file):
    bug, fix = [], []
    rem, add = [], []
    bug_file_name, fix_file_name = '', ''
    patch_lines = patch_file[2:]
    # print(patch_lines)
    bug_one, fix_one = '', ''
    rem_one, add_one = '', ''
    for line in patch_lines:
        # print('---', line)
        if '@@' in line[:2]:
            bug_one = re.sub(' +', ' ', bug_one)
            fix_one = re.sub(' +', ' ', fix_one)
            rem_one = re.sub(' +', ' ', rem_one)
            add_one = re.sub(' +', ' ', add_one)
            bug.append(bug_one[:-1])
            fix.append(fix_one[:-1])
            rem.append(rem_one[:-1])
            add.append(add_one[:-1])
            bug_one, fix_one = '', ''
            rem_one, add_one = '', ''
        elif '---' in line[:3] or '+++' in line[:3] or 'diff' in line[:4] or 'index' in line[:5]:
            if '---' in line[:3]:
                bug_file_name = line[4:]
            if '+++' in line[:3]:
                fix_file_name = line[4:]
        # 注意：由于Defects4j中将bug和fix标记反了，正确的应该是将bug和fix调换过来，因此-对应fix，+对应bug 
        elif '+' in line[:1]:  
            bug_one = bug_one + line[1:].strip() + ' '
            rem_one = rem_one + line[1:].strip() + ' '
        elif '-' in line[:1]:
            fix_one = fix_one + line[1:].strip() + ' '
            add_one = add_one + line[1:].strip() + ' '
        else:
            bug_one = bug_one + line[1:].strip() + ' '
            fix_one = fix_one + line[1:].strip() + ' '
        # print(bug_one)
    bug_one = re.sub(' +', ' ', bug_one)
    fix_one = re.sub(' +', ' ', fix_one)
    bug.append(bug_one[0:-1])
    fix.append(fix_one[0:-1])
    
    rem_one = re.sub(' +', ' ', rem_one)
    add_one = re.sub(' +', ' ', add_one)
    rem.append(rem_one[0:-1])
    add.append(add_one[0:-1])
    
    bug = bug[1:]
    fix = fix[1:]
    new_bug = []
    new_fix = []
    for b in bug:
        if b != '' and len(set(b)) > 2:
            new_bug.append(b)
    for f in fix:
        if f != '' and len(set(f)) > 2:
            new_fix.append(f)
            
    rem = rem[1:]
    add = add[1:]
    

    return new_bug, new_fix, rem, add, bug_file_name.strip(), fix_file_name.strip()

def save_file(content, file_path):
    with open (file_path, 'w') as f:
        f.writelines(content)

def find_bfps(all_projects_patche_path):
    BFPs = {}
    BFPs_list = []
    for project_path in all_projects_patche_path:
        # print(project_path)
        project_patch_path = os.listdir(project_path)
        project_patch_path = remove_test(project_patch_path)
        project_patch_path = [project_path+'/'+i for i in project_patch_path]
        
        
        project_name = project_path.split('/')[-2]
        print(project_name)
        
        # read all patch files
        patch_index = {}
        for project_patch in project_patch_path:
            patch_number = int((project_patch.split('/')[-1]).split('.')[-3])
            # patch_index.append([patch_number, project_patch])
            patch_index[patch_number] = project_patch
        patch_index = sorted(patch_index.items(), key=lambda item:item[0])
        # print(patch_index)
        for index2patch in patch_index:
            index = index2patch[0]
            patch = index2patch[1]
            print(index, patch)
            patch_file = read_file(patch)
            bug, fix, rem, add, bug_file_name, fix_file_name = split_bug_fix(patch_file)
            
            bug_fix_pair = [project_name+'-'+str(index), len(bug), len(fix), len(rem), len(add), bug, fix, rem, add, bug_file_name, fix_file_name]
            BFPs[project_name+'-'+str(index)] = bug_fix_pair
            # print(bug_fix_pair)
            BFPs_list.append(str(bug_fix_pair)+'\n')
              
    return BFPs, BFPs_list

if __name__ == '__main__':
    defects4j_path = '/SS970evo/datasets/defects4j-master/framework/projects/'
    all_projects_path = os.listdir(defects4j_path)
    all_projects_path = remove_file(all_projects_path)
    print(len(all_projects_path))
    print(all_projects_path)
    all_projects_patche_path = [defects4j_path+i+'/patches' for i in all_projects_path]
    
    BFPs, BFPs_list = find_bfps(all_projects_patche_path)
    
    save_file(BFPs_list, 'defects4j_bfps.txt')
    
    
    BFPs = json.dumps(BFPs)
    f2 = open('defects4j_bfps.json', 'w')
    f2.write(BFPs)
    f2.close()
    
    
    



