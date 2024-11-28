import requests, random, uuid, string
try:
    import flask
    from flask import jsonify, Flask, request, render_template
    from flask import render_template as templ
except ModuleNotFoundError:
    os.system("pip install flask")


x=requests.get("https://raw.githubusercontent.com/DavidWittman/requests-random-user-agent/master/requests_random_user_agent/android_useragents.txt").text
open(".uaaa.txt",'a').write(x)

xxx=open(".uaaa.txt",'r').read().splitlines()
#server
app=Flask('app')
app.json.sort_keys = False
@app.route('/',methods=['GET','POST'])
def hello():
  return render_template('mrdh.html')
@app.route('/token',methods=['GET','POST'])
def api1():
    username=request.args.get("em")
    password=request.args.get("ps")
    global xxx
    ua=random.choice(xxx)
    fbvvv=random.randint(20000000,30000000)
    random_seed = random.Random()
    adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
    device_id = str(uuid.uuid4())
    secure = str(uuid.uuid4())
    family = str(uuid.uuid4())
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    xd =str(''.join(random_seed.choices(string.digits, k=20)))
    sim_serials = f'["{xd}"]'
    li = ['28','29','210']
    li2 = random.choice(li)
    j1 = ''.join(random.choice(string.digits) for _ in range(2))
    jazoest = li2+j1
    headers={
      'Authorization':f'OAuth {accessToken}',
      'X-FB-Friendly-Name':'authenticate',
      'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
      'X-FB-Net-HNI': str(random.randint(11111, 99999)),
      'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
      'User-Agent':"[FBAN/FB4A;FBAV/"+str(random.randrange(100,450))+".0.0."+str(random.randint(10,50))+"."+str(random.randint(80,150))+";FBBV/"+str(random.randint(10000000,99999999))+f";[FBAN/MessengerLite;FBAV/"+str(random.randrange(100,450))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/2"+str(random.randint(40000000,99999999))+";FBDM/{density=3.5,width=1440,height=2730};FBLC/en_US;FBRV/2539"+str(random.randint(40000,99999))+";FBCR/SMART;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/SM-G975F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
      'Accept-Encoding':'gzip, deflate',
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-FB-HTTP-Engine': 'Liger'
      }
    dat = {
      'adid': str(uuid.uuid4()),
      'format':'json',
      'device_id':device_id,
      'email':username,
      'password':password,
      'generate_analytics_claims':'1',
      'community_id':'',
      "sim_country": "id",
      'try_num':'1',
      'family_device_id':family,
      'sim_serials':sim_serials,
      'credentials_type':'password',
      'source':'login',
      'error_detail_type':'button_with_disabled',
      'logged_out_id': str(uuid.uuid4()),
      'generate_session_cookies':'1',
      'generate_machine_id':'1',
      'tier': 'regular',
      'reg_instance': str(uuid.uuid4()),
      'meta_inf_fbmeta':'',
      'currently_logged_in_userid':'0',
      'locale': 'en_GB',
      'client_country_code':'',
      'fb_api_req_friendly_name':'authenticate',
      'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
      }
    xs=requests.post("https://graph.facebook.com/auth/login",headers=headers,data=dat).json()
    if "access_token" in xs:
        ys=requests.get(f"https://api.facebook.com/method/auth.getSessionforApp?format=json&access_token={xs['access_token']}&new_app_id=275254692598279").json()
        if "access_token" not in ys:
            jsonn=jsonify(status=True,msg="SUCCESS",eaaaau_token=xs['access_token'],eaad6v7_token="Failed to fetch")
        else:
            jsonn=jsonify(status="True",message="Information Retrieved",data1=f"""EAAAAU TOKEN: {xs['access_token']}                                                                    COOKIE: {';'.join(x['name']+'='+x['value'] for x in xs['session_cookies'])}                                                  EAAD6V7 TOKEN: {str(ys['access_token']).replace("access_token","access_token_eaad6v7")}""")
    else:
        jsonn=jsonify({
            'message': "Invalid Login",
            'status': 'False',
            }
                      )
    return jsonn
@app.route('/ffs.php',methods=['GET','POST'])
def bard_ai():
    if request.method == 'GET':
        #token = 'EAAAAUaZA8jlABO1vRESDzlaPF11lzHlFJ2ZA1z0NmvG7XjZCugJ2PZAfjrjVZCt0OcS7zZBZA1wStDjYditOwFe0KMHmyhHNqcsFjeHuZAtSy7nDNnlH1kI0XfCaOYxvsToIZA9PlM7R3PZBIViJFMEyaxZBBmkxN7dP6sQQ4579BboZB5y56sQZBWg4CgZBcnkJikn9fAmZCnIPwFhUAZDZD'
        ques = request.args.get('uid')
        tok = request.args.get("token")
        site=requests.get(f"https://graph.facebook.com/{ques}?fields=name,subscribers.limit(0)&access_token={tok}").json()
        if 'name' in site:
          json1 = jsonify(names=site['name'],followers=site['subscribers']['summary']['total_count'])
        elif "The user is enrolled in a blocking, logged-in checkpoint" in str(site):
          json1=jsonify(Message="EXPIRED TOKEN / ACC CHECKPOINT")
        else:
          json1=jsonify(
            {
              "Message":"ERROR"
            }
            )
    return json1
__name__ = "drax"
print(__name__)
if __name__ == "drax":
    app.run(host='0.0.0.0', port=1112)
