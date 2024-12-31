import ollama
import json

class Rephrase:
    def __init__(self, verbose=False) -> None:
        ollama.pull("llama3.2")
        with open("config.json", "r") as f:
            self.prompts = json.load(f)
        self.verbose = verbose

    def _rephrase_style(self, original_prompt, style_type):
        if self.verbose:
            print("--- [STYLE GENERATOR] ---")
            print("\n[SYSTEM]\n", self.prompts["prompt_styles"][style_type] + self.prompts["prompt_style_suffix"])
            print("\n[PROMPT]\n" + original_prompt)

        response_style = ollama.chat(model="llama3.2", messages=[
            {
                "role": "system", "content": self.prompts["prompt_styles"][style_type] + self.prompts["prompt_style_suffix"],
            },
            {
                "role": "user", "content": original_prompt,
            },
        ])

        if self.verbose: 
            print("\n[RESPONSE]\n", response_style["message"]["content"], "\n")

        return response_style["message"]["content"]


    def _rephrase_length(self, original_prompt, rephrased_prompt, length_type, max_iter=10):
        number_of_words_input = len(original_prompt.split())
        response = rephrased_prompt
        
        for i in range(max_iter):
            number_of_words_response = len(rephrased_prompt.split())
            if length_type == "compress" and number_of_words_response <= number_of_words_input * 1.0:
                if self.verbose:
                    print(f"break! {i}")
                break
            elif length_type == "maintain" and number_of_words_response > number_of_words_input * 0.5 and number_of_words_response <= number_of_words_input * 1.5:
                break
            elif length_type == "expand" and number_of_words_response > number_of_words_input * 1.5 and number_of_words_response <= number_of_words_input * 3.0:
                break

            if self.verbose:
                print(f"--- [LENGTH GENERATOR; {i}] ---")
                print("\n[SYSTEM]\n", self.prompts["prompt_length_prefix"] + self.prompts["prompt_lengths"][length_type] + self.prompts["prompt_length_suffix"])
                print("\n[PROMPT]\n", "original version: " + original_prompt + "\nderived version: " + rephrased_prompt)

            response_length = ollama.chat(model="llama3.2", messages=[
                {
                    "role": "system", "content": self.prompts["prompt_length_prefix"] + self.prompts["prompt_lengths"][length_type] + f" The number of words in the original sentence is {number_of_words_input}. " + self.prompts["prompt_length_suffix"],
                },
                {
                    "role": "user", "content": "original version: " + original_prompt + "\nderived version: " + rephrased_prompt,
                },
            ])

            print("\n[RESPONSE]  ", response_length["message"]["content"])
            response = response_length["message"]["content"]

        return response
    
    def __call__(self, input_prompt, style_type, length_type, max_iter=10):
        if self.verbose:
            print("\n\n\n\n\n##### ##### ##### ##### ##### ##### #####")
        styled_prompt = self._rephrase_style(original_prompt=input_prompt, style_type=style_type)
        output = self._rephrase_length(original_prompt=input_prompt, rephrased_prompt=styled_prompt, length_type=length_type, max_iter=max_iter)
        return output