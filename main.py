import requests, json
from flask import *

app=Flask(__name__)
app.secret_key="haVaiTuBahutAcchaHai"


def chk(text):
    url = "https://api.zerogpt.com/api/detect/detectText"

    headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
	 "accept": "application/json, text/plain, */*",
	 "connection": "keep-alive",
	 "sec-fetech-mode": "cors",
	 "sec-feteh-site": "same-site",
	 'sec-ch-ua-platform': '"Android"',
	 "content-type": "application/json",
	 "origin": "https://www.zerogpt.com",
	 "referer": "https://www.zerogpt.com/"}

    data = {
        "input_text": text
    }
    data=json.dumps(data)
    #{'success': True, 'data': {'sentences': [], 'isHuman': 0, 'additional_feedback': '', 'h': ['Artificial Intelligence (AI) is a rapidly growing field of computer science that focuses on creating intelligent machines.', 'These machines are capable of performing tasks that typically require human-like intelligence, such as perception, reasoning, learning, and decision-making.', 'AI technologies, including machine learning, natural language processing, and computer vision, are increasingly being used in various industries, including healthcare, finance, transportation, and manufacturing.', "With the continued advancements in AI research and development, experts believe that AI will play an increasingly critical role in shaping the future of society and help solve some of the world's most pressing problems.", 'As such, AI is poised to revolutionize the way we live and work, and its impact is only set to grow in the years to come.'], 'hi': [], 'textWords': 121, 'aiWords': 121, 'fakePercentage': 100.0, 'specialIndexes': [], 'specialSentences': [], 'input_text': ''}, 'code': 200, 'message': 'Detection complete'}

    try:
        response = requests.post(url, headers=headers, data=data).json()
        if response.get("success")==True:
            feedback=None if response["data"]["additional_feedback"]=='' else response["data"]["additional_feedback"]
            return jsonify(status=True, isHuman= response["data"]["isHuman"], aiSentences= response["data"]["h"], textWords=response["data"]["textWords"], aiWords= response["data"]["aiWords"], fakePercentage= response['data']["fakePercentage"], otherFeedback= feedback)
        else:
            return 
    except Exception as e:
        print(e)
        return jsonify(status= False, isHuman= None, sentences= None, textWords= None, aiWords= None, fakePercentage= None, otherFeedback= None)


@app.route("/")
def apiHome():
	return "<b>OK</b>"

@app.route("/api/detectText", methods=["POST", "GET"])
@app.route("/api/detectText/", methods=["POST", "GET"])
def apiMain():
	if request.method=="POST":
		if request.form.get("text"):
			text=request.form.get("text")
			if text in [None, '']:
				return '{"status": False, "isHuman": None, "sentences": None, "textWords": None, "aiWords": None, "fakePercentage": None, "otherFeedback": "Please input more text for a more accurate result."}'
			data=chk(text)
			return data
		else:
			return '{"status": False, "isHuman": None, "sentences": None, "textWords": None, "aiWords": None, "fakePercentage": None, "otherFeedback": "Please input more text for a more accurate result."}'
	else:
		return '{"status": False, "isHuman": None, "sentences": None, "textWords": None, "aiWords": None, "fakePercentage": None, "otherFeedback": "Please use POST method."}'




if __name__=="__main__":
	app.run(debug=True, host="0.0.0.0", threaded=True)
