import pymysql as my
import numpy as np
import cv2
def login_db():
    conn = my.connect(host='127.0.0.1',
                user='root',
                password='1234',      
                db='pythondb',
                charset='utf8',
                cursorclass=my.cursors.DictCursor)
    return(conn)

def create_db(conn):
    rows = None   
    try:
        with conn.cursor() as cursor :  
            sql = '''
                CREATE TABLE `test_fol` 
                (`name` VARCHAR(141) NOT NULL,
                `similarity` VARCHAR(141) NOT NULL,
            PRIMARY KEY (`name`, `similarity`)
                )
                COLLATE='utf8mb4_general_ci'
                ENGINE=InnoDB;
                '''

            cursor.execute(sql)  
            conn.commit()
            conn.close()
        
    except Exception as e:
        print(e)
    # else
    finally:
        return rows

def insert_db(conn,name,similarity,img,):
        result = None    
        try:
            with conn.cursor() as cursor :  
                sql = '''
                    insert into
                        test_fol (name,similarity,img)
                    values (%s,%s,%s);              
                    '''                   
                cursor.execute(sql,(name,similarity,img)) 
            conn.commit()
            result = conn.affected_rows()
            
        except Exception as e:
            result = None
            
        return result

def select_img(conn,id):
       
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                where id = %s;              
                '''                   
            cursor.execute(sql,(id)) 
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(res,name,similarity)

def select_last(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)

def select_last2(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 2,1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)

def select_last3(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 4,1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)

def select_last4(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 6,1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)
#################################################
def select_last5(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 8,1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)
def select_last6(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 10,1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)
def select_last7(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 12,1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)
def select_last8(conn):
        with conn.cursor() as cursor :  
            sql = '''
                select name,similarity,img
                    from test_fol
                ORDER BY id DESC limit 14,1;              
                '''                   
            cursor.execute(sql)
            conn.commit()
            
        row = cursor.fetchone()
        nparr = np.fromstring(row['img'],np.uint8)

        tmp = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
        ret, jpg = cv2.imencode('.jpg',tmp)
        res = jpg.tobytes()

        name = row['name']
        similarity = row['similarity']
        return(name,similarity,res)


#create_db()

#print(select_img(conn,2)[0])