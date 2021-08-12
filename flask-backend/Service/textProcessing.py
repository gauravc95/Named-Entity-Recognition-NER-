import en_core_web_sm
nlp = en_core_web_sm.load()
def extract_service(input):
    doc = nlp(input)
    #pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])
    # entityDict = defaultdict(list)
    # for X in doc:
    #     entityDict[str(X.label_)].append(str(X.text))
    return [[str(X), str(X.ent_iob_), str(X.ent_type_)] for X in doc]
