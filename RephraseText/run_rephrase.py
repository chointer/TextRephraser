from rephrase import Rephrase
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--save_txt_path", type=str, default="../temp/rephrase.txt", help="rephrased text file path")
    parser.add_argument("--input_prompt", type=str, default="waling animals", help="original prompt")
    parser.add_argument("--style_type", type=str, default="narrative", help="rephrased style; ['narrative', 'emotional', 'objective']")
    parser.add_argument("--length_type", type=str, default="compress", help="rephrased length: ['compress', 'maintain', 'expand']")

    args = parser.parse_args()

    rephrase = Rephrase()
    
    ### Input
    output = rephrase(args.input_prompt, args.style_type, args.length_type)

    with open(args.save_txt_path, "w") as f:
        f.write(output)