import spacy 
import numpy as np
import modules.convert_csv  as conv
import math
nlp  = spacy.load('ja_ginza')


def text_vector(text):
    doc = nlp(text)
    #for token in doc:  # Token単位で処理結果を参照。
    #    print(token.i, token.lemma_, token.pos_)

    vec = doc.vector
    
    return vec

def cos_sim(v1,v2):
    ret = np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    if math.isnan(ret):
        return 0
    else:
        return ret

def cos_distance(text1):
    vec1 = text_vector(text1)
    path = './modules/text/records.txt'
    with open(path, mode='a') as f:
        f.write(text1+"\n")
    qa_vec, qa_qes, qa_lists, sources = zip(*conv.load_csv())
    angles = []
    for vec2 in qa_vec:
        angles.append(cos_sim(vec1,vec2))
    ret_ans=[]
    source=[]
    for i in range(4):
        idx = np.asarray(angles).argmax()
        angles[idx] = 0;
        if cos_sim(vec1,qa_vec[idx]) < 0.65 and i == 0:
            ret_ans.append("すみません、よくわかりません")
            source.append("")
            ret_ans.append("該当なし")
            source.append("")
            ret_ans.append("該当なし")
            source.append("")
            ret_ans.append("該当なし")
            source.append("")
            break;
        elif cos_sim(vec1,qa_vec[idx]) < 0.55:
            ret_ans.append("該当なし")
            source.append("")
        else:   
            ret_ans.append(qa_qes[idx] + "は" + qa_lists[idx] + " です。")
            source.append("ソースは " + sources[idx] + " です。")
    
    return ret_ans, source


    
    
if __name__ == "__main__":
    text1 = "夏休みはいつですか"
    text2 = "春休みはいつですか"
    
    #print(cos_distance(text1,text2))
    
