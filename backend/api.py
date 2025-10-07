from flask import Flask, request, jsonify
from llama_cpp import Llama


app = Flask(__name__)



# Load the GGUF LLaMA model
llama = Llama(
    model_path="/home/CIN/tcl/projeto/model/Llama-3.2-3B-Instruct-Q6_K.gguf",
    n_gpu_layers=-1,
    n_ctx=2048)

def get_llama_response(user_prompt, model):
    system_prompt = (
        "You are a writer who creates long html documents based on the path to pages on your blog\n"
        "DO NOT envelop the response around ```html ```. I only want the plaintext, no markdown"
        "make sure the response has <!doctype html>"
        "dont preface your response by things like 'here is an html document'. you must ONLY SERVE THE DOCUMENT" 
    )

    full_prompt = (
        "<|start_header_id|>system<|end_header_id|>\n\n"
        f"{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        f"{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )

    return model(prompt=full_prompt, max_tokens=250)



@app.route("/", methods = ['GET'])
@app.route("/<path:path>", methods = ['GET'])
def catch_all(path=""): 
    
    prompt = path

    ai_data = get_llama_response(prompt, llama)["choices"][0]["text"]

    print(ai_data)

    content_type = ai_data.splitlines()[0]
    response_data = "\n".join(ai_data.splitlines()[1:])
    return response_data, 200, {'Content-Type': content_type}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
####
