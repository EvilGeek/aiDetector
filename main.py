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
    try:
        response = requests.post(url, headers=headers, data=data).json()
        if response.get("success"):
            feedback = response["data"]["additional_feedback"] or None
            return jsonify(
                status=True,
                isHuman=response["data"]["isHuman"],
                aiSentences=response["data"]["h"],
                textWords=response["data"]["textWords"],
                aiWords=response["data"]["aiWords"],
                fakePercentage=response['data']["fakePercentage"],
                otherFeedback=feedback
            )
        return jsonify(
            status=False,
            isHuman=None,
            sentences=None,
            textWords=None,
            aiWords=None,
            fakePercentage=None,
            otherFeedback="Something went wrong."
        )
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return jsonify(
            status=False,
            isHuman=None,
            sentences=None,
            textWords=None,
            aiWords=None,
            fakePercentage=None,
            otherFeedback=error_message
        )

@app.route("/")
def apiHome():
	return "<b>OK</b>"

@app.route("/api/detectText", methods=["POST", "GET"])
@app.route("/api/detectText/", methods=["POST", "GET"])
def apiMain():
	if request.method=="POST":
		if request.form.get("text") or request.get_json().get("text"):
			text=request.form.get("text") if request.form.get("text") else request.get_json().get("text")
			if text in [None, '']:
				return jsonify(status= False, isHuman= None, sentences= None, textWords= None, aiWords= None, fakePercentage= None, otherFeedback= "Please input more text for a more accurate result.")
			data=chk(text)
			return data
		else:
			return jsonify(status= False, isHuman= None, sentences= None, textWords= None, aiWords= None, fakePercentage= None, otherFeedback= "Please input more text for a more accurate result.")
	else:
		return jsonify(status= False, isHuman= None, sentences= None, textWords= None, aiWords= None, fakePercentage= None, otherFeedback= "Please use POST method.")




if __name__=="__main__":
	app.run(debug=True, host="0.0.0.0", threaded=True)
