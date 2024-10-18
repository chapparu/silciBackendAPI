import requests
from flask import Flask, jsonify
from config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

def trigger_jenkins_job():
    # Construct the Jenkins job URL
    job_url = f"{app.config['JENKINS_URL']}/job/{app.config['JENKINS_JOB_NAME']}/build"
    auth = (app.config['JENKINS_USER'], app.config['JENKINS_TOKEN'])

    # Trigger the job via Jenkins API
    response = requests.post(job_url, auth=(job_url, auth))

    if response.status_code == 201:
        return {"message": "Jenkins job triggered successfully."}
    else:
        return {"error": "Failed to trigger Jenkins job.", "status_code": response.status_code}


@app.route('/trigger-job', methods=['POST'])
def trigger_job():
    result = trigger_jenkins_job()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False)