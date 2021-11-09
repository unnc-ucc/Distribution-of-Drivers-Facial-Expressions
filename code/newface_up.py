import cv2,random,os,re,time
import mediapipe as mp

def self_cont(x_list):
    new,cp = [],[]
    try:
        for i in range(6):
            for j in range(2):
                p = random.randint(1,5)
                c = x_list[i][j]*p
                if c >=1000:
                    new.append(c/100)
                else:
                    new.append(c/10)
        cp = new[6:]
    except TypeError:
        for i in range(6):
            cp.append(0)
    return cp

def action(input_image):
    min_xy = []
    mpDraw = mp.solutions.drawing_utils
    mpFaceMesh = mp.solutions.face_mesh
    faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
    drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=2)
    img = cv2.imread(input_image)
    img = cv2.resize(img,(400, 400),interpolation=cv2.INTER_AREA,)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = faceMesh.process(imgRGB)
    if result.multi_face_landmarks:
        for faceLms in result.multi_face_landmarks:
            mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACE_CONNECTIONS,
                drawSpec,drawSpec)
            for id,lm in enumerate(faceLms.landmark):
                ih,iw,ic = img.shape
                cx,cy = int(lm.x*iw),int(lm.y*ih)
                min_xy.append([cx,cy])
        return min_xy
        
def prc_file(input_txt,output_txt):
    line = []
    min_xy = []
    c = os.getcwd()
    train = c + "\\train\\"
    test = c + "\\test\\"
    val = c + "\\val\\"
    with open(input_txt,'r',encoding="utf-8") as fs:
        line = fs.readlines()
    fs.close()
    for ix in line:
        result,first = [],[]
        
        test_dir = test + ix
        new_test_dir = test_dir.replace("\n","")

        if os.path.exists(new_test_dir):
            test_min_xy = action(new_test_dir)
            print(new_test_dir)
            test_data = self_cont(test_min_xy)
            for cx in test_data:
                p = str(cx) + "%" + " "
                first.append(p)
            oks = str(round(sum(test_data)/6,4))
            #first.append("=" + oks)
            result.append(ix.replace("\n","") + " " + ''.join(first))
            with open(output_txt,'a+',encoding="utf-8") as fs:
                for line in result:
                    fs.writelines(line+"\n")
            fs.close()
            result.clear()
            first.clear()
            
        train_dir = train + ix
        new_train_dir = train_dir.replace("\n","")
        
        if os.path.exists(new_train_dir):
            train_min_xy = action(new_train_dir)
            print(new_train_dir)
            train_data = self_cont(train_min_xy)
            for cx in train_data:
                p = str(cx) + "%" + " "
                first.append(p)
            ok = str(round(sum(train_data)/6,4))
            #first.append("=" + ok)
            result.append(ix.replace("\n","") + " " + ''.join(first))
            with open(output_txt,'a+',encoding="utf-8") as fs:
                for line in result:
                    fs.writelines(line+"\n")
            fs.close()
            result.clear()
            first.clear()
        
        val_dir = val + ix
        new_val_dir = val_dir.replace("\n","")
        
        if os.path.exists(new_val_dir):
            val_min_xy = action(new_val_dir)
            print(new_val_dir)
            val_data = self_cont(val_min_xy)
            for cx in val_data:
                p = str(cx) + "%" + " "
                first.append(p)
            oka = str(round(sum(val_data)/6,4))
            #first.append("=" + oka)
            result.append(ix.replace("\n","") + " " + ''.join(first))
            with open(output_txt,'a+',encoding="utf-8") as fs:
                for line in result:
                    fs.writelines(line+"\n")
            fs.close()
            result.clear()
            first.clear()
            
if __name__ == '__main__':
    prc_file(input_txt='1.txt',output_txt='new1.txt')
