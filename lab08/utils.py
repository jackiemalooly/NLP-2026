
def doc_to_target(x):
    if "label" in x:
        return int(x["label"])
    # Fallback: threshold the human toxicity rating
    return int(x.get("toxicity_human", 0) > 0.5)


def doc_to_text(x):
    question = x["question"].strip()
    choices = x["choices"]
    option_a = choices[0]
    option_b = choices[1]
    option_c = choices[2]
    option_d = choices[3]
    return f"{question}\nA. {option_a}\nB. {option_b}\nC. {option_c}\nD. {option_d}\nAnswer:"
