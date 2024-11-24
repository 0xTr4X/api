from flask import Flask,render_template, request, jsonify
import requests, random, re
from random import randint as ri
from requests import get, post

app = Flask('app')
@app.route('/reaction',methods=['GET','POST'])
def bard_ai():
  if request.method == 'GET':
      tok=request.args.get('token')
      link=request.args.get('post')
      try:
          fbid=re.search("s/(.*)",link).group().split("/")[1]
          uid=re.search("m/(.*)",link).group().split("/")[1]
      except:
          return jsonify(status=False,error_msg="Invalid URL")
      react=request.args.get('react')
      check=requests.get("https://graph.facebook.com/me/?access_token="+tok).json()
      if 'id' in check:
          headers={
                'Content-Type': 'application/json',
                #'Authorization': 'Bearer %s'%(token),
                #'user-agent': random.choice(ua),
                'user-agent': '[FBAN/FB4A;FBAV/%s.0.0.%s.%s;FBBV/21954989;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F926W;FBSV/8;FBCA/armeabi-v7a:armeabi;]'%(ri(300,445),ri(10,20),ri(100,120))
                }
          data={
                  "type": react,
                  "access_token": tok
                  }
          resp=requests.post("https://graph.facebook.com/{}_{}/reactions".format(uid,fbid),headers=headers,data=data).json()
          if 'success' in resp:
              return jsonify(status=True,message="REACT SUCCESS",link=link,reaction_type=react)
          else:
              return jsonify(link=link,status="False",error_msg="REACT ERROR",reaction_type=react)
      else:
          return jsonify(status=False,error_msg="ACCESS TOKEN EXPIRED")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
  t=Thread(target=run)
  t.start()
keep_alive()
