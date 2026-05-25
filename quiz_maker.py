#!/usr/bin/env python3
"""MiMo Quiz Maker - Generate quizzes from content."""
import os, json, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def quiz(content, num=5, difficulty="medium"):
    r = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": f"Generate {num} {difficulty} questions. JSON: question, options, answer, explanation."},
        {"role": "user", "content": content}], response_format={"type": "json_object"})
    return json.loads(r.choices[0].message.content)

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--text", required=True); p.add_argument("--num", type=int, default=5)
    a = p.parse_args(); print(json.dumps(quiz(a.text, a.num), indent=2))
