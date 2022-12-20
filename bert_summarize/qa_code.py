import requests
import os
from dotenv import load_dotenv
load_dotenv()

# from summarize_code import Summary


class QA:

    def __init__(self, text):
        self.text = text

    def _query_generate(self, payload):
        API_TOKEN = os.environ.get('QUESTION_API_TOKEN')
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.post(
            os.environ.get("QUESTION_API_URL"),
            headers=headers,
            json=payload)
        return response.json()

    def _query_answers(self, payload):
        API_TOKEN = os.environ.get('ANSWER_API_TOKEN')
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.post(
            os.environ.get("ANSWER_API_URL"),
            headers=headers,
            json=payload)
        return response.json()

    def get_questions(self):
        questions_tuple = []
        if len(self.text) > 20:
            for i in range(20):
                output = self._query_generate(
                    {"inputs": "answer:" + self.text[i]})
                questions = output[0]['generated_text']
                questions_tuple.append(questions)
        else:
            for i in range(len(self.text)):
                output = self._query_generate(
                    {"inputs": "answer:" + self.text[i]})
                questions = output[0]['generated_text']
                questions_tuple.append(questions)

        return questions_tuple

    def get_answers(self):
        answers_tuple = []
        question = self.get_questions()
        if len(question) > 20:
            for i in range(20):
                output = self._query_answers(
                    {"inputs": {"question": question[i], "context": self.text[i]}, })
                answer = output['answer']
                answers_tuple.append([question[i], answer])
        else:
            for i in range(len(question)):
                output = self._query_answers(
                    {"inputs": {"question": question[i], "context": self.text[i]}, })
                try:
                    answer = output['answer']
                    score = round(float(output['score']), 3) * 100
                    answers_tuple.append(
                        [question[i], answer, round(score, 3)])
                except KeyError:
                    answer = score = ""
                    answers_tuple.append([question[i], answer, score])

        return answers_tuple
