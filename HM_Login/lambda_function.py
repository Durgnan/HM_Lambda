import json
import pymysql.cursors

def lambda_handler(event, context):
    # TODO implement
    MODE = event['MODE']
    if MODE == 'LOGIN':
        username = event['username']
        password = event['password']
        connection = pymysql.connect(host='homeomitra.can55fak5hyt.ap-south-1.rds.amazonaws.com',user='DBA_RAVI',password='SAGGIT360626',db='HOMEOMITRA',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        
        
        
        try:
    
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT COUNT(*) CC FROM `LOGIN_CREDS`  WHERE (EMAIL = %s OR PHONE = %s) AND (PASSWORD = %s)"
                cursor.execute(sql, (username,username, password))
                if cursor.rowcount == 1:
    
                    result = cursor.fetchone()
                    temp = result.values()
                    if result['CC'] == 1:
                        St = 'SUCCESS'
                        return {'statusCode':200,'message':St}
                    else:
                        St = 'INCORRECT CREDENTIALS'
                        return {'statusCode':404,'message':St}
                else:
                    St = 'FAILED'
                    return {'statusCode':404,'message':St}
        finally:
            connection.close()
    elif MODE == 'SIGNUP':
        email = event['email']
        fname = event['fname']
        lname = event['lname']
        password = event['password']
        phone   = event['phone']
        tpe = event['type']
        connection = pymysql.connect(host='homeomitra.can55fak5hyt.ap-south-1.rds.amazonaws.com',user='DBA_RAVI',password='SAGGIT360626',db='HOMEOMITRA',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        if tpe == 'PATIENT' or tpe == 'PHARMACY':
            area = event['area']
            address = event['address']
            landmark = event['landmark']
            pincode = event['pincode']
            city = event['city']
            try:
                with connection.cursor() as cursor:
                # Read a single record
                    sql = "INSERT INTO LOGIN_CREDS(EMAIL,PASSWORD,USER_CLASS,PHONE) VALUES(%s,%s,%s,%s)"
                    cursor.execute(sql, (email,password,tpe,phone))
                    sql = "INSERT INTO USER_INFORMATION(EMAIL,FIRST_NAME,LAST_NAME) VALUES(%s,%s,%s)"
                    cursor.execute(sql, (email,fname,lname))
                    sql = "INSERT INTO "+tpe+"_ADDITIONAL_INFORMATION(EMAIL,AREA,ADDRESS,LANDMARK,PINCODE,CITY) VALUES(%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (email,area,address,landmark,pincode,city))
                    connection.commit()
                    return {'statusCode':200,'message':'SUCCESS'}
                    connection.close()
                    
            except Exception:
                return {'statusCode':404,'message':'FAILED'} 
            
            
        elif tpe == 'DOCTOR':
            location = event['location']
            degree = event['degree']
            specialization = event['specialization']
            dayOpen = event['dopen'].split(',')
            dayOpen = '_'.join(dayOpen)
            timings = event['timings'].split(',')
            timings = '_'.join(timings)
            picurl = ''
            try:
                with connection.cursor() as cursor:
                # Read a single record
                    sql = "INSERT INTO LOGIN_CREDS(EMAIL,PASSWORD,USER_CLASS,PHONE) VALUES(%s,%s,%s,%s)"
                    cursor.execute(sql, (email,password,tpe,phone))
                    sql = "INSERT INTO USER_INFORMATION(EMAIL,FIRST_NAME,LAST_NAME) VALUES(%s,%s,%s)"
                    cursor.execute(sql, (email,fname,lname))
                    sql = "INSERT INTO DOCTOR_ADDITIONAL_INFORMATION(EMAIL,LOCATION,DEGREE,SPECIALIZATION,DAYS_OF_SERVICE_SEPERATED_BY_UNDERSCORES,TIMINGS_SLOTS_SEPERATED_BY_COLON_FURTHUR_SEPERATED_BY_COMMA,PICURL) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (email,location,degree,specialization,dayOpen,timings,picurl))
                    connection.commit()
                    return {'statusCode':200,'message':'SUCCESS'} 
                    connection.close()
            except Exception:
                return {'statusCode':404,'message':'FAILED'}
            
            
            
            
            
