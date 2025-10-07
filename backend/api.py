from flask import Flask, request, jsonify
from llama_cpp import Llama


app = Flask(__name__)

# Load the GGUF LLaMA model
llama = Llama(
    model_path="/home/CIN/tcl/projeto/model/Llama-3.2-3B-Instruct-Q6_K.gguf",
    n_ctx=2048)

def get_llama_response(user_prompt, model):
    system_prompt = (
        "You are an assistant that generates Three.js code for meshes only.\n"
        "Given a user's input describing a shape, produce ONLY the JavaScript code that creates the mesh.\n"
        "Do NOT include any code about rendering, scene setup, cameras, lights, or comments.\n"
        "Return only the code creating the mesh, e.g., geometry, material, and mesh creation."
    )

    full_prompt = (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
        f"{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        f"{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )

    return model(prompt=full_prompt, max_tokens=150)


@app.route("/generate", methods=["POST"])
def generate_text():    
    print()
    # Extract input from the request
    input_text = request.json.get("input_text")
    if not input_text:
        return jsonify({"error": "No input_text provided"}), 400

    # Generate text using LLaMA
    response = llama(
        prompt=input_text,
        max_tokens=300)
    return jsonify({"generated_text": response["choices"][0]["text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)